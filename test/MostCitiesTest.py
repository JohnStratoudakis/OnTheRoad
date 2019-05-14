
#from Travel import TravelCost, Location

import unittest

class MostCitiesTests(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual("Carnivore Diet", "Carnivore Diet")

    def test_3_cities(self):
        # given
        ams = Location.Location("amsterdam", "amsterdam, netherlands")
        brussels = Location.Location("brussels", "brussels, belgium")
        london = Location.Location("london", "london, united kingdom")

        # when
        #[distance_meters, duration_seconds] = TravelCost.TravelCost(ams, brussels).cost()

        # then
        #self.assertEqual(distance_meters, 202828)
        #self.assertEqual(duration_seconds, 8372)

