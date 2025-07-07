from pathlib import Path
import platform
import os
import unittest
from unittest.mock import patch, mock_open


# ----------- Downloads Directory Logic -----------

def get_linux_downloads_folder() -> Path:
    config_file = Path.home() / ".config/user-dirs.dirs"
    if config_file.exists():
        with config_file.open() as f:
            for line in f:
                if line.startswith("XDG_DOWNLOAD_DIR"):
                    path = line.split("=")[1].strip().strip('"')
                    path = path.replace("$HOME", str(Path.home()))
                    return Path(path)
    return Path.home() / "Downloads"


def get_windows_downloads_folder() -> Path:
    return Path.home() / "Downloads"


def get_macos_downloads_folder() -> Path:
    return Path.home() / "Downloads"


def get_downloads_folder() -> Path:
    system = platform.system()
    if system == "Linux":
        return get_linux_downloads_folder()
    elif system == "Windows":
        return get_windows_downloads_folder()
    elif system == "Darwin":
        return get_macos_downloads_folder()
    else:
        raise OSError(f"Unsupported OS: {system}")


# ----------- Unit Tests -----------

class TestDownloadsFolderDetection(unittest.TestCase):

    @patch('platform.system', return_value='Windows')
    def test_windows_downloads(self, mock_system):
        expected = Path.home() / "Downloads"
        self.assertEqual(get_downloads_folder(), expected)

    @patch('platform.system', return_value='Darwin')
    def test_macos_downloads(self, mock_system):
        expected = Path.home() / "Downloads"
        self.assertEqual(get_downloads_folder(), expected)

    @patch('platform.system', return_value='Linux')
    @patch('pathlib.Path.exists', return_value=False)
    def test_linux_downloads_fallback(self, mock_exists, mock_system):
        expected = Path.home() / "Downloads"
        self.assertEqual(get_downloads_folder(), expected)

    @patch('platform.system', return_value='Linux')
    @patch('pathlib.Path.exists', return_value=True)
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='XDG_DOWNLOAD_DIR="$HOME/CustomDownloads"\n')
    def test_linux_downloads_from_xdg_config(self, mock_file, mock_exists, mock_system):
        expected = Path.home() / "CustomDownloads"
        self.assertEqual(get_downloads_folder(), expected)

    @patch('platform.system', return_value='Solaris')
    def test_unknown_os(self, mock_system):
        with self.assertRaises(OSError):
            get_downloads_folder()


# ----------- Optional: Run directly -----------

if __name__ == '__main__':
    unittest.main()
