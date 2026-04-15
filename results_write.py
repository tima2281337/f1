import sqlite3 as sql
import pandas as pd
import fastf1 as f1

connection = sql.connect('f1max.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

session = f1.get_session(2024, 7, 'R')
session.load(laps=False, telemetry=False)

current_country = session.event['Country']
current_season = int(session.event.year)

query = f"SELECT race_id FROM races WHERE country = '{current_country}' AND season = {current_season}"
race_id_df = pd.read_sql_query(query, connection)

if not race_id_df.empty:
    current_race_id = int(race_id_df.iloc[0]['race_id'])
    print(f"ID нашей гонки в базе: {current_race_id}")
else:
    print("Гонка не найдена в базе!")

query1 = f"SELECT driver_id, abb FROM drivers"
spravka = pd.read_sql_query(query1, connection)
print(spravka)

final_results = session.results.merge(spravka, left_on='Abbreviation', right_on='abb')
print(final_results)
final_results['race_id'] = current_race_id
final_results = final_results[[
    'driver_id',
    'race_id',
    'GridPosition',
    'Position',
    'Points',
    'Status'
]]
final_results = final_results.rename(columns = {'GridPosition':'pole_pos', 'Position':'fin_pos', 'Points':'points', 'Status':'status'})
final_results['fin_pos'] = final_results['fin_pos'].astype(int)

try:
    final_results.to_sql('results', connection, if_exists='append', index=False)
    print(f"Результаты гонки успешно загружены! Обработано {len(final_results)} пилотов.")
except Exception as e:
    print(f"Ошибка при загрузке результатов: {e}")

connection.commit()
connection.close()