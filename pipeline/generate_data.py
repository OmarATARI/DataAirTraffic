import pandas as pd
from time import sleep
from sqlalchemy import create_engine

if __name__ == '__main__':
    connection = create_engine("postgresql://pxl:password@localhost/airtraffic")
    
    flights = pd.read_csv('../csv/flights.csv')
    print(flights.head(10).to_dict())
    flights.head(10).to_sql('Flights', connection)
