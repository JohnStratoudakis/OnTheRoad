from OnTheRoad import BestPath, Location
from OnTheRoad.TravelCost import TravelCost

import logging
logger = logging.getLogger(__name__.split('.')[0])

import tests.unit.MockDistance

from unittest import mock, TestCase
from hamcrest import any_of, assert_that, equal_to

class BestPathTests(TestCase):
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

    # Other European Cities
    mun = Location.Location("Munich", "mun", "Munich, Germany")
    lju = Location.Location("Ljubljana", "lju", "ljubljana, Slovenia")

    def getIndex(self, shortName, allCities):
        for idx in range(len(allCities)):
            if shortName == allCities[idx].getShortName():
                return idx
        return -1

    def test_best_path_smoke(self):
        assert_that("Sugar is bad", equal_to("Sugar is bad"))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_generate_Distances_List(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]

        # WHEN
        dist_list = BestPath.genDistList(allCities)

        # THEN
        assert_that(len(dist_list), equal_to(3))

        # Amsterdam to Brussels
        assert_that(dist_list[0][0], equal_to(0))
        assert_that(dist_list[0][1], equal_to(1))
        assert_that(dist_list[0][2], equal_to(TravelCost.getDistanceBetween(self.ams, self.bru)[0]))

        # Amsterdam to London
        assert_that(dist_list[1][0], equal_to(0))
        assert_that(dist_list[1][1], equal_to(2))
        assert_that(dist_list[1][2], equal_to(TravelCost.getDistanceBetween(self.ams, self.lon)[0]))

        # Brussels to London
        assert_that(dist_list[2][0], equal_to(1))
        assert_that(dist_list[2][1], equal_to(2))
        assert_that(dist_list[2][2], equal_to(TravelCost.getDistanceBetween(self.bru, self.lon)[0]))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip_fitness(self):
        # GIVEN
        allCities = [self.ams, self.bru, self.lon]
        state = [0, 1, 2]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(TravelCost.getDistanceBetween(self.ams, self.bru)[0] +
                                      TravelCost.getDistanceBetween(self.bru, self.lon)[0] ))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_ams_bud_lon_bru(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [3, 1, 0, 2]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(TravelCost.getDistanceBetween(self.ams, self.bud)[0] +
                                      TravelCost.getDistanceBetween(self.bud, self.lon)[0] +
                                      TravelCost.getDistanceBetween(self.lon, self.bru)[0] ))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_lon_ams_bru_bud(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [0, 3, 2, 1]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(TravelCost.getDistanceBetween(self.lon, self.ams)[0] +
                                      TravelCost.getDistanceBetween(self.ams, self.bru)[0] +
                                      TravelCost.getDistanceBetween(self.bru, self.bud)[0] ))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_lon_bru_ams_bud(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]
        state = [0, 2, 3, 1]

        # WHEN
        fitness = BestPath.tsp_fitness(state, allCities)

        # THEN
        assert_that(fitness, equal_to(TravelCost.getDistanceBetween(self.lon, self.bru)[0] +
                                      TravelCost.getDistanceBetween(self.bru, self.ams)[0] +
                                      TravelCost.getDistanceBetween(self.ams, self.bud)[0] ))


    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip(self):
        # GIVEN
        allCities = [self.lon, self.bru, self.ams]

        # WHEN
        best_state, fitness = BestPath.calcTsp(allCities)

        # THEN
        # Technically there are multiple 'best paths' to take
        # London -> Brussels -> Amsterdam
        # Amsterdam -> Brussels -> London
        assert_that(best_state[0], any_of(0, 2))
        assert_that(best_state[1], equal_to(1))
        assert_that(best_state[2], any_of(0, 2))

        tot_distance_from_lon = TravelCost.getDistanceBetween(self.lon, self.bru)[0] + \
                                TravelCost.getDistanceBetween(self.bru, self.ams)[0]
        tot_distance_from_ams = TravelCost.getDistanceBetween(self.ams, self.bud)[0] + \
                                TravelCost.getDistanceBetween(self.lon, self.bru)[0]

        assert_that(fitness, any_of(tot_distance_from_lon, tot_distance_from_ams))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_may_trip_with_Budapest(self):
        # GIVEN
        allCities = [self.lon, self.bud, self.bru, self.ams]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        tot_lon_ams_bru_bud = TravelCost.getDistanceBetween(self.lon, self.ams)[0] + \
                              TravelCost.getDistanceBetween(self.ams, self.bru)[0] + \
                              TravelCost.getDistanceBetween(self.bru, self.bud)[0]
        assert_that(best_fitness, equal_to(tot_lon_ams_bru_bud))

        assert_that(best_state[0], equal_to(self.getIndex("lon", allCities)))
        assert_that(best_state[1], equal_to(self.getIndex("ams", allCities)))
        assert_that(best_state[2], equal_to(self.getIndex("bru", allCities)))
        assert_that(best_state[3], equal_to(self.getIndex("bud", allCities)))


    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_dec_trip(self):
        # GIVEN
        allCities = [self.vie, self.bud, self.bra, self.pra]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        tot_pra_bra_vie_bud = TravelCost.getDistanceBetween(self.pra, self.bra)[0] + \
                              TravelCost.getDistanceBetween(self.bra, self.vie)[0] + \
                              TravelCost.getDistanceBetween(self.vie, self.bud)[0]
        assert_that(best_fitness, equal_to(tot_pra_bra_vie_bud))

        assert_that(best_state[0], equal_to(self.getIndex("pra", allCities)))
        assert_that(best_state[1], equal_to(self.getIndex("bra", allCities)))
        assert_that(best_state[2], equal_to(self.getIndex("vie", allCities)))
        assert_that(best_state[3], equal_to(self.getIndex("bud", allCities)))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_dec_trip_2(self):
        # GIVEN
        allCities = [self.vie, self.bud, self.pra, self.bra]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)

        # THEN
        tot_pra_bra_vie_bud = TravelCost.getDistanceBetween(self.pra, self.bra)[0] + \
                              TravelCost.getDistanceBetween(self.bra, self.vie)[0] + \
                              TravelCost.getDistanceBetween(self.vie, self.bud)[0]
        assert_that(best_fitness, equal_to(tot_pra_bra_vie_bud))

        assert_that(best_state[0], equal_to(self.getIndex("pra", allCities)))
        assert_that(best_state[1], equal_to(self.getIndex("bra", allCities)))
        assert_that(best_state[2], equal_to(self.getIndex("vie", allCities)))
        assert_that(best_state[3], equal_to(self.getIndex("bud", allCities)))

    @mock.patch('OnTheRoad.TravelCost.TravelCost.getDistanceBetween', new=tests.unit.MockDistance.mock_getDistanceBetween)
    def test_south_central_europe(self):
        # GIVEN
        allCities = [self.mun, self.lju, self.vie, self.pra, self.bra, self.bud]

        # WHEN
        best_state, best_fitness = BestPath.calcTsp(allCities)
        BestPath.dumpBestPath(allCities, best_state, best_fitness)

        # THEN
        assert_that(best_state[0], equal_to(self.getIndex("pra", allCities)))
        assert_that(best_state[1], equal_to(self.getIndex("bud", allCities)))
        assert_that(best_state[2], equal_to(self.getIndex("bra", allCities)))
        assert_that(best_state[3], equal_to(self.getIndex("vie", allCities)))
        assert_that(best_state[4], equal_to(self.getIndex("lju", allCities)))
        assert_that(best_state[5], equal_to(self.getIndex("mun", allCities)))