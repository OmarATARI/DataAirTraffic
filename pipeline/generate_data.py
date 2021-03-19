import pandas as pd
from sqlalchemy import create_engine
from database import session, engine

if __name__ == '__main__':
    #connection = create_engine("postgresql://pxl:password@localhost/airtraffic")
    connection = engine
    
    flights = pd.read_csv('../csv/flights.csv')
    airlines = pd.read_csv('../csv/airlines.csv')
    airports = pd.read_csv('../csv/airports.csv')
    weather = pd.read_csv('../csv/weather.csv')
    planes = pd.read_csv('../csv/planes.csv')

    print(flights.head(10).to_dict())
    print(airlines.head(10).to_dict())
    print(airports.head(10).to_dict())
    print(planes.head(10).to_dict())

    flights.head(10).to_sql('Flights', connection)
    airlines.head(10).to_sql('Airlines', connection)
    airports.head(10).to_sql('Airports', connection)
    weather.head(10).to_sql('Weather', connection)
    planes.head(10).to_sql('Planes', connection)
