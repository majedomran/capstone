##### Introduction 

this is the Backend for the international space station or at least an extremely simiplified version of it

- Motivation
    - since i have already done a DataBase model for this project in college i thought to myself why not do a complete backend for it 
# the station system has four sections which are as follows:


1. Station: the station it self
2. SpaceShip: the main way to get to the station 
3. Flight: which has a specific date and SpaceShip and many Astronatus 
4. Astronaut: they are the backbone of the station and get between earth and space by using SpaceShips
#### Dependencies
- all dependencies are included in the requiremnets.txt file and you can run them by the command:
    'pip3 install -r requirements.txt'
- for runnig the development server:
    'export FLASK_APP=api.py;'
    'flask run --reload'
#### how to use the API
- Authentication:
    - is provided by Auth0 
    - their are two levels of roles:
        - Captian : which can access everything
        - Astronaut: which onle can access basic get endpoints
    - you need a JWT to access the endpoints which all are provided in the setup.sh file and you can export them yo the enviroment by the command 
    'source setup.sh'
    -an example for the authentication in a header:
    header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IncyZVdtNWdrMl9nVjBNMVMtZWtFcCJ9.eyJpc3MiOiJodHRwczovL2Rldi04b2JlaGV1ei5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4YTg1ZGNiYWFhMWMwMDZmNmM0YzM3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDY2NDY1MzcsImV4cCI6MTYwNjczMjkzNywiYXpwIjoiNkE0bmg5MkpLY24yenNMdUtTbTZCRkoyQlFxbFZiSU8iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpvbmUiLCJnZXQ6YWxsIiwiZ2V0Om9uZSIsInBvc3Q6b25lIl19.StJRmer_TnduFTmZtj7JUwWO4btu0G_ENz28ayKEudbaPzQs_eoPzEUjcRM2tcI2wBo2dtDcirvaUlsQHmOsvNbpCJvRGcJpxs7sR5j0rUsJPSeR5J2v0AgG1PPPPY8Sq2UcGOGbf0X5pqMQaKo6w_VVaABNfQqmlp5wbrkUP1Gj--NE9Y-8UaXgNN0p5SYrqQ7KFK0Kgg27DkYEMFmbAV6q0gPbucAhOyYfm-mUhH-oGAC2ey2Mtr4x1LoJLKpQHdap3VtkgT3ExpAtzfYEwOcI-wGYnyL0c3f78Yo808ACbSY5rcQJBEpsIBDLTfxwlUcAWouADxGuRsSzmOIb6w'}

1. SpaceShip:
    - Attributes:
        - id: is the primary key
        - name 
        - model: the year of making 
        - reuseable: to know if a rocket can be used for more than one time 
        - capacity: how many astronauts can the rocket carry 
    - EndPoints:
        - Post: adds a SpaceShip
        only Accesable by Captians 
        json.dumps({'name':'SLS','model':'2020','reuseable':'True','capacity':5}) 
        requests.post('https://heroku-sample-majed.herokuapp.com/Spaceship',data=data,headers=header)
        - get: gets all SpaceShips
        only Accesable by Astronaut
        requests.get('https://heroku-sample-majed.herokuapp.com/Spaceship',headers=header)
        - get: Gets a specific SpacShip
        only accesable by Captain
        requests.get('https://heroku-sample-majed.herokuapp.com/Spaceship/1',headers=header)
        - delete: deletes a SpaceShip
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Astronaut/2',headers=header)
        - patch: edits a SpaceShip 
        only accessable by a Captian
        requests.patch('https://heroku-sample-majed.herokuapp.com/Spaceship/1',headers=header)

