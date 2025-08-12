"""Utility functions and constants for Sims 4 Mod Manager.

Provides OS detection, config and data directory paths, and
determines the location of the Sims 4 Mods folder based on the OS.
"""
import sys
from pathlib import Path
from typing import Literal

from platformdirs import user_config_dir, user_data_dir, user_documents_dir

APP_NAME = "Sims4ModManager"
CONFIG_FILENAME = "config.json"

config_file_path: Path = Path(user_config_dir(APP_NAME)) / CONFIG_FILENAME

data_dir: Path = Path(user_data_dir(APP_NAME))


def get_os() -> Literal["windows", "mac", "linux", "unknown"]:
    """Detect the current operating system.

    Returns:
        Literal["windows", "mac", "linux", "unknown"]: OS identifier string.
    """
    platform_name = sys.platform
    if platform_name.startswith("win"):
        return "windows"
    elif platform_name.startswith("darwin"):
        return "mac"
    elif platform_name.startswith("linux"):
        return "linux"
    else:
        return "unknown"


def get_mods_dir() -> Path:
    """Get the default path to the Sims 4 Mods directory based on the OS.

    Returns:
        Path: The path to the Mods folder.
    """
    os_name = get_os()
    if os_name in ("windows", "mac"):
        return Path(user_documents_dir()/"Electronic Arts/The Sims 4/Mods")
    elif os_name == "linux":
        return (
            Path.home()
            / ".local/share/Steam/steamapps/compatdata/1222670/pfx"
            / "drive_c/users/steamuser/Documents/Electronic Arts/The Sims 4/Mods"
        )
