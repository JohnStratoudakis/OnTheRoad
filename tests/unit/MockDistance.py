
from OnTheRoad import BestPath, Location, TravelCost


def mock_getDistanceBetween(city_1, city_2):
    allCosts = {
                'ams': {
                    'bra': [ 1_205_785,     41_742],
                    'bru': [   205_810,      6_960],
                    'bud': [ 1_395_722,     48_614],
                    'london': [   587_177,     17_880],
                    'lju': [ 1_232_829,     43_534],
                    'mun': [   824_754,     29_342],
                    'pra': [   879_316,     30_932],
                    'vie': [ 1_146_993,     40_838],
                },
                'bra': {
                    'ams': [ 1_236_089,     61_416],
                    'bru': [ 1_617_508,     69_756],
                    'bud': [   202_343,     11_640],
                    'london': [ 1_990_726,     79_296],
                    'lju': [   545_015,     27_996],
                    'mun': [   536_714,     20_136],
                    'pra': [   339_324,     14_220],
                    'vie': [    65_067,      3_960],
                },
                'bru': {
                    'ams': [   213_999,      7_320],
                    'bra': [ 1_233_963,     45_360],
                    'bud': [ 1_539_118,     68_700],
                    'london': [   377_011,     10_380],
                    'lju': [ 1_188_909,     48_688],
                    'mun': [   824_534,     24_780],
                    'pra': [   894_112,     51_060],
                    'vie': [ 1_283_984,     58_800],
                },
                'bud': {
                    'ams': [ 1_403_823,     63_480],
                    'bra': [   199_315,      8_580],
                    'bru': [ 1_576_729,     72_900],
                    'london': [ 1_798_742,     73_020],
                    'lju': [   639_544,     30_480],
                    'mun': [   715_951,     24_720],
                    'pra': [   538_617,     23_220],
                    'vie': [   257_024,      9_480],
                },
                'london': {
                    'ams': [   612_215,     18_960],
                    'bra': [ 1_980_636,     70_499],
                    'bru': [   376_976,      8_640],
                    'bud': [ 2_158_014,     74_880],
                    'lju': [ 1_766_849,     54_868],
                    'mun': [ 1_443_568,     32_160],
                    'pra': [ 1_267_330,     62_580],
                    'vie': [ 1_902_880,     64_980],
                },
                'lju': {
                    'ams': [ 1_232_631,     43_118],
                    'bra': [   354_073,     27_960],
                    'bru': [ 1_031_310,     58_468],
                    'bud': [   644_900,     51_120],
                    'london': [ 1_404_499,     70_048],
                    'mun': [   429_461,     22_500],
                    'pra': [   650_012,     43_860],
                    'vie': [   322_402,     23_160],
                },
                'mun': {
                    'ams': [   824_560,     29_026],
                    'bra': [   521_264,     20_100],
                    'bru': [   824_489,     24_840],
                    'bud': [   650_978,     23_539],
                    'london': [ 1_158_569,     58_140],
                    'lju': [   435_309,     23_100],
                    'pra': [   504_104,     28_440],
                    'vie': [   402_249,     15_763],
                },
                'pra': {
                    'ams': [ 1_076_876,     55_620],
                    'bra': [   339_324,     14_400],
                    'bru': [ 1_232_654,     63_960],
                    'bud': [   538_617,     23_400],
                    'london': [ 1_605_872,     73_500],
                    'lju': [   828_925,     47_728],
                    'mun': [   861_546,     32_280],
                    'vie': [   402_558,     14_700],
                },
                'vie': {
                    'ams': [ 1_146_959,     40_490],
                    'bra': [    76_132,      4_859],
                    'bru': [ 1_539_752,     64_080],
                    'bud': [   257_024,      9_540],
                    'london': [ 1_788_897,     75_600],
                    'lju': [   346_375,     23_880],
                    'mun': [   402_198,     15_587],
                    'pra': [   402_558,     14_580],
                },

               }
    shortA = city_1.getShortName()
    shortB = city_2.getShortName()
    if shortA in allCosts and shortB in allCosts[shortA]:
        return allCosts[city_1.getShortName()][city_2.getShortName()]
    elif shortB in allCosts and shortA in allCosts[shortB]:
        return allCosts[city_2.getShortName()][city_1.getShortName()]
