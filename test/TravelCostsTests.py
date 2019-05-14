from Travel import TravelCost, Location

import unittest
from unittest import mock
from hamcrest import *

class TravelCostTests(unittest.TestCase):

    def test_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))
        #self.assertEqual("Sugar is bad", "Sugar is bad")

    def test_amsterdam_to_brussels(self):
        # given
        ams = Location.Location("amsterdam", "amsterdam, netherlands")
        brussels = Location.Location("brussels", "brussels, belgium")

        # when
        [distance_meters, duration_seconds] = TravelCost.TravelCost(ams, brussels).cost()

        # then
        self.assertEqual(distance_meters, 202828)
        self.assertEqual(duration_seconds, 8372)


    def test_brussels_to_london(self):
        # given
        brussels = Location.Location("brussels", "brussels, belgium")
        london = Location.Location("london", "london, united kingdom")

        # when
        [distance_meters, duration_seconds] = TravelCost.TravelCost(brussels, london).cost()

        # then
        self.assertEqual(distance_meters, 375174)
        self.assertEqual(duration_seconds, 7260)


if __name__ == '__main__':
    unittest.main()