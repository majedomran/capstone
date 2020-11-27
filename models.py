from sqlalchemy import Column, String,Integer,Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os
database_path = 'postgres://jacjbynzzzwfvc:18fa778bcf412fe1f027cebdf64e5bf5c5b831f5ec25b019f72d0f6af99a8e03@ec2-54-156-85-145.compute-1.amazonaws.com:5432/d8tfe8vij6fp4r'

db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
#     db.session.commit() 
#     db.drop_all()
    db.create_all()

'''
Person
Have title and release year
'''

class Astronaut(db.Model):  
  __tablename__ = 'astronaut'
  id = Column(Integer, primary_key=True)
  name = db.Column(db.String(),nullable=False)
  Job = db.Column(db.String(),nullable=False)
  Flight = db.Column(db.Integer,db.ForeignKey('flight.id'))
 
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'Job': self.Job,
      'Flight': self.Flight
      }
  def insert(self):
        db.session.add(self)
        db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()

class SpaceShip(db.Model):
  __tablename__ = 'spaceship'
  id = Column(Integer,primary_key=True)
  name = Column(String)
  model = Column(String)
  reuseable = Column(Boolean)
  capacity = Column(Integer)
  def format(self):
        return {
      'id': self.id,
      'name': self.name,
      'model': self.model,
      'reuseable' : self.reuseable,
      'capacity' : self.capacity
      }
  def insert(self):
        db.session.add(self)
        db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()
class Station(db.Model):
  __tablename__ = 'station'
  id = db.Column(db.Integer,primary_key=True)
  CrewCapacity =db.Column(db.Integer,nullable=False)
  FuelCapacity = db.Column(db.Integer,nullable=False)
  def format(self):
        return {
      'id': self.id,
      'CrewCapacity': self.CrewCapacity,
      'FuelCapacity': self.FuelCapacity
      }
  def insert(self):
          db.session.add(self)
          db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()
class Flight(db.Model):
  __tablename__ = 'flight'
  id = db.Column(db.Integer,primary_key=True)
  SpaceShip =db.Column(db.Integer,db.ForeignKey('spaceship.id'),nullable=False)
  Station = db.Column(db.Integer,db.ForeignKey('station.id'),nullable=False)
  LaunchingPad = db.Column(db.String(),nullable=False)
  LaunchingDate = db.Column(db.String(),nullable=False) 
  def format(self):
        return {
      'id': self.id,
      'SpaceShip': self.SpaceShip,
      'Station': self.Station,
      'LaunchingPad' : self.LaunchingPad,
      'LaunchingDate' : self.LaunchingPad
      }
  def insert(self):
          db.session.add(self)
          db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()
