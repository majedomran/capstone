import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from app import create_app
from models import setup_db

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy() 
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    def tearDown(self):
        """Executed after reach test"""
        pass
    def test_main_app(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code,200)
    # test spaceShip
    def test_add_SpaceShip(self):
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        print('1')
        res = self.client().post('/Spaceship',data=data)
        self.assertEqual(res.status_code,200)
    def test_get_SpaceShip(self):
        res = self.client().get('/Spaceship')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_SpaceShip(self):
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data)
        res = self.client().get('/Spaceship/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_SpaceShip(self):
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data)
        res = self.client().delete('/Spaceship/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # test station
    def test_add_Station(self):
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        print('2')
        res = self.client().post('/Station',data=data)
        self.assertEqual(res.status_code,200)
    def test_get_Station(self):
        res = self.client().get('/Station')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_Station(self):
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        self.client().post('/Station',data=data)
        res = self.client().get('/Station/1')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_Station(self):
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        self.client().post('/Station',data=data)
        res = self.client().delete('/Station/1')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # flight test
    def test_add_Flight(self):
        print('3')
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        res = self.client().post('/Flight',data=data)
        self.assertEqual(res.status_code,200)
    def test_get_flight(self):
        res = self.client().get('/Flight')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_flight(self):
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        self.client().post('/Flight',data=data)
        res = self.client().get('/Flight/1')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_flight(self):
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        self.client().post('/Flight',data=data)
        res = self.client().delete('/Flight/1')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # Astronaut test
    def test_add_Astronaut(self):
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        res = self.client().post('/Flight',data=data_flight)
        res = self.client().post('/Astronaut',data=data)
        self.assertEqual(res.status_code,200)
    def test_get_Astronaut(self):
        res = self.client().get('/Astronaut')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_Station(self):
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        self.client().post('/Flight',data=data_flight)
        self.client().post('/Astronaut',data=data)
        res = self.client().get('/Astronaut')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_Astronaut(self):
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station)
        self.client().post('/Spaceship',data=data_spaceship)
        self.client().post('/Flight',data=data_flight)
        self.client().post('/Astronaut',data=data)
        res = self.client().delete('/Astronaut/1')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()