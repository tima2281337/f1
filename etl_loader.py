import fastf1 as f1
import pandas as pd
import sqlite3 as sql

road_type = {
    'Monaco': 'Street',
    'Belgium':'Permanent', 
    'Saudi Arabia': 'Street', 
    'Bahrain':'Permanent', 
    'Australia':'Street', 
    'Japan':'Permanent',
    'China':'Permanent',
    'Miami':'Permanent',
    'Italy':'Permanent',
    'Canada':'Permanent',
    'Spain':'Permanent',
    'Austria':'Permanent',
    'Britain':'Permanent',
    'Hungary':'Permanent',
    'Netherlands':'Permanent',
    'Italy':'Permanent',
    'Azerbaijan':'Street',
    'Singapore':'Street',
    'United States':'Permanent',
    'Mexico':'Permanent',
    'Brazil':'Permanent',
    'Las Vegas':'Street',
    'Qatar':'Permanent',
    'Abu Dhabi':'Permanent'
}

session = f1.get_session(2024, 7, 'Q')
session.load(laps=False, telemetry=False)
df = session.results[['FullName', 'TeamName', 'Abbreviation']]
df = df.rename(columns={'FullName':'name', 'TeamName':'team', 'Abbreviation':'abb'})


connection = sql.connect('f1max.db')
try:
    df.to_sql('drivers', connection, if_exists='append', index=False, method='multi')
    print('добавили')
except Exception as e:
    print(f"что-то пошло не так: {e}")

connection.close()

country_name = session.event['Country']
race_info = {
    'season': int(session.event.year),
    'country': country_name,
    'road_type': road_type.get(country_name, 'Permanent')
}
race_df = pd.DataFrame([race_info])

print(race_df)

connection = sql.connect('f1max.db')
try:
    race_df.to_sql('races', connection, if_exists='append', index=False, method='multi')
    print('добавили')
except Exception as e:
    print(f"что-то пошло не так: {e}")

connection.close()


print(session.results.columns)