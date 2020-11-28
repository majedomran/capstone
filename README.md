##### Introduction 

this is the Backend for the international space station or at least an extremely simiplified version of it
 
# the station system has four sections which are as follows:


1. Station: the station it self
2. SpaceShip: the main way to get to the station 
3. Flight: which has a specific date and SpaceShip and many Astronatus 
4. Astronaut: they are the backbone of the station and get between earth and space by using SpaceShips

#### how to use the API

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
        -delete: deletes a Station
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Station/2',headers=header)
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
        -delete: deletes a Flight
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Flight/2',headers=header)
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
        -delete: deletes a Astronaut
        only accesable by a Captain
        requests.delete('https://heroku-sample-majed.herokuapp.com/Astronaut/2',headers=header)


        
