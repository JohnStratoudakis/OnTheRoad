
from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler
#from flask_cors import cross_origin
#from flask_cors import crossdomain
from flask import jsonify

import logging
import os
import sys
from OnTheRoad import flask_config
from OnTheRoad import BestPath, Location, TravelCost

from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

LINE_LENGTH = 80

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "johnstratoudakis.com"}})


@app.route('/version', methods=['GET'])
def get_version():
    version = flask_config.version

    print(f'[PRINT_3] get_version called, version: {version}')
    app.logger.info(f'[INFO_3] get_version called, version: {version}')
    app.logger.debug(f'[DEBUG_3] get_version called, version: {version}')
    app.logger.debug(f'[DEBUG_3] get_version called, version: {version}')
    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

    return response_raw_text

@app.route('/', methods=['POST'])
def default_path():
    print("-" * LINE_LENGTH)
    app.logger.info("=" * LINE_LENGTH)
    API_KEY = os.environ['GOOG_API_KEY']
    app.logger.error(f"API_KEY: {API_KEY}"")
    app.logger.error("=" * LINE_LENGTH)
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
            app.logger.info("Location: {}".format(location[0]))
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
#    #version = flask_config.version
#    version="1.0.1"
#    print(f"Returning version: {version}")
#
#    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"
#
#    return response_raw_text

@app.route('/slash', methods=['GET'])
def slash():
    return "Default text for uwsgi app"

if __name__ == "__main__":
    print("main.py::__main__")
    app.run(host='0.0.0.0', port=5000)
