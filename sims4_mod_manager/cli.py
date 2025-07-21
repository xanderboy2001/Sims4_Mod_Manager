import argparse
import sys


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
        # TODO: Implement dir walk to organize mods by folder
    else:
        parser.print_help()
        sys.exit(1)
