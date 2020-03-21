
from OnTheRoad import BestPath
from OnTheRoad import Location
from OnTheRoad.TravelCost import TravelCost

import logging

logger = logging.getLogger(__name__.split('.')[0])

file_template = """
from OnTheRoad import BestPath, Location, TravelCost


def mock_getDistanceBetween(city_1, city_2):
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

def dump_python_matrix(allCities, output_file):
    file_body = ""
    for left_city in allCities:
        file_body += f"                '{left_city}': {{\n"
        for right_city in allCities:
            if left_city != right_city:
                [dist_meters, time_sec] = TravelCost.getDistanceBetween(left_city, right_city) 
                if dist_meters != TravelCost.MAX_VAL and time_sec != TravelCost.MAX_VAL:
                    file_body += f"                    '{right_city}': [{dist_meters:10_}, {time_sec:10_}],\n"
        file_body += "                },\n"

    file_contents = file_template.format(file_body)

    if output_file:
        logger.info(f"Saving to Python file: {output_file}")
        with open(output_file, "w") as fout:
            fout.write(file_contents)

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
                cost = TravelCost.getDistanceBetween(shortA, shortB) [0]
                if int(cost):
                    cost = f"{int(cost):,d}"
            line += f"{cost:>15}"
        print(f"{line}")