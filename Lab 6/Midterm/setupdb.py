import sqlite3

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS Data;')

try:
    cursor.execute('''
        CREATE TABLE Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distance FLOAT,
            x FLOAT,
            y FLOAT,
            z FLOAT
        );
    ''')
except RuntimeError as err:
    print(f'Runtime error: {err}')


from random import uniform
a = 1.05
b = 35
query = 'INSERT INTO Data VALUES (?, ?, ?, ?, ?)'
values = [
    (None, uniform(a, b), uniform(a, b), uniform(a, b), uniform(a, b)),
    (None, uniform(a, b), uniform(a, b), uniform(a, b), uniform(a, b)),
    (None, uniform(a, b), uniform(a, b), uniform(a, b), uniform(a, b))
]
cursor.executemany(query, values)
db.commit()