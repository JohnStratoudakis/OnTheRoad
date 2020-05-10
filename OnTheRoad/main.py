from flask import Flask

app = Flask(__name__)


@app.route('/version', methods=['GET'])
def get_version():
    print("get_version() called")
    version = "0.0.10"
    print(f"Returning version: {version}")

    response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

    return response_raw_text

@app.route('/slash', methods=['GET'])
def slash():
    return "Default text for uwsgi app"

if __name__ == "__main__":
    print("main.py::__main__")
    app.run(host='0.0.0.0', port=5000)
