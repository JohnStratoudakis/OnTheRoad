from Travel import TravelCost, Location

import unittest
from unittest import mock
from hamcrest import *

class TravelCostsTests(unittest.TestCase):

    def test_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    @mock.patch.object(TravelCost.TravelCost, 'cost')
    def test_amsterdam_to_brussels(self, mock_input):
        # GIVEN
        mock_input.return_value = [202828, 8372]
        ams = Location.Location("Amsterdam", "ams", "amsterdam, netherlands")
        brussels = Location.Location("Brussels", "bru", "brussels, belgium")

        # WHEN
        [distance_meters, duration_seconds] = TravelCost.TravelCost.cost(ams, brussels)

        # THEN
        self.assertEqual(distance_meters, 202828)
        self.assertEqual(duration_seconds, 8372)

    def test_best_path_may_2019(self):
        # GIVEN
        ams = Location.Location("Amsterdam", "ams", "Amsterdam, Netherlands")
        brussels = Location.Location("Brussels", "bru", "Brussels, Belgium")
        london = Location.Location("London", "lon", "London, United Kingdom")

        # WHEN
        allCosts = TravelCost.TravelCost.allCosts([ams, brussels, london])

        # THEN
        print("allCosts: {}".format(allCosts))
        print("path[0]: {}".format(allCosts[0].getStartCity()))
        assert_that(len(allCosts), equal_to(6))

#        assert_that(1, equal_to(2))

if __name__ == '__main__':
    unittest.main()
