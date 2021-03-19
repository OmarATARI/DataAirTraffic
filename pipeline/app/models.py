from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Float

Base = declarative_base()

class Flight(Base):
  """Flight"""

  __tablename__ = "Flights"

  index = Column(Integer, primary_key=True, autoincrement="auto")
  year = Column(Integer)
  month = Column(Integer)
  day = Column(Integer)
  dep_time = Column(Integer)
  sched_dep_time = Column(Integer)
  dep_delay = Column(Integer)
  arr_time = Column(Integer)
  sched_arr_time = Column(Integer)
  arr_delay = Column(Integer)
  carrier = Column(String)
  flight = Column(Integer)
  tailnum = Column(String)
  origin = Column(String, ForeignKey('Airports.faa'))
  dest = Column(String, ForeignKey('Airports.faa'))
  air_time = Column(Integer)
  distance = Column(Integer)
  hour = Column(Integer)
  minute = Column(Integer)
  time_hour = Column(String)

  parent_id = Column(String, ForeignKey('Planes.tailnum'))
  parent = relationship("Plane", back_populates="children")

  airline_id = Column(String, ForeignKey('Airlines.carrier'))
  airline = relationship("Airline", back_populates="children")

  airport = relationship("Airport", back_populates="children")

  def serialize(self):
    return {
        'index': self.index, 
        'carrier': self.carrier,
        'flight': self.flight,
        'tailnum': self.tailnum,
        'origin': self.origin,
        'dest': self.dest
    }

class Plane(Base):
  """Planes"""

  __tablename__ = "Planes"

  tailnum = Column(String, primary_key=True)
  year = Column(Integer)
  type_ = Column(String)
  manufacturer = Column(String)
  model = Column(String)
  engines = Column(Integer)
  seats = Column(Integer)
  speed = Column(Integer)
  engine = Column(String)
  children = relationship("Flight", back_populates="parent")

class Airport(Base):
  """Airports"""

  __tablename__ = "Airports"

  faa = Column(String, primary_key=True)
  name = Column(String)
  lat = Column(String)
  lon = Column(String)
  alt = Column(Integer)
  tz = Column(Integer)
  dst = Column(String)
  tzone = Column(String)

  children = relationship("Flight", back_populates="airport")

class Airline(Base):
  """Airlines"""

  __tablename__= "Airlines"

  carrier = Column(String, primary_key=True)
  name = Column(String)

  children = relationship("Flight", back_populates="airline")


class Weather(Base):
  """Weather"""

  __tablename__ = "Weather"

  origin = Column(String, primary_key=True)
  year =  Column(Integer, primary_key=True)
  month =  Column(Integer, primary_key=True)
  day =  Column(Integer, primary_key=True)
  hour =  Column(Integer, primary_key=True)

  temp = Column(Float)
  dewp = Column(Float)
  humid = Column(Float)
  wind_dir = Column(Integer)
  wind_speed = Column(Float)
  wind_gust = Column(Float)
  precip = Column(Float)
  pressure = Column(Float)
  visib = Column(Float)
  time_hour = Column(String)
