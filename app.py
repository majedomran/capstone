import os
from flask import Flask, jsonify, request, abort, render_template
from models import Flight, SpaceShip, setup_db, Astronaut, Station
from flask_cors import CORS
import json
from auth import requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_instuctions():
        # excited = os.environ['EXCITED']
        # greeting = "Hello"
        # if excited == 'true': greeting = greeting + "!!!!!"
        return render_template('index.html')
    # Flight

    @app.route('/auth', methods=['POST'])
    @requires_auth('get:drinks-detail')
    def req_auth(jwt):
        return jsonify({"success": True})

    @app.route('/Flight')
    @requires_auth('get:all')
    def get_flights():
        return paginate_flights()

    @app.route('/Flight/<id>', methods=['GET'])
    @requires_auth('get:one')
    def get_flight_id(id):
        error = False
        try:
            flight = Flight.query.get(id)
            if not flight:
                error = True
        except BaseException:
            print('aborted')
            abort(404)
        if error:
            abort(404)
        return jsonify({'success': 'True', 'Flight': flight.format()})

    @app.route('/Flight', methods=['POST'])
    @requires_auth('post:one')
    def add_Flight():
        try:
            data = json.loads(request.data)
            flight = Flight(
                SpaceShip=data['spaceship'],
                Station=data['station'],
                LaunchingPad=data['launchingpad'],
                LaunchingDate=data['launchingdate'])
            Flight.insert(flight)
        except BaseException:
            print('aborted')
            abort(422)
        return paginate_flights()

    @app.route('/Flight/<id>', methods=['DELETE'])
    @requires_auth('delete:one')
    def delete_flight(id):
        print('delete flight')
        try:
            flight = Flight.query.get(id)
            Flight.delete(flight)
        except BaseException:
            print("aborted")
            abort(404)
        finally:
            return jsonify({'Deleted flight': id, 'success': True})
    # Vehicle

    @app.route('/Spaceship')
    @requires_auth('get:all')
    def get_vehicles():
        return paginate_SpaceShip()

    @app.route('/Spaceship/<id>', methods=['GET'])
    @requires_auth('get:one')
    def get_vehicle_id(id):
        try:
            Spaceship = SpaceShip.query.get(id)
            if not Spaceship:
                abort(404)
        except BaseException:
            abort(404)
        return jsonify({'success': 'True', 'SpaceShip': Spaceship.format()})

    @app.route('/Spaceship', methods=['POST'])
    @requires_auth('post:one')
    def add_vehicle():
        try:
            data = json.loads(request.data)
            print(data['reuseable'])
            reuseable = False
            if(data['reuseable'] == 'True'):
                reuseable = True
            Spaceship = SpaceShip(
                name=data['name'],
                model=data['model'],
                reuseable=reuseable,
                capacity=data['capacity'])
            SpaceShip.insert(Spaceship)
        except BaseException:
            abort(403)
        return paginate_SpaceShip()

    @app.route('/Spaceship/<id>', methods=['DELETE'])
    @requires_auth('delete:one')
    def delete_vehicle(id):
        try:
            Spaceship = SpaceShip.query.get(id)
            SpaceShip.delete(Spaceship)
        except BaseException:
            abort(404)
        return jsonify({'Deleted Spaceship': id, 'success': True})
    # Astronaut

    @app.route('/Astronaut')
    @requires_auth('get:all')
    def get_Astronaut():
        return paginate_Astronaut()

    @app.route('/Astronaut/<id>', methods=['GET'])
    @requires_auth('get:one')
    def get_Astronaut_id(id):
        try:
            astronaut = Astronaut.query.get(id)
            if not astronaut:
                abort(404)
        except BaseException:
            abort(404)
        return jsonify({'success': 'True', 'Astronaut': astronaut.format()})

    @app.route('/Astronaut', methods=['POST'])
    @requires_auth('post:one')
    def add_Astronaut():
        try:
            data = json.loads(request.data)
            print(data)
            astronaut = Astronaut(
                name=data['name'],
                Job=data['job'],
                Flight=data['flight'])
            Astronaut.insert(astronaut)
        except BaseException:
            abort(403)
        return paginate_Astronaut()

    @app.route('/Astronaut/<id>', methods=['DELETE'])
    @requires_auth('delete:one')
    def delete_Astronaut(id):
        try:
            astronaut = Astronaut.query.get(id)
            Astronaut.delete(astronaut)
        except BaseException:
            abort(404)
        return jsonify({'Deleted Astronaut': id, 'success': True})
    # station

    @app.route('/Station')
    @requires_auth('get:all')
    def get_Station():
        return paginate_Station()

    @app.route('/Station/<id>', methods=['GET'])
    @requires_auth('get:one')
    def get_Station_id(id):
        try:
            station = Station.query.get(id)
            if not station:
                abort(404)
        except BaseException:
            abort(404)
        return jsonify({'success': 'True', 'station': station.format()})

    @app.route('/Station', methods=['POST'])
    @requires_auth('post:one')
    def add_Station():
        try:
            data = json.loads(request.data)
            print(data)
            station = Station(
                CrewCapacity=data['crewcapacity'],
                FuelCapacity=data['fuelcapacity'])
            Station.insert(station)
        except BaseException:
            abort(403)
        return paginate_Station()

    @app.route('/Station/<id>', methods=['DELETE'])
    @requires_auth('delete:one')
    def delete_Stationt(id):
        try:
            station = Station.query.get(id)
            Station.delete(station)
        except BaseException:
            abort(404)
        return jsonify({'Deleted Astronaut': id, 'success': True})

    def paginate_flights():
        flights_paginated = []
        flights = Flight.query.all()
        for flight in flights:
            flights_paginated.append(flight.format())
        return jsonify({'success': True, 'Flights': flights_paginated})

    def paginate_SpaceShip():
        vehicles_paginated = []
        vehicles = SpaceShip.query.all()
        for vehicle in vehicles:
            vehicles_paginated.append(vehicle.format())
        return jsonify({'success': True, 'SpaceShips': vehicles_paginated})

    def paginate_Astronaut():
        astronauts_paginated = []
        astronauts = Astronaut.query.all()
        for astronaut in astronauts:
            astronauts_paginated.append(astronaut.format())
        return jsonify({'success': True, 'Astronauts': astronauts_paginated})

    def paginate_Station():
        station_paginated = []
        stations = Station.query.all()
        for station in stations:
            station_paginated.append(station.format())
        return jsonify({'success': True, 'Stations': station_paginated})

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
