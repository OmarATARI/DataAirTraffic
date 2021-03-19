from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Float

Base = declarative_base()

class Name(Base):
  """Name account."""

  __tablename__ = "NAMES"
  
  index = Column(Integer, primary_key=True, autoincrement="auto")
  name = Column(String(255), unique=True, nullable=False)
  occurences = Column(Integer)
  gender = Column(String(1), nullable= False)

  def __repr__(self):
    return "<Name %r>" % self.name

  def serialize(self):
    return {
        'index': self.index, 
        'name': self.name,
        'occurences': self.occurences,
        'gender': self.gender
    }

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
  origin = Column(String)
  dest = Column(String)
  air_time = Column(Integer)
  distance = Column(Integer)
  hour = Column(Integer)
  minute = Column(Integer)
  time_hour = Column(String)

  def serialize(self):
    return {
        'index': self.index, 
        'carrier': self.carrier,
        'flight': self.flight,
        'tailnum': self.tailnum,
        'origin': self.origin,
        'dest': self.dest
    }

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

class Plane(Base):
  """Planes"""

  __tablename__ = "Planes"

  tailnum = Column(String, primary_key=True)
  name = Column(Integer)
  lat = Column(String)
  lon = Column(String)
  alt = Column(String)
  tz = Column(Integer)
  dst = Column(String)
  tzone = Column(String)

class Airline(Base):
  """Airlines"""

  __tablename__= "Airlines"

  carrier = Column(String, primary_key=True)
  name = Column(String)

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
