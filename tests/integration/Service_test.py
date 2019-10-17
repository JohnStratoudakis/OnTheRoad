from OnTheRoad import TravelCost, Location

#from tests.unit.BestPath_test import BestPathTest
import tests.unit.MockDistance

import unittest
from unittest import mock
from hamcrest import *

class ServiceTests(unittest.TestCase):

    # An actual Euro Trip I did in May of 2019
    # I flew in to Amsterdam, and flew out from London
    ams = Location.Location("Amsterdam", "ams", "Amsterdam, Netherlands")
    bru = Location.Location("Brussels", "bru", "Brussels, Belgium")
    lon = Location.Location("London", "lon", "London, United Kingdom")

    # I want to figure out which of the following cities I should
    # travel to on my next Euro Trip
    vie = Location.Location("Vienna", "vie", "Vienna, Austria")
    bra = Location.Location("Bratislava", "bra", "Bratislava, Slovakia")
    bud = Location.Location("Budapest", "bud", "Budapest, Hungary")
    pra = Location.Location("Prague", "pra", "Prague, Czechia")

    def test_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_ams_bru_lon(self):
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

        # THEN
        #self.assertEqual(distance_meters, 212132)
        #self.assertEqual(duration_seconds, 6780)

if __name__ == '__main__':
    unittest.main()
