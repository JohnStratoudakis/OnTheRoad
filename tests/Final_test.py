import unittest
from hamcrest import *

class FinalTests(unittest.TestCase):

    def test_smoke(self):
        # GIVEN
        # WHEN
        # THEN
        assert_that("J", equal_to("J"))

