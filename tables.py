import sqlite3 as sql


connection = sql.connect('f1max.db')
cursor = connection.cursor()
#подключение внешних ключей
cursor.execute('PRAGMA foreign_keys = ON;')

#таблица гонщиков
cursor.execute('''
    create table if not exists drivers(
        driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(255) not null unique,
        team varchar(255) not null,
        date_of_birth integer not null   
    )
''')
#таблица гонок
cursor.execute('''
    create table if not exists races(
        race_id INTEGER PRIMARY KEY AUTOINCREMENT,
        season integer not null,
        country varchar(100) not null,
        road_type varchar(20) not null
    )
''')
#таблица результатов
cursor.execute('''
    create table if not exists results(
        results_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        driver_id int references drivers(driver_id),
        race_id int references races(race_id),
        pole_pos integer not null,
        fin_pos integer not null,
        points real not null,
        status varchar(20) not null
    )
''')

cursor.execute('''
    create table if not exists laptime(
        lap_id integer primary key autoincrement,
        driver_id int references drivers(driver_id),
        race_id int references races(race_id),
        tires varchar(50) not null,
        lap_number integer not null,
        lap_time real not null
    )
''')


connection.commit()
connection.close()