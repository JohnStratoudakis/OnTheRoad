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
                    'bra': [199311, 6780],
                    'pra': [538613, 6780],
                    'vie': [219301, 6780]
                    },
                'bra': {
                    'bud': [199311, 6780],
                    'pra': [357049, 6780],
                    'vie': [587306, 6780],
                    },
                'pra': {
                    'bud': [538613, 6780],
                    'bra': [357049, 6780],
                    'vie': [587306, 6780],
                    },
                'vie': {
                    'bra': [62070, 6780],
                    'bud': [219301, 6780],
                    'pra': [402558, 6780],
                    }
                }
    shortA = city_1.getShortName()
    shortB = city_2.getShortName()
    if shortA in allCosts and shortB in allCosts[shortA]:
        return allCosts[city_1.getShortName()][city_2.getShortName()]
    elif shortB in allCosts and shortA in allCosts[shortB]:
        return allCosts[city_2.getShortName()][city_1.getShortName()]

