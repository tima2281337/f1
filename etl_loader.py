import fastf1 as f1
import pandas as pd

session = f1.get_session(2021, 'French Grand Prix', 'Q')
session.load(laps=False, telemetry=False)
df = session.results[['FullName', 'TeamName', 'Abbreviation']]
df = df.rename(columns={'FullName':'name', 'TeamName':'team', 'Abbreviation':'abb'})

print(df)
