from OnTheRoad import Location, TravelCost

# state is an array of cities to visit
def tsp_fitness(state, c):
    total_cost = 0
    try:
        for i in range(0, len(state)-1):
            shortA = c[state[i]]
            shortB = c[state[i+1]]
            cost = TravelCost.TravelCost.getDistanceBetween(shortA, shortB) [0]
            total_cost += cost
    except Exception as ex:
        print("Exception caught in tsp_fitness: {}".format(ex))
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

def genDistList(allCities):
    dist_list = []

    for i in range(len(allCities)):
        for j in range(i, len(allCities)):
            if i != j:
                cost = TravelCost.TravelCost.getDistanceBetween(allCities[i], allCities[j]) [0]
                dist_list.append((i, j, cost))

    return dist_list
