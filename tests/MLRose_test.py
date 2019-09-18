from Travel import MLRose, Location, TravelCost

import unittest
from unittest import mock
from hamcrest import *

class MLRoseTests(unittest.TestCase):
    nyc = Location.Location("New York", "nyc", "New York City, USA")

    ams = Location.Location("Amsterdam", "ams", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "bru", "Brussels, Belgium")
    lon = Location.Location("London", "lon", "London, United Kingdom")

    vie = Location.Location("Vienna", "vie", "Vienna, Austria")
    bra = Location.Location("Bratislava", "bra", "Bratislava, Slovakia")
    bud = Location.Location("Budapest", "bud", "Budapest, Hungary")
    pra = Location.Location("Prague", "pra", "Prague, Czechia")

    def test_getDistance_BetweenJohn(self):
        # GIVEN

        # WHEN
        distance, duration = TravelCost.TravelCost.getDistanceBetween(self.ams, self.bru)

        # THEN
        assert_that(distance, equal_to(204027))
        assert_that(duration, equal_to(6300))

    def test_genDistList(self):
        # GIVEN
        allCities = [ self.ams, self.bru, self.lon ]

        # WHEN
        mlRose = MLRose.MLRose()
        dist_list = mlRose.genDistList(allCities)

        # THEN
        assert_that(len(dist_list), equal_to(3))
        assert_that(dist_list[0][0], equal_to(0))
        assert_that(dist_list[0][1], equal_to(1))
        assert_that(dist_list[0][2], equal_to(212132))

        assert_that(dist_list[2][0], equal_to(1))
        assert_that(dist_list[2][1], equal_to(2))
        assert_that(dist_list[2][2], equal_to(375174))

    def DISABLED_test_may_trip(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]

        # WHEN
        mlRose = MLRose.MLRose()
        best_state, best_fitness = mlRose.calcTsp(allCities)

        # THEN
        assert_that(best_state[0], equal_to(2))
        assert_that(best_state[1], equal_to(1))
        assert_that(best_state[2], equal_to(0))
        #assert_that(1, equal_to(2))
        print("TSP Best State: {}".format(best_state))
        for city in best_state:
            print(f"{allCities[city]}")
        print("BEST FITNESS: {}".format(best_fitness))

    def test_nov_trip(self):
        # GIVEN
        allCities = [self.nyc, self.vie, self.bud, self.bra, self.pra]

        # WHEN
        mlRose = MLRose.MLRose()
        best_state, best_fitness = mlRose.calcTsp(allCities)

        # THEN
#        assert_that(best_state[0], equal_to(2))
#        assert_that(best_state[1], equal_to(1))
#        assert_that(best_state[2], equal_to(0))
        #assert_that(1, equal_to(2))
        print("TSP Best State: {}".format(best_state))
        for city in best_state:
            print(f"{allCities[city]}")
        print("BEST FITNESS: {}".format(best_fitness))
        assert_that(2, equal_to(0))

