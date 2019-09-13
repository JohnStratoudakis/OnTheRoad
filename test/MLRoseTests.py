from Travel import MLRose, Location, TravelCost

import unittest
from unittest import mock
from hamcrest import *

class MLRoseTests(unittest.TestCase):
    ams = Location.Location("Amsterdam", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "Brussels, Belgium")
    lon = Location.Location("London", "London, United Kingdom")

    def DISABLED_test_8queens(self):
        mlRose = MLRose.MLRose()
        mlRose.test_8queens()
        assert_that(2, equal_to(2))

    def test_getDistance_Between(self):
        # GIVEN
        
        # WHEN
        distance = TravelCost.TravelCost.getDistanceBetween(self.ams, self.bru)[0]

        # THEN
        assert_that(distance, equal_to(202828))

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
        assert_that(dist_list[0][2], equal_to(202828))

        assert_that(dist_list[2][0], equal_to(1))
        assert_that(dist_list[2][1], equal_to(2))
        assert_that(dist_list[2][2], equal_to(375174))

    def test_three_cities(self):
        # GIVEN
        allCities = [ self.ams, self.bru, self.lon ]

        # WHEN
        mlRose = MLRose.MLRose()
        best_state, best_fitness = mlRose.calcTsp(allCities)

        # THEN
        assert_that(best_state[0], equal_to(2))
        assert_that(best_state[1], equal_to(1))
        assert_that(best_state[2], equal_to(0))
        #assert_that(1, equal_to(2))
        #print("TSP Best State: {}".format(best_state))
        #print("BEST FITNESS: {}".format(best_fitness))

