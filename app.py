import os
from flask import Flask, jsonify, request, abort, render_template
from models import Flight, SpaceShip, setup_db, Astronaut, Station, db
from flask_cors import CORS
import json
from auth import requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app,False)
    CORS(app)
    # a simple HTML description
    @app.route('/')
    def get_instuctions():
        
        return render_template('index.html')
# Flight
    
    # get all flights
    @app.route('/Flight')
    @requires_auth('get:all')
    def get_flights():
        return paginate_flights()
    # get a specific flight
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
    # add a new flight
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
    # edit a Flight
    @app.route('/Flight/<id>', methods=['PATCH'])
    @requires_auth('patch:one')
    def patch_flight_id(id):
        try:
            data = json.loads(request.data)
            flight = Flight.query.get(id)
            if 'Station' in data.keys():
                flight.Station = data['Station']
            if 'SpaceShip' in data.keys():
                flight.SpaceShip = data['SpaceShip']
            if 'LaunchingPad' in data.keys():
                flight.LaunchingPad = data['LaunchingPad']
            if 'LaunchingDate' in data.keys():
                flight.LaunchingDate = data['LaunchingDate']
            db.session.commit()
        except:
            abort(400)
        finally:
            return paginate_flights()
    # delete a flight
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
    # get all SpacShips
    @app.route('/Spaceship')
    @requires_auth('get:all')
    def get_vehicles():
        return paginate_SpaceShip()
    # get a specific SpaceShip
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
    # add a new SpaceShip
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
    # edit a Flight
    @app.route('/Spaceship/<id>', methods=['PATCH'])
    @requires_auth('patch:one')
    def patch_Spaceship(id):
        try:
            data = json.loads(request.data)
            Spaceship = SpaceShip.query.get(id)
            if 'name' in data.keys():
                Spaceship.name = data['name']
            if 'model' in data.keys():
                Spaceship.model = data['model']
            if 'reuseable' in data.keys():
                Spaceship.reuseable = data['reuseable']
            if 'capacity' in data.keys():
                 Spaceship.capacity = data['capacity']
            db.session.commit()
        except:
            abort(400)
        finally:
            return paginate_SpaceShip()
    # delete a SpaceShip
    @app.route('/Spaceship/<id>', methods=['DELETE'])
    @requires_auth('delete:one')
    def delete_vehicle(id):
        # try:
        Spaceship = SpaceShip.query.get(id)
        SpaceShip.delete(Spaceship)
        # except BaseException:
            # abort(404)
        return jsonify({'Deleted Spaceship': id, 'success': True})
    # Astronaut
    # get all Astronauts
    @app.route('/Astronaut')
    @requires_auth('get:all')
    def get_Astronaut():
        return paginate_Astronaut()
    # get a specific Astronaut
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
    # add a new Astronaut
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
    # edit an Astronaut
    @app.route('/Astronaut/<id>', methods=['PATCH'])
    @requires_auth('patch:one')
    def patch_Astronaut(id):
        try:
            data = json.loads(request.data)
            astronaut = Astronaut.query.get(id)
            if 'name' in data.keys():
                astronaut.name = data['name']
            if 'Job' in data.keys():
                astronaut.Job = data['Job']
            if 'Flight' in data.keys():
                astronaut.Flight = data['Flight']
            db.session.commit()
        except:
            abort(400)
        finally:
            return paginate_Astronaut()
    # delete an Astronaut
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
    # get all stations
    @app.route('/Station')
    @requires_auth('get:all')
    def get_Station():
        return paginate_Station()
    # get a specific Station
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
    # add a new Station
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
    #  edit a Station
    @app.route('/Station/<id>', methods=['PATCH'])
    @requires_auth('patch:one')
    def patch_Station(id):
        try:
            data = json.loads(request.data)
            station = Station.query.get(id)
            if 'CrewCapacity' in data.keys():
                station.CrewCapacity = data['CrewCapacity']
            if 'FuelCapacity' in data.keys():
                station.FuelCapacity = data['FuelCapacity']
            db.session.commit()
        except:
            abort(400)
        finally:
            return paginate_Astronaut()
    # delete a Station
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
    @app.errorhandler(403)
    def not_found(error):
        error_data = {
            "success": False,
            "error": 403,
            "message": "requested resource is forbidden"
        }
        return jsonify(error_data), 403
    @app.errorhandler(400)
    def bad_request(error):
        error_data = {
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }
        return jsonify(error_data), 400

app = create_app()

if __name__ == '__main__':
    app.run()
