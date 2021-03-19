import pandas as pd
from database import session, engine

def clean_empty_df_columns(df):
  for column in df.columns:
    df = df.drop(df[df[f'{column}'] == ' '].index)
    df = df.drop(df[df[f'{column}'] == ''].index)
    df = df.drop(df[df[f'{column}'] == None].index)
  return df

def clean(dfs):
  cleaned_dfs = []
  for df in dfs:
    cleaned_dfs.append(clean_empty_df_columns(df))

  return cleaned_dfs

if __name__ == '__main__':
    connection = engine

    flights = pd.read_csv('csv/flights.csv')
    airlines = pd.read_csv('csv/airlines.csv', index_col='carrier')
    airports = pd.read_csv('csv/airports.csv', index_col='faa')
    planes = pd.read_csv('csv/planes.csv', index_col='tailnum')

    planes = planes.rename(columns = { 'type': 'type_'})
    # Prevent contraint errors when inserting
    flights = flights[flights.dest.isin(airports.index)]
    flights = flights[flights.origin.isin(airports.index)]
    clean_dataframes = clean([flights, airlines, airports, planes])

    clean_dataframes[1].to_sql('Airlines', connection, if_exists='append')
    clean_dataframes[2].to_sql('Airports', connection, if_exists='append')
    clean_dataframes[3].to_sql('Planes', connection, if_exists='append')
    clean_dataframes[0].to_sql('Flights', connection, if_exists='append')