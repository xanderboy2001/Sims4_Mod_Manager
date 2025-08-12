"""Configuration management for the Sims 4 Mod Manager.

Handles creation, loading, and printing of user configuration files,
including paths for mods and downloads directories.
"""

import json

from platformdirs import user_downloads_dir

from sims4_mod_manager.utils import config_file_path, get_mods_dir

DEFAULT_CONFIG = {
    "paths": {
        "mods_folder": str(get_mods_dir()),
        "downloads_folder": str(user_downloads_dir()),
    }
}


def create_default_config() -> None:
    """Create the default configuration file with mod and download paths.

    Ensures the config directory exists before writing the default
    JSON configuration to disk.
    """
    config_file_path.parent.mkdir(parents=True, exist_ok=True)
    with config_file_path.open("w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)


def load_config() -> dict[str, dict[str, str]]:
    """Load and return the configuration from the JSON config file.

    Returns:
        dict: The configuration data loaded from file.
    """
    with config_file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def print_config(pretty=False) -> None:
    """Print the current configuration to standard output.

    Args:
        pretty (bool): If True, pretty-prints the JSON configuration;
            otherwise, prints compact JSON.
    """
    config = load_config()
    if pretty:
        print(json.dumps(config, indent=4))
    else:
        print(json.dumps(config))
