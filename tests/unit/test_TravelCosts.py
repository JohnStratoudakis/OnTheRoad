from OnTheRoad.Location import Location
from OnTheRoad.TravelCost import TravelCost

from unittest import mock, TestCase
from hamcrest import assert_that, equal_to


class TravelCostsTests(TestCase):
    ams = Location("Amsterdam", "ams", "Amsterdam, Netherlands")
    bru = Location("Brussels", "bru", "Brussels, Belgium")

    def test_travel_costs_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    @staticmethod
    def mock_getDistanceBetween(city_1, city_2):
        allCosts = {
                'ams': {
                    'bru': [212132, 6780]
                    }
                }
        return allCosts[city_1.getShortName()][city_2.getShortName()]

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=mock_getDistanceBetween)
    def test_getDistance_Between_Amsterdam_and_Brussels_no_brackets(self):
        # GIVEN
        # WHEN
        distance, duration = TravelCost.getDistanceBetween(self.ams, self.bru)

        # THEN
        assert_that(distance, equal_to(212132))
        assert_that(duration, equal_to(6780))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=mock_getDistanceBetween)
    def test_amsterdam_to_brussels(self):
        # GIVEN
        # WHEN
        [distance_meters, duration_seconds] = TravelCost.getDistanceBetween(self.ams, self.bru)

        # THEN
        self.assertEqual(distance_meters, 212132)
        self.assertEqual(duration_seconds, 6780)