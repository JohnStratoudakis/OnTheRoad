from OnTheRoad import TravelCost, Location

import unittest
from unittest import mock
from hamcrest import *

class TravelCostsTests(unittest.TestCase):
    ams = Location.Location("Amsterdam", "ams", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "bru", "Brussels, Belgium")

    def test_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    def mock_getDistanceBetween(city_1, city_2):
        allCosts = {
                'ams': {
                    'bru': [212132, 6780]
                    }
                }
        return allCosts[city_1.getShortName()][city_2.getShortName()]

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=mock_getDistanceBetween)
    def test_getDistance_Between_Amsterdam_and_Brussels(self):
        # GIVEN
        # WHEN
        distance, duration = TravelCost.TravelCost.getDistanceBetween(self.ams, self.bru)

        # THEN
        assert_that(distance, equal_to(212132))
        assert_that(duration, equal_to(6780))

    #@mock.patch.object(TravelCost.TravelCost, 'cost')
    #def test_amsterdam_to_brussels(self, mock_input):
    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=mock_getDistanceBetween)
    def test_amsterdam_to_brussels(self):
        # GIVEN
        #mock_input.return_value = [202828, 8372]
        ams = Location.Location("Amsterdam", "ams", "amsterdam, netherlands")
        brussels = Location.Location("Brussels", "bru", "brussels, belgium")

        # WHEN
        [distance_meters, duration_seconds] = TravelCost.TravelCost.cost(ams, brussels)

        # THEN
        self.assertEqual(distance_meters, 212132)
        self.assertEqual(duration_seconds, 6780)

if __name__ == '__main__':
    unittest.main()
