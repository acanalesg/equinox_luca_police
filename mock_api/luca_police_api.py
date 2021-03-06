import logging
from flask import Flask
from flask import request
from car_positions import Fleet
from incidents import simulate_incident

app = Flask(__name__)

f = Fleet()
server_port = 5001


@app.route("/get_positions")
def get_positions():
    return f.get_car_positions()


@app.route("/push_incident")
def push_incident():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    logging.info("Received push_incident invoke: " + str((lat,lon)))
    return simulate_incident(lat, lon)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-6s| %(message)s')
    logging.info("Starting API")

    app.run(port=server_port)