from Travel import Combinations, TravelCost, Location

import unittest

def dumpPath( path ):
    print("Dumping path")

class TestCombinations(unittest.TestCase):

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
        allPaths = Travel.Combinations.calc( guests )

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
        allPaths = Travel.Combinations.calc( guests )

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
        self.assertEqual( len(actPaths), len(expPaths) )
        for expPath in expPaths:
            self.assertTrue( expPath in actPaths )

    def test_4_guests(self):
        global verbose
        verbose = False

        # GIVEN
        guests = [ "A", "B", "C", "D" ]

        # WHEN
        allPaths = Travel.Combinations.calc( guests )

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
            self.assertTrue( expPath in actPaths )

    def test_remove_duplicates(self):
        pass

if __name__ == '__main__':
    unittest.main()
