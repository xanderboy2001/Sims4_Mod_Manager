import argparse
import sys
from sims4_mod_manager.utils import get_mods_dir
from sims4_mod_manager.mods.manager import print_directory_tree


def main():
    parser = argparse.ArgumentParser(
        prog="sims4-mod-manager",
        description="A simple mod manager for The Sims 4",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all installed mods")

    args = parser.parse_args()

    if args.command == "list":
        print("Listing installed mods...")
        print_directory_tree(get_mods_dir())
    else:
        parser.print_help()
        sys.exit(1)
