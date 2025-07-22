import argparse
import sys

from sims4_mod_manager.mods.manager import print_directory_tree
from sims4_mod_manager.setup import first_run
from sims4_mod_manager.utils import get_mods_dir


def main():
    parser = argparse.ArgumentParser(
        prog="sims4-mod-manager",
        description="A simple mod manager for The Sims 4",
    )

    parser.add_argument(
        "--first_run",
        help="""Simulates running the program for the first time
        (WARNING: THIS WILL REMOVE ALL SETTINGS AND RESET THE
        PROGRAM TO ITS FACTORY DEFAULTS)""",
        action="store_true",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all installed mods")

    args = parser.parse_args()

    if args.first_run:
        print("Simulating first run...")
        first_run()

    if args.command == "list":
        print("Listing installed mods...")
        print_directory_tree(get_mods_dir())
    else:
        parser.print_help()
        sys.exit(1)
