from OnTheRoad import TravelCost, Location

import unittest
from unittest import mock
from hamcrest import *

class ServiceTests(unittest.TestCase):
    ams = Location.Location("Amsterdam", "ams", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "bru", "Brussels, Belgium")
    lon = Location.Location("London", "lon", "London, England")

    def test_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    def test_hello(self):
        # GIVEN
        locations = [self.ams, self.bru, self.lon]

        # WHEN
        import requests
        post_data = {}
        post_data['locations'] = []
        for location in locations:
            post_data['locations'].append(
                    [location.getName(), location.getAddress()])

        resp = requests.post('http://127.0.0.1:5000/onTheRoad', json=post_data)

        # THEN
        resp_json = resp.json()
        print(f"resp_json: {resp_json}")

        assert_that(resp_json['status'], equal_to(200))
        assert_that(resp_json['best_path'], has_length(3))

#    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=mock_getDistanceBetween)
    def DISABLED_test_amsterdam_to_brussels(self):
        # GIVEN
        #mock_input.return_value = [202828, 8372]
        ams = Location.Location("Amsterdam", "ams", "amsterdam, netherlands")
        brussels = Location.Location("Brussels", "bru", "brussels, belgium")

        # WHEN
        #[distance_meters, duration_seconds] = TravelCost.TravelCost.cost(ams, brussels)

        # THEN
        #self.assertEqual(distance_meters, 212132)
        #self.assertEqual(duration_seconds, 6780)

if __name__ == '__main__':
    unittest.main()
