#!/usr/local/bin/python3

from Travel import TravelCost, Location

import unittest

class TravelCostTests(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual("Sugar is bad", "Sugar is bad")

    def test_Amsterdam_to_Brussels(self):
        # GIVEN
        ams = Location.Location("Amsterdam", "Amsterdam, Netherlands")
        brussels = Location.Location("Brussels", "Brussels, Belgium")

        # WHEN
        cost = TravelCost.TravelCost(ams, brussels).cost()

        # THEN
        self.assertEquals(1, 2)
#        #self.assertEquals(cost)

if __name__ == '__main__':
    unittest.main()

