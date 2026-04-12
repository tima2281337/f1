import fastf1 as f1
import pandas as pd
import sqlite3 as sql

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

print(df)
