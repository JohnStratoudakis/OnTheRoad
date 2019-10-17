#!/usr/bin/python3.7

from flask import Flask
from flask import request

from flask import jsonify

from OnTheRoad import BestPath, Location, TravelCost

app = Flask(__name__)

@app.route('/onTheRoad', methods=['POST'])
def post():
    print("----------------------------------------")
    if request.is_json:
        content = request.get_json()
        # TODO: Use python logger with appropriate log leves
        #print(f"Content: {content}")
        locations = content['locations']
        #print(f"Locations: {locations}")

        allCities = []
        for location in locations:
            loc_obj = Location.Location(location[0], location[0], location[1])
            allCities.append(loc_obj)

        best_state, best_fitness = BestPath.calcTsp(allCities)
        #best_state = [1, 0, 2]
        best_path = []
        for state in best_state:
            loc_obj = Location.Location(allCities[state].getName(),
                                        allCities[state].getName(),
                                        allCities[state].getAddress())
            # TODO: Figure out how to serialize Location object
            #       to send back a better response
            #best_path.append(loc_obj)
            best_path.append([loc_obj.getName(), loc_obj.getAddress()])

        resp = {
                "status":200,
                "message":"Successfully calculated",
                "best_path": best_path
                }
    else:
        resp = {
                "status":400,
                "message":"Request not in Json format"
                }
    return jsonify(resp)

app.run(host='0.0.0.0', port=5000)
