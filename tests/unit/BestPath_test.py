from OnTheRoad import BestPath, Location, TravelCost

import tests.unit.MockDistance

import unittest
from unittest import mock
from hamcrest import *

class BestPathTest(unittest.TestCase):
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

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_generate_Distances_List(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]

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

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip_fitness(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]
        state = [0, 1, 2]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(587306))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_ams_bud_lon_bru(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [3, 1, 0, 2]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(3614561))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_lon_ams_bru_bud(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [0, 3, 2, 1]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(3408903))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_lon_bru_ams_bud(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [0, 2, 3, 1]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(1983021))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_lon_ams_bru_bud(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [0, 3, 2, 1]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(2152537))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip(self):
        # GIVEN
        allCities = [self.lon, self.bru, self.ams]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        assert_that(best_fitness, equal_to(587306))

        assert_that(best_state[0], equal_to(2))
        assert_that(best_state[1], equal_to(1))
        assert_that(best_state[2], equal_to(0))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip_with_Budapest(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        assert_that(best_fitness, equal_to(1983021))

        assert_that(best_state[0], equal_to(1))
        assert_that(best_state[1], equal_to(3))
        assert_that(best_state[2], equal_to(2))
        assert_that(best_state[3], equal_to(0))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_nov_trip(self):
        # GIVEN
        allCities = [self.vie, self.bud, self.bra, self.pra]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        assert_that(best_fitness, equal_to(638420))
        # TODO: remove these lines
#        for s in best_state:
#            print(f"{allCities[s]}")

        assert_that(best_state[0], equal_to(1))
        assert_that(best_state[1], equal_to(0))
        assert_that(best_state[2], equal_to(2))
        assert_that(best_state[3], equal_to(3))