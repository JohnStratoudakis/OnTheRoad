from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/version', methods=['GET'])
    def get_version():
        print("get_version() called")
        version = "0.0.1"
        print(f"Returning version: {version}")

        response_raw_text = f"OnTheRoad WSGI Version: {version}\n"

        return response_raw_text

    return app