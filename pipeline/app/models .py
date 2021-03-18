from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String

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
  name = Column(integer)
  lat = Column(String)
  lon = Column(String)
  alt = Column(String)
  tz = Column(Integer)
  dst = Column(String)
  tzone = Column(String)

class Airline(Base):
  """Airlines"""

  __tablename__= "Airlines"
jjcdkckjd kj dk kx kjdckjdckjdcndkcjdkjcndk