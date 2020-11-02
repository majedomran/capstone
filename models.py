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
    db.session.commit() 
    # db.drop_all()
    db.create_all()

'''
Person
Have title and release year
'''

class Person(db.Model):  

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase
      
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}
  def insert(self):
        db.session.add(self)
        db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()
class Flight(db.Model):
  id = Column(Integer,primary_key=True)
  origin = Column(String)
  destination = Column(String)
  vehicle = Column(Integer )
  def format(self):
        return {
      'id': self.id,
      'origin': self.origin,
      'destination': self.destination,
      'vehicle' : self.vehicle
      }
  def insert(self):
          db.session.add(self)
          db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()
class Vehicle(db.Model):
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
