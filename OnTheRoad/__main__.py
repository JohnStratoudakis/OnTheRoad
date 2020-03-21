
#from OnTheRoad.BestPath import BestPath
from OnTheRoad.Location import Location
from OnTheRoad.TravelCost import TravelCost

from OnTheRoad.DistanceMatrix import dump_python_matrix
from OnTheRoad.DistanceMatrix import dump_ascii_matrix

import argparse
import logging
from pathlib import Path
import sys

logger = logging.getLogger(__name__.split('.')[0])
LINE_LENGTH = 80

def configure_logging(verbose):
    if verbose:
        logger.setLevel(logging.DEBUG)
        #logging.getLogger().setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        #logging.getLogger().setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)

    formatter_stdout = logging.Formatter(f"%(message)s")
    stream_handler.setFormatter(formatter_stdout)
    logger.addHandler(stream_handler)

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dump the Matrix of distance")

    parser.add_argument("--dump-matrix", action="store_true", help="Dump Matrix of distances")
    parser.add_argument("--cities", help="")
    parser.add_argument("--cities-file", help="File Containing List of Addresses")
    parser.add_argument("--output", help="Where to save Python file")
    parser.add_argument("--verbose", action="store_true", help="Be verbose")

    return parser.parse_args()

def main() -> None:
    args = get_args()
    configure_logging(args.verbose)

    logger.info("-" * LINE_LENGTH)
    logger.info(" + Checking for environment variables")
    logger.info("-" * LINE_LENGTH)
    logger.info(" + Log Level Test")
    logger.info("INFO")
    logger.debug("DEBUG")
    logger.info("-" * LINE_LENGTH)

    if args.dump_matrix:
        logger.info(" + Dumping distance matrix")
        logger.info("-" * LINE_LENGTH)
        if args.cities_file:
            logger.info(f"Using file {args.cities_file}")

            if Path(args.cities_file).exists() == False:
                logger.info(f"Cities file '{args.cities_file}' does not exist")
                sys.exit(1)
            file_in = open(args.cities_file, 'r')
            all_lines = file_in.readlines()
            file_in.close()

            if len(all_lines) == 0:
                logger.info("Empty cities file")
                sys.exit(1)
            all_cities = []

            for line in all_lines:
                line = line.strip()
                parts = line.split(',')
                name = parts[0]
                address_parts = [x.strip() for x in parts[1:]]
                address = ", ".join(address_parts)
                logger.info(f" + Adding:   {name:<10}  {address}")
                all_cities.append(Location(name, name, address))

            logger.info(f"Found {len(all_cities)} addresses")

            logger.info("-" * LINE_LENGTH)
            dump_ascii_matrix(all_cities)
            dump_python_matrix(all_cities, args.output)

if __name__ == "__main__":
    main()