2. Station:
    - Attributes:
        - id: is the primary key
        - CrewCapacity: number of crew it can maintain
        - FuelCapacity: amount of fuel the Statin can carry
    - EndPoints:
        - Post: adds a Station
        only Accesable by Captians 
        json.dumps({'crewcapacity':10,'fuelcapacity':500000})
        requests.post('https://heroku-sample-majed.herokuapp.com/Station',data=data_Station,headers=header)
        - get: gets all Stations
        only Accesable by Astronaut
        requests.get('https://heroku-sample-majed.herokuapp.com/Station',headers=header)
        - get: Gets a specific Station
        only accesable by Captain
        requests.get('https://heroku-sample-majed.herokuapp.com/Station/1',headers=header)
        - delete: deletes a Station
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Station/2',headers=header)
        - patch: edits a Station 
        only accessable by a Captian
        requests.patch('https://heroku-sample-majed.herokuapp.com/Station/1',headers=header)
3. Flight:
    - Attributes:
        - id: is the primary key
        - SpaceShip: the specific SpaceShip that is going to carry the astronauts
        - Station: which Station the SpaceShip will dock with
        - LaunchingPad: which lauchpad the rocket is going to launch from 
        - LaunchingDate: at which time the flight is going to take place
    - EndPoints:
        - Post: adds a Flight and must point to an existing SpaceShip and Station 
        only Accesable by Captians 
        json.dumps({'spaceship':1,'station':1,'launchingpad':'37A','launchingdate':'2020/11/16'})
        requests.post('https://heroku-sample-majed.herokuapp.com/Flight',data=data_flight,headers=header) 
        - get: gets all Flights
        only Accesable by Astronaut
        requests.get('https://heroku-sample-majed.herokuapp.com/Flight',headers=header)
        - get: Gets a specific Flight
        only accesable by Captain
        requests.get('https://heroku-sample-majed.herokuapp.com/Flight/1',headers=header)
        - delete: deletes a Flight
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Flight/2',headers=header)
        - patch: edits a Flight 
        only accessable by a Captian
        requests.patch('https://heroku-sample-majed.herokuapp.com/Astronaut/1',headers=header)
4. Astronaut:
    - Attributes:
        - id: is the primary key
        - name:
        - Job: what kind of job does the astronaut do 
        - Flight: which flight is he going to take
    - EndPoints:
        - Post: adds an Astronaut and must point to an existing Flight 
        only Accesable by Captians 
        json.dumps({'name':'majed','job':"IT",'flight':1})
        requests.post('https://heroku-sample-majed.herokuapp.com/Astronaut',data=data_astronaut,headers=header)
        - get: gets all Astronauts
        only Accesable by Astronaut
        requests.get('https://heroku-sample-majed.herokuapp.com/Astronaut',headers=header)
        - get: Gets a specific Astronaut
        only accesable by Captain
        requests.get('https://heroku-sample-majed.herokuapp.com/Astronaut/1',headers=header)
        - delete: deletes a Astronaut
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Astronaut/2',headers=header)
        - patch: edits an Astronaut
        only accessable by a Captian
        requests.patch('https://heroku-sample-majed.herokuapp.com/Astronaut/1',headers=header)
#### expected responses:
    
- GET:
    {
    "SpaceShips": [
        {
            "capacity": 5,
            "id": 1,
            "model": "2020",
            "name": "SLS",
            "reuseable": true
        }
    ],
    "success": true
    }
- GET: get an item
    {
    "SpaceShip": {
        "capacity": 5,
        "id": 1,
        "model": "2020",
        "name": "SLS",
        "reuseable": true
    },
    "success": "True"
    }
- POST:
    "SpaceShips": [
        {
            "capacity": 5,
            "id": 1,
            "model": "2020",
            "name": "SLS",
            "reuseable": true
        },
        {
            "capacity": 2,
            "id": 2,
            "model": "1965",
            "name": "atlas",
            "reuseable": False
        }
    ],
    "success": true
    }
- DELETE:
    {
        "Deleted Spaceship": 1,
        "success": True
    }
- PATCH:
    "SpaceShips": [
        {
            "capacity": 5,
            "id": 1,
            "model": "2020",
            "name": "SLS",
            "reuseable": true
        },
        {
            "capacity": 2,
            "id": 2,
            "model": "1965",
            "name": "atlas",
            "reuseable": False
        }
    ],
    "success": true
    }

        
