
from flask import (
    app,
    Flask,
    jsonify,
    request
)
from flask_cors import CORS
from flask.logging import default_handler

from OnTheRoad import (
    BestPath,
    flask_config,
    Location,
    TravelCost
)

import logging
from logging.config import dictConfig
import os
import sys

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
cors = CORS(app, resources={r"/": {"origins": ["http://localhost:3000", "johnstratoudakis.com"]}})


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
    app.logger.info("=" * LINE_LENGTH)
    if request.is_json:
        content = request.get_json()
#        app.logger.info(f"requiest_content: {content}")
        locations = content['locations']
        startingIndex = content['startingIndex']

        allCities = []
        for location in locations:
            loc_obj = Location.Location(location[0], location[0], location[1])
            app.logger.info(f' - Location: {location[0]},  Starting Point: {location[2]}')
            allCities.append(loc_obj)

        app.logger.info(f' - Starting Index: {startingIndex}')
        best_state, best_fitness = BestPath.calcTsp(allCities, startingIndex)

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
                "status": 200,
                "message": "Successfully calculated",
                "best_path": best_path
                }
    else:
        resp = {
                "status": 400,
                "message": "Request not in Json format"
                }
    app.logger.info(f"Sending: {resp}")
    app.logger.info(f"Sending: {jsonify(resp)}")
    return jsonify(resp)

@app.route('/slash', methods=['GET'])
def slash():
    return "Default text for uwsgi app"

if __name__ == "__main__":
    print("main.py::__main__")
    app.run(host='0.0.0.0', port=5000)
