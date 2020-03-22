from OnTheRoad.TravelCost import TravelCost

import logging
from flask.logging import default_handler

logger = logging.getLogger(__name__.split('.')[0])
logger.addHandler(default_handler)


# state is an array of cities to visit
def tsp_fitness(state, c):
    total_cost = 0
    try:
        for i in range(0, len(state)-1):
            shortA = c[state[i]]
            shortB = c[state[i+1]]
            cost = TravelCost.getDistanceBetween(shortA, shortB) [0]
            total_cost += cost
    except Exception as ex:
        print("Exception caught in tsp_fitness: {}".format(str(ex)))
        print("{}".format(ex))
    return total_cost

def calcTsp(allCities):
    from mlrose import TravellingSales, TSPOpt, genetic_alg, CustomFitness
    import numpy as np

    best_state = []
    best_fitness = []

    # Initialize custom fitness function object
    kwargs = {'c': allCities}
    fitness_cust = CustomFitness(tsp_fitness, problem_type='tsp', **kwargs)

    # Define optimization problem object
    tsp_fit = TSPOpt(length = len(allCities), fitness_fn = fitness_cust, maximize = False)

    # Solve using genetic algorithm
    best_state, best_fitness = genetic_alg(problem = tsp_fit,
                                                     pop_size = 20,
                                                     mutation_prob = 0.1,
                                                     max_attempts = 20,
                                                     #max_iters = 2000,
                                                     random_state = 3)

    return [best_state, best_fitness]


def dumpPathDetails(pathString: str):
    if pathString is None or len(pathString) == 0:
        return
    allCities = pathString.strip().split('-')
    if len(allCities) != 2:
        print("Please enter 2 cities at most.  A ciy is the first 3\n" +
              "letters of the last city you searched for.  i.e.\n" +
              "\tprg - Prague")
        return
    startLoc = allCities[0]
    endLoc = allCities[1]

    response_obj = TravelCost.loadCachedResponse(startLoc, endLoc)

    status = "<missing>"
    if "status" in response_obj:
        status = response_obj["status"]
    print(f"Status: {status}")

    if "routes" in response_obj:
        routes = response_obj["routes"]
        print(f"Returned {len(routes)} route(s)")
        for route in routes:
            for key in route.keys():
                if key == "bounds":
                    print("Bounds:")
                    for bound in route[key].keys():
                        print(f"  + {bound}")
                        print(f"     * lat: {route[key][bound]['lat']}")
                        print(f"     * lng: {route[key][bound]['lng']}")
                elif key == "legs":
                    print(f"  + # of legs: {len(route['legs'])}")
                    for leg in route['legs']:
                        print(f"     *  distance: {leg['distance']['text']}")
                        print(f"     *  duration: {leg['duration']['text']}")
                        print(f"     *  start: {leg['start_address']}")
                        print(f"          lat: {leg['start_location']['lat']}")
                        print(f"          lng: {leg['start_location']['lng']}")
                        print(f"     *  end:{leg['end_address']}")
                        print(f"          lat: {leg['end_location']['lat']}")
                        print(f"          lng: {leg['end_location']['lng']}")
#                else:
#                    print(f"Ignoring [route][{key}]")

def dumpBestPath(allCities, best_state, best_fitness):
    print("Recommended Path:")
    full_path_str = ""
    full_dist_str = ""
    full_time_str = ""
    for i in range(len(best_state)-1):
        start = allCities[best_state[i]]
        end = allCities[best_state[i+1]]
        path_str = f"({start.getShortName()} -> {end.getShortName()})"

        dist_meters, duration_seconds = TravelCost.getDistanceBetween(start, end) 
        dist_str = f"{dist_meters:,}{'meters':>8}"
        time_str = f"{duration_seconds:,} seconds"

        full_path_str += f"{path_str:>25}"
        full_dist_str += f"{dist_str:>25}"
        full_time_str += f"{time_str:>25}"

    print(full_path_str)
    print(full_dist_str)
    print(full_time_str)
    print(f"Total Distance: {best_fitness:,} meters")

def genDistList(allCities):
    dist_list = []

    for i in range(len(allCities)):
        for j in range(i, len(allCities)):
            if i != j:
                cost = TravelCost.getDistanceBetween(allCities[i], allCities[j]) [0]
                dist_list.append((i, j, cost))

    return dist_list