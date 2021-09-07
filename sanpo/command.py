# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
import argparse


def _parsed_args():
    parser = argparse.ArgumentParser(description="Sanitize PO files from gettext for version control")
    parser.add(
        "po_files",
        metavar="PO_FILE",
        type=argparse.FileType("r"),
        nargs="+",
        help="PO file(s) to sanitize",
    )
    return parser.parse_args()


def main():
    print("hello")


if __name__ == "__main__":
    main()
