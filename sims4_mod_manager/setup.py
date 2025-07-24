"""Setup routines for the Sims 4 Mod Manager.

This module provides logic to detect and handle the first-time setup,
including creation of the default configuration file.
"""
from sims4_mod_manager.config import create_default_config
from sims4_mod_manager.utils import config_file_path


def is_first_run() -> bool:
    """Determine whether this is the first time the program has been run.

    Returns:
        bool: True if the configuration file does not exist; otherwise, False.
    """
    return not config_file_path.exists()


def first_run():
    """Perform initial setup tasks, such as creating the default config file."""
    create_default_config()
