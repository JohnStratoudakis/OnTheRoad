
from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler
#from flask_cors import cross_origin
#from flask_cors import crossdomain

import logging
import sys
from OnTheRoad import flask_config

logger = logging.getLogger(__name__.split('.')[0])
logger.addHandler(default_handler)
logger.addHandler(logging.StreamHandler(sys.stdout))

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "johnstratoudakis.com"}})
#CORS(app)

#def set_up_logging(verbose):
#    if verbose:
#        logger.setLevel(logging.DEBUG)
#    else:
#        logger.setLevel(logging.INFO)
#    formatter = logging.Formatter('%(asctime)s - %(message)s')
#    logger.info("INFO")
#    logger.debug("DEBUG")

#set_up_logging(false)

#cors = CORS(app, resources={r"/slash": {"origins": "*"}})
#import flask_cors
#@crossdomain(origin='*')
#@flask_cors.cross_origin()
@app.route('/version', methods=['GET'])
def get_version():
    version = flask_config.version

    print(f'[PRINT_2] get_version called, version: {version}')
    app.logger.info(f'[INFO_2] get_version called, version: {version}')
    app.logger.debug(f'[DEBUG_2] get_version called, version: {version}')
    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

    return response_raw_text

@app.route('/locations', methods=['POST'])
def locations():
    #version = flask_config.version
    version="1.0.1"
    print(f"Returning version: {version}")

    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

    return response_raw_text

@app.route('/slash', methods=['GET'])
def slash():
    return "Default text for uwsgi app"

if __name__ == "__main__":
    print("main.py::__main__")
    app.run(host='0.0.0.0', port=5000)
