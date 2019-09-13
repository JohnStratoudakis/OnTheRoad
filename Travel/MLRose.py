from Travel import MLRose, Location, TravelCost

def queens_max(state):

    # Initialize counter
    fitness = 0

    # For all pairs of queens
    for i in range(len(state) - 1):
        for j in range(i + 1, len(state)):

            # Check for horizontal, diagonal-up and diagonal-down attacks
            if (state[j] != state[i]) \
                and (state[j] != state[i] + (j - i)) \
                and (state[j] != state[i] - (j - i)):

                # If no attacks, then increment counter
                fitness += 1
    return fitness

class MLRose:
    def __init__(self):
        pass

    def test_8queens(self):
        print("TEST")
        import mlrose
        import numpy as np

        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
        from sklearn.metrics import accuracy_score

        # Initialize custom fitness function object
        fitness_cust = mlrose.CustomFitness(queens_max)

        ## Initialize fitness function object using pre-defined class
        #fitness = mlrose.Queens()

        # Define optimization problem object
        problem = mlrose.DiscreteOpt(length = 8, fitness_fn = fitness_cust, maximize=False, max_val=8)

        # Define decay schedule
        schedule = mlrose.ExpDecay()

        # Solve using simulated annealing - attempt 1
        init_state = np.array([0, 1, 2, 3, 4, 5, 6, 7])
        best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule, max_attempts = 10,
                                                            max_iters = 1000, init_state = init_state,
                                                            random_state = 1)
        print('The best state found is: ', best_state)
        print('The fitness at the best state is: ', best_fitness)

    def calcTsp(self, allCities):
        import mlrose

        dist_list = self.genDistList(allCities)

        # Initialize fitness function object using dist_list
        fitness_dists = mlrose.TravellingSales(distances = dist_list)

        # Define optimization problem object
        problem_fit2 = mlrose.TSPOpt(length = len(dist_list), fitness_fn = fitness_dists, maximize = False)

        # Solve using genetic algorithm
        best_state, best_fitness = mlrose.genetic_alg(problem_fit2, mutation_prob = 0.2, max_attempts = 100,
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
