""" OnTheRoad
Calculates optimal path between a list of cities using
the Google Maps API.

Pass list of cities with one city on each line, i.e.
----sample_addrs.txt---
Bratislava, Slovenia
Budapest, Hungary
Vienna, Austria
"""

import argparse
import os
from typing import Tuple

from OnTheRoad import Location, BestPath

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
            required=True
            )
    parser.add_argument(
            "-g",
            "--google_api_key",
            type=str,
            help="Google Directions API Key",
            )
    args = parser.parse_args()
    if args.file:
        print(f"Address File: {args.file}")

    return (args.file, args.google_api_key)

def main() -> None:
    (address_file, google_api_key) = parse_args()

    address_list = []
    if address_file:
        print(f"Reading address's from {address_file}")
        with open(address_file, 'rt') as fin:
            for line in fin:
                addr_short = line.split(',')[0]
                loc = Location.Location(addr_short, addr_short, line)
                address_list.append(loc)

    if google_api_key:
        print(f"Overriding Google API Key with user supplied value")

    best_state, best_fitness = BestPath.calcTsp(address_list)

    print(f"Best Path")
    for city in best_state:
        print(f"({city.getShortName()})")

if __name__ == "__main__":
    main()
