from OnTheRoad import BestPath, Location, TravelCost

def mock_getDistanceBetween(city_1, city_2):
    allCosts = {
                'ams': {
                    'bru': [ 212132, 6780],
                    'bud': [1395715, 6780],
                    'lon': [ 587306, 6780]
                    },
                'bru': {
                    'ams': [ 212132, 6780],
                    'bud': [1353099, 6780],
                    'lon': [ 375174, 6780]
                    },
                'lon': {
                    'ams': [ 587306, 6780],
                    'bru': [ 375174, 6780],
                    'bud': [1843672, 6780]
                    },
                'bud': {
                    'bra': [283_610, 6780],
                    'pra': [448_830, 6780],
                    'vie': [220_082, 6780]
                    },
                'bra': {
                    'bud': [282_403, 6780],
                    'pra': [654_202, 6780],
                    'vie': [65_067, 6780],
                    },
                'pra': {
                    'bud': [450_682, 6780],
                    'bra': [352_319, 6780],
                    'vie': [298_032, 6780],
                    },
                'vie': {
                    'bra': [75_939, 6780],
                    'bud': [215_605, 6780],
                    'pra': [255_700, 6780],
                    }
                }
    shortA = city_1.getShortName()
    shortB = city_2.getShortName()
    if shortA in allCosts and shortB in allCosts[shortA]:
        return allCosts[city_1.getShortName()][city_2.getShortName()]
    elif shortB in allCosts and shortA in allCosts[shortB]:
        return allCosts[city_2.getShortName()][city_1.getShortName()]


#def dump_distance_matrix(allCities):
#    for i in range(len(allCities)):
#        if i == 0:
#            c_header = f"\n{'+':>20}"
#            for c in range(len(allCities)):
#                jo = str(allCities[c])
#                print(f"{jo:>20}")
#                c_header += f'{jo:>20}'
#            print(f"{c_header}")
#        line = f'{str(allCities[i]):>20}'
#        for j in range(len(allCities)):
#            shortA = allCities[i]
#            shortB = allCities[j]
#            if shortA == shortB:
#                cost = "-"
#            else:
#                cost = TravelCost.TravelCost.getDistanceBetween(shortA, shortB) [0]
#                if int(cost):
#                    cost = f"{int(cost):,d}"
#            line += f"{cost:>20}"
#        print(f"{line}")