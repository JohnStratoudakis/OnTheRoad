#!/usr/bin/python3.7

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/onTheRoad', methods=['POST'])
def post():
    print("----------------------------------------")
    if request.is_json:
        content = request.get_json()
        print(f"Content: {content}")
        locations = content['locations']
        print(f"Locations: {locations}")

    return 'JSON posted'

app.run(host='0.0.0.0', port=5000)
