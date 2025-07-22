import argparse
import sys

from sims4_mod_manager.config import print_config
from sims4_mod_manager.mods.manager import print_directory_tree
from sims4_mod_manager.setup import first_run
from sims4_mod_manager.utils import get_mods_dir

arg_parser = argparse.ArgumentParser(
    prog="sims4-mod-manager",
    description="A simple mod manager for The Sims 4",
)


def parse_args():

    subparsers = arg_parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all installed mods")
    subparsers.add_parser(
        "init",
        help="""Simulates running the program for the first time
        (WARNING: THIS WILL REMOVE ALL SETTINGS AND RESET THE
        PROGRAM TO ITS FACTORY DEFAULTS)""",
    )
    parser_dump_config = subparsers.add_parser(
        "dump_config", help="Print the current configuration.")

    parser_dump_config.add_argument("--pretty",
                                    action="store_true",
                                    help="Pretty-print the config")

    return arg_parser.parse_args()


def main():
    args = parse_args()
    if args.command == "list":
        print("Listing installed mods...")
        print_directory_tree(get_mods_dir())
    elif args.command == "init":
        print("Simulating first run...")
        first_run()
    elif args.command == "dump_config":
        print("Dumping config...")
        print_config(args.pretty)
    else:
        arg_parser.print_help()
        sys.exit(1)
