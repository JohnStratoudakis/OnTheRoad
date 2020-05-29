
from flask import Flask
from flask_cors import CORS

from OnTheRoad import flask_config

app = Flask(__name__)
CORS(app)

@app.route('/version', methods=['GET'])
#@crossdomain(origin='johnstratoudakis.com')
def get_version():
    version = flask_config.version
    print(f"Returning version: {version}")

    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

    return response_raw_text

@app.route('/slash', methods=['GET'])
def slash():
    return "Default text for uwsgi app"

if __name__ == "__main__":
    print("main.py::__main__")
    app.run(host='0.0.0.0', port=5000)
