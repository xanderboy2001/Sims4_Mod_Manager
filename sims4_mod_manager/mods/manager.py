"""Module for managing Sims 4 mod directories.

Provides functionality to display the directory tree of the mods folder,
handling permission and missing path errors gracefully.
"""

from pathlib import Path

from sims4_mod_manager.utils import get_mods_dir


def print_directory_tree(start_path: Path, prefix: str = ""):
    """Print the entire directory tree starting at the given path.

    Args:
        start_path (Path): The root directory path to start printing from.
        prefix (str): String prefix used for formatting the tree structure.

    Returns:
        None
    """
    try:
        entries = sorted(start_path.iterdir(), key=lambda p: p.name.lower())
    except PermissionError:
        print(f"{prefix} [Permission Denied]")
        return
    except FileNotFoundError:
        print(f"{prefix} [Path Not Found]")
        return

    for i, entry in enumerate(entries):
        connector = "├── " if i < len(entries) - 1 else "└── "
        entry_str = str(entry).replace(str(get_mods_dir()), ".")
        print(f"{prefix}{connector}{entry_str}")
        if entry.is_dir():
            extension = "│   " if i < len(entries) - 1 else "    "
            print_directory_tree(entry, prefix + extension)
