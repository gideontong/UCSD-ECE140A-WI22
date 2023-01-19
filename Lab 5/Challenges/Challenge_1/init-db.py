import sqlite3
import datetime

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS Gallery;")

try:
    cursor.execute("""
    CREATE TABLE Gallery (
      id          integer   PRIMARY KEY AUTOINCREMENT,
      name        VARCHAR(50) NOT NULL,
      owner VARCHAR(50) NOT NULL,    
      height       integer,
      age  integer
    );
    """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))


query = "INSERT INTO Gallery (name, owner, height, age) VALUES (?, ?, ?, ?)"
values = [
  ('Geisel-1.jpg', 'Terrell Gilmore', 163, 45),
  ('Geisel-2.jpg', 'Sila Mann', 189, 51),
  ('Geisel-3.jpg', 'Nyle Hendrix', 152, 27),
  ('Geisel-4.jpg', 'Axel Horton', 176, 21),
  ('Geisel-5.jpg', 'Courtney Mcneil', 172, 64)
]
cursor.executemany(query, values)
db.commit()