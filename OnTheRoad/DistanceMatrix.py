
from OnTheRoad import BestPath
from OnTheRoad import Location
from OnTheRoad import TravelCost

import logging

logger = logging.getLogger(__name__.split('.')[0])

file_template = """
from OnTheRoad import BestPath, Location, TravelCost
    allCosts = {{
{}
               }}
    shortA = city_1.getShortName()
    shortB = city_2.getShortName()
    if shortA in allCosts and shortB in allCosts[shortA]:
        return allCosts[city_1.getShortName()][city_2.getShortName()]
    elif shortB in allCosts and shortA in allCosts[shortB]:
        return allCosts[city_2.getShortName()][city_1.getShortName()]
"""

def dump_python_matrix(allCities):

    for left_city in allCities:
        for right_city in allCities:
            print(f"{left_city} -> {right_city}")
#                'ams': {
#                    'bru': [ 212132, 6780],
#                    'bud': [1395715, 6780],
#                    'lon': [ 587306, 6780]
#                    },

    file_body = "DDDD"
    file_contents = file_template.format(file_body)

    print("Save the following to a file:")
    print(f"{file_contents}")

def dump_ascii_matrix(allCities):
    for i in range(len(allCities)):
        if i == 0:
            c_header = f"\n{'+':>15}"
            for c in range(len(allCities)):
                jo = str(allCities[c])
                #print(f"{jo:>20}")
                c_header += f'{jo:>15}'
            print(f"{c_header}")
        line = f'{str(allCities[i]):>15}'
        for j in range(len(allCities)):
            shortA = allCities[i]
            shortB = allCities[j]
            if shortA == shortB:
                cost = "-"
            else:
                cost = TravelCost.TravelCost.getDistanceBetween(shortA, shortB) [0]
                if int(cost):
                    cost = f"{int(cost):,d}"
            line += f"{cost:>15}"
        print(f"{line}")