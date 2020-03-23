
from OnTheRoad import BestPath
from OnTheRoad.Location import Location
from OnTheRoad.TravelCost import TravelCost

from OnTheRoad.DistanceMatrix import dump_python_matrix
from OnTheRoad.DistanceMatrix import dump_ascii_matrix

import argparse
import logging
import os
from pathlib import Path
import sys

logger = logging.getLogger(__name__.split('.')[0])
LINE_LENGTH = 80

def configure_logging(logger, verbose):
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


def is_file(path: str):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a file.")
    return path

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dump the Matrix of distance")

    parser.add_argument("--dump-matrix", action="store_true", help="Dump Matrix of distances")
    parser.add_argument("--cities", help="")
    parser.add_argument("--cities-file", help="File Containing List of Addresses")
    parser.add_argument("--output", help="Where to save Python file")

    parser.add_argument("--goog-api-key", help="Manually specify the GOOG_API_KEY")
    parser.add_argument("--dump-path",
                        help="Dump details of path specified by '<3" +
                             " letter code>-<3 letter code>'")

    parser.add_argument("--calc-path",
                        type=is_file,
                        help="File with newline separated addresses")

    parser.add_argument("--verbose", action="store_true", help="Be verbose")

    return parser.parse_args()

def main() -> None:
    args = get_args()
    configure_logging(logger, args.verbose)

    logger.info("-" * LINE_LENGTH)
    logger.info(" + Checking for environment variables")
    logger.info(" + Checking for GOOG_API_KEY...")
    if args.goog_api_key:
        logger.info(f" + Overriding GOOG_API_KEY...")
        logger.info(f"args.goog_api_key: {args.goog_api_key}")
        os.environ['GOOG_API_KEY'] = args.goog_api_key
    if 'GOOG_API_KEY' in os.environ:
        logger.info("  + GOOG_API_KEY found")
    else:
        logger.error("  - GOOG_API_KEY not found.  Set the environment variable\n"
                     "    or use the override --goog-api-key <GOOG_API_KEY>")
        sys.exit(1)

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
            if args.output:
                dump_python_matrix(all_cities, args.output)
    elif args.dump_path and len(args.dump_path) > 0:
        logger.info(f"Dumping details for path: {args.dump_path}")
        BestPath.dumpPathDetails(args.dump_path)
    elif args.calc_path:
        logger.info(f"Calculating best path for addresses defined in ${args.calc_path}")

        file_in = open(args.calc_path, 'r')
        all_lines = file_in.readlines()
        file_in.close()

        if len(all_lines) == 0:
            logger.info("Empty cities file")
            sys.exit(1)
        all_cities = []

        logger.info(f"Reading address's from {args.calc_path}")
        for line in all_lines:
            line = line.strip()
            parts = line.split(',')
            name = parts[0]
            address_parts = [x.strip() for x in parts[1:]]
            address = ", ".join(address_parts)
            logger.info(f" + Adding:   {name:<10}  {address}")
            all_cities.append(Location(name, name, address))

        if len(all_cities) > 0:
            [best_state, best_fitness] = BestPath.calcTsp(all_cities)

            BestPath.dumpBestPath(all_cities, best_state, best_fitness)

if __name__ == "__main__":
    main()