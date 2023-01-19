import sqlite3

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS objects;')

try:
    cursor.execute('''
        CREATE TABLE objects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            colorhl INTEGER,
            colorsl INTEGER,
            colorvl INTEGER,
            colorhh INTEGER,
            colorsh INTEGER,
            colorvh INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE found_objects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object_name TEXT,
            address TEXT
        );
    ''')
except RuntimeError as err:
    print(f'Runtime error: {err}')

query = 'INSERT INTO objects VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
values = [
    (None, 'apple', 4, 93, 52, 4, 67, 41),
    (None, 'orange', 28, 93, 97, 44, 63, 75),
    (None, 'banana', 59, 98, 99, 69, 58, 80)
]
cursor.executemany(query, values)
db.commit()