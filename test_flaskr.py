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
        setup_db(self.app,True, self.database_path)

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
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data,headers=header)
        self.assertEqual(res.status_code,200)
    def test_SpaceShip_faluire(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'n':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data,headers=header)
        self.assertEqual(res.status_code,403)    
    def test_get_SpaceShip(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        res = self.client().get('/Spaceship',headers=header)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_SpaceShip(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data,headers=header)
        res = self.client().get('/Spaceship/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_SpaceShip(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data,headers=header)
        res = self.client().delete('/Spaceship/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_patch_SpaceShip(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Spaceship',data=data,headers=header)
        data = json.dumps({'name':'starship','model':'2024','capacity':2})
        res = self.client().patch('/Spaceship/1',data=data,headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # # test station
    def test_add_Station(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        res = self.client().post('/Station',data=data,headers=header)
        self.assertEqual(res.status_code,200)
    def test_Station_faluire(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'n':'SLS','modesl':'2020','reuseable':'True','capacity':5})
        res = self.client().post('/Station',data=data,headers=header)
        self.assertEqual(res.status_code,403)    
    def test_get_Station(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        res = self.client().get('/Station',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_Station(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        self.client().post('/Station',data=data,headers=header)
        res = self.client().get('/Station/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_Station(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        self.client().post('/Station',data=data,headers=header)
        res = self.client().delete('/Station/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_patch_Station(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        res = self.client().post('/Station',data=data,headers=header)
        data = json.dumps({'crewcapacity':1320,'fuelcapacity':5000})
        res = self.client().patch('/Station/1',data=data,headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # # flight test
    def test_add_Flight(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data,headers=header)
        self.assertEqual(res.status_code,200)
    def test_flight_faluire(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'stati3on':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data,headers=header)
        self.assertEqual(res.status_code,422)
    def test_get_flight(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        res = self.client().get('/Flight',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_flight(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        self.client().post('/Flight',data=data,headers=header)
        res = self.client().get('/Flight/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_flight(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        self.client().post('/Flight',data=data,headers=header)
        res = self.client().delete('/Flight/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_patch_flight(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data,headers=header)
        data = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A234','launchingdate':'2020/1/16'})
        res = self.client().patch('/Flight/1',data=data,headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    # # Astronaut test
    def test_add_Astronaut(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data_flight,headers=header)
        res = self.client().post('/Astronaut',data=data,headers=header)
        self.assertEqual(res.status_code,200)
    def test_Astronaut_flauire(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'jobbb':"IT",'flight':1})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data_flight,headers=header)
        res = self.client().post('/Astronaut',data=data,headers=header)
        self.assertEqual(res.status_code,403)
    def test_get_Astronaut(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        res = self.client().get('/Astronaut',headers=header)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_one_Astronaut(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        self.client().post('/Flight',data=data_flight,headers=header)
        self.client().post('/Astronaut',data=data,headers=header)
        res = self.client().get('/Astronaut',headers=header)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_delete_Astronaut(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        self.client().post('/Flight',data=data_flight,headers=header)
        self.client().post('/Astronaut',data=data,headers=header)
        res = self.client().delete('/Astronaut/1',headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    def test_patch_Astronaut(self):
        token = 'Bearer ' + os.environ.get('Captian')
        header = {'Authorization': token}
        data_station = json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        data_spaceship = json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5})
        data_flight = json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        data = json.dumps({'name':"majed",'job':"IT",'flight':1})
        self.client().post('/Station',data=data_station,headers=header)
        self.client().post('/Spaceship',data=data_spaceship,headers=header)
        res = self.client().post('/Flight',data=data_flight,headers=header)
        res = self.client().post('/Astronaut',data=data,headers=header)
        data = json.dumps({'name':"maijed",'job':"IiiiiT",'flight':1})
        res = self.client().patch('/Astronaut/1',data=data,headers=header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()