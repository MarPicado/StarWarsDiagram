import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(40))
    gravity = Column(String(40))
    terrain = Column(String(40))
    surface_water = Column(Integer)
    gravity = Column(String(40))

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(Integer)
    hair_color = Column(String(40))
    skin_color = Column(String(40))
    eye_color = Column(String(40))
    birth_year = Column(String(40), nullable=False)
    gender = Column(String(15))
    surface_water = Column(Integer)
    homeworld = Column(String(200))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(100), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    people_id = Column(String(40), ForeignKey(People.id))
    planets_id = Column(String(40), ForeignKey(Planets.id))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')