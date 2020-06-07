
from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler
#from flask_cors import cross_origin
#from flask_cors import crossdomain

import logging
import sys
from OnTheRoad import flask_config

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
