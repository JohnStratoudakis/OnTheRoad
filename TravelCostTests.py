#!/usr/local/bin/python3

import TravelCost

import unittest

class TravelCostTests(unittest.TestCase):

    def test_smoke(self):
        self.assertEquals("Sugar is bad", "Sugar is bad")

    def test_Athens_to_Lisbon(self):
        # GIVEN
        athens = Location("Athens, Greece")
        lisbon = Location("Lisbon, Portugal")

        # WHEN
        cost = TravelCost(athens, lisbon).cost()

        # THEN
        self.assertEquals(cost

if __name__ == '__main__':
    unittest.main()

