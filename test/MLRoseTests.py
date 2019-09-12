from Travel import MLRose, Location

import unittest
from unittest import mock
from hamcrest import *

class MLRoseTests(unittest.TestCase):
    ams = Location.Location("Amsterdam", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "Brussels, Belgium")
    lon = Location.Location("London", "London, United Kingdom")

    def DISABLED_test_8queens(self):
        mlRose = MLRose.MLRose()
        mlRose.test()
        assert_that(2, equal_to(2))

    def test_genDistList(self):
        # GIVEN
        allCities = [ self.ams, self.bru, self.lon ]

        # WHEN
        #dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), (0, 5, 5.3852), \
        mlRose = MLRose.MLRose()
        dist_list = mlRose.genDistList(allCities)

        # THEN
        assert_that(len(dist_list), equal_to(6))
        assert_that(1, equal_to(2))

    def DISABLED_test_three_cities(self):
        # GIVEN
        ams = Location.Location("Amsterdam", "Amsterdam, Netherlands")
        bru = Location.Location("Brussels", "Brussels, Belgium")
        lon = Location.Location("London", "London, United Kingdom")

        # WHEN
        mlRose = MLRose.MLRose()
        mlRose.test_tsp([ams, bru, lon])
        #bestPath = MLRose.MLRose.getBestPath([ams, brussels, london])

        # THEN
        #assert_that(1, equal_to(2))

