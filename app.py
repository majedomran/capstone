import os
from flask import Flask,jsonify,request,abort
from models import Flight, Vehicle, setup_db
from flask_cors import CORS
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    def paginate_flights():
        flights_paginated = []
        flights = Flight.query.all()
        for flight in flights:
            flights_paginated.append(flight.format())
        return jsonify(flights_paginated)
    def paginate_vehicles():
        vehicles_paginated = []
        vehicles = Vehicle.query.all()
        for vehicle in vehicles:
            vehicles_paginated.append(vehicle.format())
        return jsonify(vehicles_paginated)
    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting
    # Flight 
    @app.route('/Flight')
    def get_flights():
        return paginate_flights()  
    @app.route('/Flight/<id>',methods=['GET'])
    def get_flight_id(id):
        try:
            flight = Flight.query.get(id)
        except:
            abort(404)  
        finally:
            return jsonify({'success':'True','Flight':flight.format()})
    @app.route('/Flight',methods=['POST'])
    def add_Flight():
        print(request.form)
        flight = Flight(origin = request.form['origin'],destination=request.form['destination'],vehicle=request.form['vehicle'])
        Flight.insert(flight)
        return paginate_flights()
    @app.route('/Flight/<id>',methods=['DELETE'])
    def delete_flight(id):
        try:
            flight = Flight.query.get(id)
            Flight.delete(flight)
        except:
            abort(404)
        finally:
            return jsonify({'Deleted flight':id,'success':True})
    # Vehicle
    @app.route('/Vehicle')
    def get_vehicles():
        return paginate_vehicles()  
    @app.route('/Vehicle/<id>',methods=['GET'])
    def get_vehicle_id(id):
        vehicle = Vehicle.query.get(id)
        return jsonify(vehicle.format())
    @app.route('/Vehicle',methods=['POST'])
    def add_vehicle():
        print(request.form['reuseable'])
        reuseable =False
        if(request.form['reuseable'] == 'True'):
            reuseable = True
        vehicle = Vehicle(name = request.form['name'],model=request.form['model'],reuseable=reuseable,capacity=request.form['capacity'])
        Vehicle.insert(vehicle)
        return paginate_vehicles()
    @app.route('/Vehicle/<id>',methods=['DELETE'])
    def delete_vehicle(id):
        vehicle = Vehicle.query.get(id)
        Vehicle.delete(vehicle)
        return jsonify({'Deleted vehicle':id,'success':True})
    return app

app = create_app()

if __name__ == '__main__':
    app.run()