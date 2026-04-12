import sqlite3 as sql
connection = sql.connect('f1max.db')
cursor = connection.cursor()
cursor.execute('''
    create table if not exists drivers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(255) not null unique,
        team varchar(255) not null,
        age integer not null   
    )
''')

cursor.execute('insert or ignore into drivers(name,team,age) values(?,?,?)', ('Max Verstappen', 'Red Bull Racing', 28))

cursor.execute('select * from drivers')
drivers = cursor.fetchall()
for driver in drivers:
    print(driver)

connection.commit()
connection.close()