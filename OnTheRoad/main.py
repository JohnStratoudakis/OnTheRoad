
from flask import Flask
from flask_cors import CORS
#from flask_cors import cross_origin
#from flask_cors import crossdomain

#from OnTheRoad import flask_config

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "johnstratoudakis.com"}})
#CORS(app)

#cors = CORS(app, resources={r"/slash": {"origins": "*"}})
#import flask_cors
@app.route('/version', methods=['GET'])
#@crossdomain(origin='*')
#@flask_cors.cross_origin()
def get_version():
    #version = flask_config.version
    version="1.0.1"
    print(f"Returning version: {version}")

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
