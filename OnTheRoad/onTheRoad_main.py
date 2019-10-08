#!/usr/bin/python3.7

import argparse
import os
from typing import Tuple

def is_file(path: str):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a file.")
    return path

def parse_args() -> Tuple[str]:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
               "-f",
               "--file",
               type=is_file,
               help="File with newline separated addresses",
               )
    args = parser.parse_args()
    if args.file:
        print(f"File: {args.file}")

    return (args.file)

def main() -> None:
    (address_file) = parse_args()


if __name__ == "__main__":
    main()
