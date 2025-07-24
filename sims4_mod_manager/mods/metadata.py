"""Metadata management for Sims 4 mods.

Provides functions to scan the mods directory for files, extract metadata,
and read/write metadata to a JSON data file.
"""
import json

from sims4_mod_manager.utils import data_dir, get_mods_dir

PATTERN_MAP = {"package": "*.package", "script": "*.ts4script"}
EXTENSION_MAP = {".package": "Package", ".ts4script": "Script"}

DATA_FILE = data_dir / "metadata.json"


def get_metadata(filetypes: str | list[str] | None = None) -> list[dict[str, str]]:
    """Scan the mods directory for specified file types and collect metadata.

    Args:
        filetypes (str | list[str] | None): File types to search for. Accepts a string,
            a list of strings, or None.
            If None, defaults to both 'package' and 'script'.

    Returns:
        list[dict[str, str]]: A list of metadata dictionaries for each matched file.
    """
    if not filetypes:
        filetypes = ["package", "script"]
    else:
        if isinstance(filetypes, str):
            filetypes = [filetypes]
    directory = get_mods_dir()
    metadata_list = []
    patterns = []

    for filetype in filetypes:
        patterns.append(PATTERN_MAP[filetype.lower()])

    for pattern in patterns:
        for file in directory.rglob(pattern):
            try:
                metadata = {
                    "filename": file.name,
                    "path": str(file.resolve()),
                    "type": EXTENSION_MAP.get(file.suffix.lower(), "Unknown"),
                }
                metadata_list.append(metadata)
            except (OSError, ValueError) as e:
                print(f"Skipping {file}: {e}")
    return metadata_list


def write_metadata(metadata: list[dict[str, str]] | None = None) -> None:
    """Write metadata to the metadata JSON file.

    If no metadata is passed, new metadata will be generated from the mods directory.

    Args:
        metadata (list[dict[str, str]] | None): Metadata to write.
            If None, data will be freshly generated.
    """
    if not metadata:
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
