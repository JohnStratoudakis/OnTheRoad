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
        ams = Location.Location("amsterdam", "amsterdam, netherlands")
        brussels = Location.Location("brussels", "brussels, belgium")

        # WHEN
        [distance_meters, duration_seconds] = TravelCost.TravelCost.cost(ams, brussels)

        # THEN
        self.assertEqual(distance_meters, 202828)
        self.assertEqual(duration_seconds, 8372)

    def test_fill_out_matrix(self):
        # GIVEN
        ams = Location.Location("Amsterdam", "Amsterdam, Netherlands")
        brussels = Location.Location("Brussels", "Brussels, Belgium")
        london = Location.Location("London", "London, United Kingdom")

        # WHEN

        # THEN

if __name__ == '__main__':
    unittest.main()