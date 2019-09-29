from Travel import BestPath, Location, TravelCost

import unittest
from unittest import mock
from hamcrest import *

class BestPathTests(unittest.TestCase):
    # nyc is home for me, so optimal use of this algorithm is for me to
    # start there
    nyc = Location.Location("New York", "nyc", "New York City, USA")

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

    def mock_getDistanceBetween(city_1, city_2):
        allCosts = {
                'ams': {
                    'bru': [212132, 6780],
                    'lon': [587306, 6780]
                    },
                'bru': {
                    'lon': [375174, 6780]
                    }
                }
        return allCosts[city_1.getShortName()][city_2.getShortName()]

    @mock.patch('Travel.TravelCost.TravelCost.getDistanceBetween', 
                 new=mock_getDistanceBetween)
    def test_generate_Distances_List(self):
        # GIVEN
        allCities = [ self.ams, self.bru, self.lon ]

        # WHEN
        dist_list = BestPath.genDistList(allCities)

        # THEN
        assert_that(len(dist_list), equal_to(3))
        assert_that(dist_list[0][0], equal_to(0))
        assert_that(dist_list[0][1], equal_to(1))
        assert_that(dist_list[0][2], equal_to(212132))

        assert_that(dist_list[1][0], equal_to(0))
        assert_that(dist_list[1][1], equal_to(2))
        assert_that(dist_list[1][2], equal_to(587306))

        assert_that(dist_list[2][0], equal_to(1))
        assert_that(dist_list[2][1], equal_to(2))
        assert_that(dist_list[2][2], equal_to(375174))

    @mock.patch('Travel.TravelCost.TravelCost.getDistanceBetween', 
                 new=mock_getDistanceBetween)
    def DISABLED_test_may_trip(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        assert_that(best_state[0], equal_to(2))
        assert_that(best_state[1], equal_to(1))
        assert_that(best_state[2], equal_to(0))
        #assert_that(1, equal_to(2))
        print("TSP Best State: {}".format(best_state))
        for city in best_state:
            print(f"{allCities[city]}")
        print("BEST FITNESS: {}".format(best_fitness))

    def DISABLED_test_nov_trip(self):
        # GIVEN
        allCities = [self.nyc, self.vie, self.bud, self.bra, self.pra]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
#        assert_that(best_state[0], equal_to(2))
#        assert_that(best_state[1], equal_to(1))
#        assert_that(best_state[2], equal_to(0))
        #assert_that(1, equal_to(2))
        print("TSP Best State: {}".format(best_state))
        for city in best_state:
            print(f"{allCities[city]}")
        print("BEST FITNESS: {}".format(best_fitness))
        assert_that(2, equal_to(0))

