from flask import Flask
from flask import request
from flask.logging import default_handler
from flask_cors import CORS

from flask import jsonify

import logging
import os

from OnTheRoad import BestPath, Location, TravelCost

LINE_LENGTH = 80

logger = logging.getLogger(__name__.split('.')[0])
logger.addHandler(default_handler)

app = Flask(__name__)
CORS(app)

def set_up_logging(verbose):
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    logger.info("INFO")
    logger.debug("DEBUG")

@app.route('/version', methods=['GET'])
def get_version():
    print("get_version() called")
    version = "0.0.1"
    print(f"Returning version: {version}")
    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"
    return response_raw_text

@app.route('/onTheRoad', methods=['POST'])
def post():
    print("-" * LINE_LENGTH)
#    logger.info("=" * LINE_LENGTH)
    API_KEY = os.environ['GOOG_API_KEY']
#    logger.error("=" * LINE_LENGTH)
    if request.is_json:
#        API_KEY = os.environ['GOOG_API_KEY']
#        print("JOHN_API_KEY: {}".format(API_KEY))
        content = request.get_json()
        # TODO: Use python logger with appropriate log leves
        #print(f"Content: {content}")
        locations = content['locations']
        #print(f"Locations: {locations}")

        allCities = []
        for location in locations:
            loc_obj = Location.Location(location[0], location[0], location[1])
            logger.info("Location: {}".format(location[0]))
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

if __name__ == "__main__":
    print("flaskapp.py::__main__")
    app.run(host='0.0.0.0', port=5000)
