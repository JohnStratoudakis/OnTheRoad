from Travel import MLRose, Location, TravelCost

class MLRose:
    def __init__(self):
        pass

    def calcTsp(self, allCities):
        from mlrose import TravellingSales, TSPOpt, genetic_alg
        import numpy as np

        dists = self.genDistList(allCities)
        print("Dumping dist_list")
        for i in range(len(dists)):
            index_1 = dists[i][0]
            index_2 = dists[i][1]
            city_1 = allCities[ index_1 ].getShortName() + f"({index_1})"
            city_2 = allCities[ index_2 ].getShortName() + f"({index_2})"
            varType = type(dists[i])
            print(f"type: {varType} - [{i}] = {city_1} - {city_2} - {dists[i][2]}")

        # Initialize fitness function object using dists
        fitness_dists = TravellingSales(distances=dists)

        # Define optimization problem object
        tsp_fit = TSPOpt(length = len(allCities), fitness_fn = fitness_dists, maximize = False)

        # Solve using genetic algorithm
        best_state, best_fitness, fit_curve = genetic_alg(problem = tsp_fit,
                                                    mutation_prob = 0.1,
                                                    max_attempts = 20000,
                                                    #max_iters = 2000,
                                                    curve = True,
                                                    random_state = 2)
        #for i in range(len(fit_curve)-2, len(fit_curve)):
        #    print(f"[{i}] = {fit_curve}")
        return best_state, best_fitness

    def genDistList(self, allCities):
        dist_list = []

        for i in range(len(allCities)):
            for j in range(i, len(allCities)):
                if i != j:
                    cost = TravelCost.TravelCost.getDistanceBetween(allCities[i], allCities[j]) [0]
                    print(f"(i {i}, j {j}, {cost})")
                    dist_list.append((i, j, cost/10000))

        return dist_list

