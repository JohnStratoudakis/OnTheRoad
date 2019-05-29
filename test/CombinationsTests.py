from Travel import Combinations, TravelCost, Location

import unittest
from hamcrest import *

#def dumpPath( path ):
#    print("Dumping path")

class CombinationsTests(unittest.TestCase):

    def test_1_guest(self):
        global verbose
        verbose = False
        print("")

        # GIVEN
        guests = [ "A" ]

        # WHEN
        allPaths = Combinations.Combinations.calc( guests )

        # THEN
        expPaths = [ ]
        expPaths.append(   [ ("A",) ]   )
        self.assertEqual( expPaths, allPaths )

    def test_2_guests(self):
        global verbose
        verbose = False
        print("")

        # GIVEN
        guests = [ "A", "B" ]

        # WHEN
        allPaths = Combinations.Combinations.calc( guests )

        # THEN
        expPaths = [ ]
        expPaths.append([  ("A", ), ("B", )   ])
        expPaths.append([  ("B", ), ("A", )   ])
        expPaths.append([  ( "A",  "B")       ])
        expPaths.append([  ( "B",  "A")       ])
        self.assertEqual( expPaths, allPaths )

    def test_3_guests(self):
        global verbose
        verbose = False
        print("")

        # GIVEN
        guests = [ "A", "B", "C" ]

        # WHEN
        allPaths = Combinations.Combinations.calc( guests )

        # THEN
        expPaths = [ ]
        # A picks 0
        expPaths.append([ ("A", ), ("B", ), ("C", ) ])
        expPaths.append([ ("A", ), ("C", ), ("B", ) ])
        expPaths.append([ ("A", ), ( "B",  "C") ])
        expPaths.append([ ("A", ), ( "C",  "B") ])
        # A picks 1
        expPaths.append([ ("A", "B"), ("C", ) ])
        expPaths.append([ ("A", "C"), ("B", ) ])
        # A picks 2
        expPaths.append([ ("A", "B", "C") ])
        expPaths.append([ ("A", "C", "B") ])
        # B picks 0
        expPaths.append([ ("B", ), ("A", ), ("C", ) ])
        expPaths.append([ ("B", ), ("C", ), ("A", ) ])
        expPaths.append([ ("B", ), ( "A",  "C") ])
        expPaths.append([ ("B", ), ( "C",  "A") ])
        # B picks 1
        expPaths.append([ ("B", "A"), ("C", ) ])
        expPaths.append([ ("B", "C"), ("A", ) ])
        # B picks 2
        expPaths.append([ ("B", "A", "C") ])
        expPaths.append([ ("B", "C", "A") ])
        # C picks 0
        expPaths.append([ ("C", ), ("B", ), ("A", ) ])
        expPaths.append([ ("C", ), ("A", ), ("B", ) ])
        expPaths.append([ ("C", ), ( "B",  "A") ])
        expPaths.append([ ("C", ), ( "A",  "B") ])
        # C picks 1
        expPaths.append([ ("C", "B"), ("A", ) ])
        expPaths.append([ ("C", "A"), ("B", ) ])
        # C picks 2
        expPaths.append([ ("C", "B", "A") ])
        expPaths.append([ ("C", "A", "B") ])

        # WHEN
        self.assertEqual( len(allPaths), len(expPaths) )
        for expPath in expPaths:
            self.assertTrue( expPath in allPaths )

    def test_4_guests(self):
        global verbose
        verbose = False

        # GIVEN
        guests = [ "A", "B", "C", "D" ]

        # WHEN
        allPaths = Combinations.Combinations.calc( guests )

        # THEN
        expPaths = [ ]
        # A picks 0
        expPaths.append([ ("A", ), ("B", ), ("C", ), ("D", ) ])
        # A picks 0, B picks 0
        expPaths.append([ ("A", ), ("B", ), ("C", "D") ])
        expPaths.append([ ("A", ), ("B", ), ("D", "C") ])
        # A picks 0, B picks 1
        expPaths.append([ ("A", ), ("B", "C"), ("D", ) ])
        expPaths.append([ ("A", ), ("B", "D"), ("C", ) ])
        # A picks 0, B picks 2
        expPaths.append([ ("A", ), ("B", "C", "D", ) ])
        expPaths.append([ ("A", ), ("B", "D", "C", ) ])

        for expPath in expPaths:
            self.assertTrue( expPath in allPaths )

    def test_1_city(self):
        # GIVEN
        ams = "Amsterdam"

        # WHEN
        allPaths = Combinations.Combinations.calcSinglePath( [ ams ] )

        # THEN
        assert_that(len(allPaths), equal_to(1))
        # Only one city in path - Amsterdam
        assert_that(allPaths[0], equal_to(ams))

    def test_2_cities(self):
        # GIVEN
        ams = "Amsterdam"
        bru = "Brussels"

        # WHEN
        allPaths = Combinations.Combinations.calcSinglePath( [ ams, bru ] )

        # THEN
        assert_that(len(allPaths), equal_to(2))
        # Order is important
        assert_that(allPaths[0], equal_to(ams))
        assert_that(allPaths[1], equal_to(bru))

    def test_3_cities(self):
        # GIVEN
        ams = "Amsterdam"
        bru = "Brussels"
        lon = "London"

        # WHEN
        allPaths = Combinations.Combinations.calcSinglePath( [ ams, bru, lon ] )

        # THEN
        assert_that(len(allPaths), equal_to(3))
        # Order is important
        assert_that(allPaths[0], equal_to(ams))
        assert_that(allPaths[1], equal_to(bru))
        assert_that(allPaths[2], equal_to(lon))


if __name__ == '__main__':
    unittest.main()
