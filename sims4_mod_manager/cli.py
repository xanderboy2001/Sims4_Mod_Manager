"""Command-line interface for the Sims 4 Mod Manager.

This module defines the CLI commands available to users, such as listing
installed mods, resetting the configuration, printing the current config,
and scanning for mod metadata.

Functions:
    cmd_list(args): Lists all installed mods.
    cmd_init(args): Simulates a first run and resets config if '--force' is passed.
    cmd_dump_config(args): Prints the current configuration.
    cmd_scan(args): Scans mods directory for files and writes metadata.
    parse_args(): Parses CLI arguments.
    main(): Entry point for CLI command execution.
"""

import argparse
import sys
from collections.abc import Callable

from sims4_mod_manager.config import print_config
from sims4_mod_manager.mods.manager import print_directory_tree
from sims4_mod_manager.mods.metadata import get_metadata, write_metadata
from sims4_mod_manager.setup import first_run
from sims4_mod_manager.utils import get_mods_dir


def cmd_list(args: argparse.Namespace) -> None:
    """Handle the 'list' command.

    Prints a tree view of all mods installed in the configured mods directory.
    """
    print("Listing installed mods...")
    print_directory_tree(get_mods_dir())


def cmd_init(args: argparse.Namespace) -> None:
    """Handle the 'init' command.

    Simulates a first run by resetting the program configuration.
    Requires the '--force' flag to proceed.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    """
    if args.force:
        print("Simulating first run...")
        first_run()
    else:
        print("Use --force to reset the program.")
        sys.exit(1)


def cmd_dump_config(args: argparse.Namespace) -> None:
    """Handle the 'init' command.

    Simulates a first run by resetting the program configuration.
    Requires the '--force' flag to proceed.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    """
    print("Dumping config...")
    print_config(args.pretty)


def cmd_scan(args: argparse.Namespace) -> None:
    """Handle the 'scan' command.

    Scans the mods directory for supported mod file types and writes metadata.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    """
    metadata = None
    if args.extensions:
        metadata = get_metadata(args.extensions)
    write_metadata(metadata)
    print("wrote metadata")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog="sims4-mod-manager",
        description="A simple mod manager for The Sims 4",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_list = subparsers.add_parser("list", help="List all installed mods")

    parser_init = subparsers.add_parser(
        "init",
        help="""Simulates running the program for the first time
        (WARNING: THIS WILL REMOVE ALL SETTINGS AND RESET THE
        PROGRAM TO ITS FACTORY DEFAULTS) Run with '--force' to execute.""",
    )
    parser_init.add_argument(
        "--force", action="store_true", help="Use this to reset the program."
    )

    parser_config = subparsers.add_parser(
        "dump_config", help="Print the current configuration."
    )
    parser_config.add_argument(
        "--pretty", action="store_true", help="Pretty-print the config"
    )

    parser_scan = subparsers.add_parser(
        "scan", help="Scan Mods folder for all '.package' and '.ts4script' files."
    )
    parser_scan.add_argument(
        "extensions",
        nargs="*",
        help="Optional extension or extensions to scan for (packages or scripts)",
    )

    return parser.parse_args()


def main() -> None:
    """Main entry point for the CLI.

    Parses arguments and dispatches the appropriate command handler.
    """
    args = parse_args()
    commands: dict[str, Callable[[argparse.Namespace], None]] = {
        "list": cmd_list,
        "init": cmd_init,
        "dump_config": cmd_dump_config,
        "scan": cmd_scan,
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)
    else:
        print("Unknown command")
        sys.exit(1)
