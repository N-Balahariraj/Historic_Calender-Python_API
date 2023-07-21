from flask import Flask, jsonify, request, send_from_directory

import requests

app = Flask(__name__)


@app.route("/get_data/<int:day>/<int:mon>", methods=["GET"])
def generate_data(day, mon):
    api_url = "https://api.api-ninjas.com/v1/historicalevents?month={}&day={}".format(
        mon, day
    )
    data = requests.get(
        api_url, headers={"X-Api-Key": "UbVZej3yrHJV+ecO+rxMsQ==oo0aKI49HPbUciVP"}
    )
    return data.text


@app.route("/")
def get_data():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    app.run()
