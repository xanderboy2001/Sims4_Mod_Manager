"""Metadata management for Sims 4 mods.

Provides functions to scan the mods directory for files, extract metadata,
and read/write metadata to a JSON data file.
"""

import json
from pathlib import Path

from sims4_mod_manager.utils import data_dir, get_mods_dir

PATTERN_MAP = {"package": "*.package", "script": "*.ts4script"}
EXTENSION_MAP = {".package": "Package", ".ts4script": "Script"}

DATA_FILE = data_dir / "metadata.json"


class Mod_File:
    """Represents a Sims 4 mod file and its associated metadata."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.filename = self.filepath.name
        self.filetype = self._determine_type()
        self.author = self._determine_author()

    def _determine_type(self) -> str:
        """Return the file type based on its extension."""
        return EXTENSION_MAP.get(self.filepath.suffix.lower(), "Unknown")

    def _determine_author(self) -> str:
        if "_" in self.filename:
            pieces = self.filename.split("_")
            # Whicked Whims animations start are in the following format:
            # WW_{authorname}_{animationname}
            if pieces[0] == "WW":
                return pieces[1]
            else:
                return pieces[0]
        else:
            return "Unknown"

    def get_filename(self) -> str:
        """Return the filename of the mod file."""
        return self.filename

    def get_type(self) -> str:
        """Return the file type of the mod file."""
        return self.filetype


def get_metadata(filetypes: str | list[str] | None = None) -> list[dict[str, str]]:
    """Scan the mods directory for specified file types and collect metadata.

    Args:
        filetypes (str | list[str] | None): File types to search for. Accepts a string,
            a list of strings, or None.
            If None, defaults to both 'package' and 'script'.

    Returns:
        list[dict[str, str]]: A list of metadata dictionaries for each matched file.
    """
    # If filetypes weren't passed, set to default
    if not filetypes:
        filetypes = ["package", "script"]
    else:
        # If we passed a single string, convert it to a list
        if isinstance(filetypes, str):
            filetypes = [filetypes]

    # Normalize filetypes and allowed extensions
    normalized = [filetype.lower() for filetype in filetypes]

    # Accept both friendly names and raw extensions
    allowed_suffixes = set()
    for filetype in normalized:
        if filetype.startswith("."):
            allowed_suffixes.add(filetype)  # raw extension
        else:
            # friendly name lookup
            for ext, type_name in EXTENSION_MAP.items():
                if type_name.lower() == filetype:
                    allowed_suffixes.add(ext.lower())

    directory = get_mods_dir()
    metadata_list = []

    for file in directory.rglob("*"):
        if file.is_file() and file.suffix.lower() in allowed_suffixes:
            # Extract filename, path, and get type based on dictionary mapping
            try:
                mod = Mod_File(file)
                metadata = {
                    "filename": mod.filename,
                    "path": str(file.relative_to(directory)),
                    "type": mod.filetype,
                    "author": mod.author,
                }
                metadata_list.append(metadata)
                # print(type(file))
            except (OSError, ValueError) as e:
                print(f"Skipping {file}: {e}")
    return metadata_list


def write_metadata(metadata: list[dict[str, str]] | None = None) -> None:
    """Write metadata to the metadata JSON file.

    Args:
        filetypes (str | list[str] | None): OPtional filter for file types.
    """
    metadata = get_metadata()
    data_dir.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)


def load_metadata() -> list[dict[str, str]]:
    """Load and return metadata from the metadata JSON file.

    Returns:
        list[dict[str, str]]: Metadata previously saved to disk.
    """
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)
