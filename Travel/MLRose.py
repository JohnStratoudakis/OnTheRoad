from Travel import MLRose, Location, TravelCost

class MLRose:
    def __init__(self):
        pass

    def calcTsp(self, allCities):
        import mlrose

        dist_list = self.genDistList(allCities)

        # Initialize fitness function object using dist_list
        fitness_dists = mlrose.TravellingSales(distances = dist_list)

        # Define optimization problem object
        problem_fit2 = mlrose.TSPOpt(length = len(dist_list), fitness_fn = fitness_dists, maximize = False)

        # Solve using genetic algorithm
        best_state, best_fitness = mlrose.genetic_alg(problem_fit2,
                                                    mutation_prob = 0.01,
                                                    max_attempts = 200,
                                                    random_state = 2)

        return best_state, best_fitness

    def genDistList(self, allCities):
        dist_list = []

        for i in range(len(allCities)):
            for j in range(i, len(allCities)):
                if i != j:
                    print(f"i {i}, j {j}")
                    dist_list.append((i, j, TravelCost.TravelCost.getDistanceBetween(allCities[i], allCities[j])[0]))

        return dist_list
