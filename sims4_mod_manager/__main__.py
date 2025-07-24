"""
Entry point for the Sims 4 Mod Manager CLI application.

This script checks if the application is being run for the first time,
and if so, it initializes the default configuration. It then delegates
to the main CLI interface defined in the `cli` module.

Modules:
    - sims4_mod_manager.setup: Handles first-run logic and config initialization.
    - sims4_mod_manager.cli: Defines and runs the command-line interface.

Usage:
    python -m sims4_mod_manager
"""

from sims4_mod_manager.cli import main
from sims4_mod_manager.setup import create_default_config, is_first_run

if __name__ == "__main__":
    if is_first_run():
        print("This is the first run. Creating default config...")
        create_default_config()
    main()
