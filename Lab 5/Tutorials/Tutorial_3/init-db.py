import mysql.connector as mysql
import os
import datetime
from dotenv import load_dotenv  # only required if using dotenv for creds

load_dotenv('credentials.env')
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass,
                   host=db_host, database=db_name)
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS TeachingStaff;")

try:
    cursor.execute("""
    CREATE TABLE TeachingStaff (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      name        VARCHAR(50) NOT NULL,
      designation VARCHAR(50) NOT NULL,    
      email       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
    """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))


query = "INSERT INTO TeachingStaff (name, designation, email, created_at) VALUES (%s, %s, %s, %s)"
values = [
 ('Ramsin Khoshabeh','Professor','ramsin@artofproducts.com', datetime.datetime.now()),
 ('Rick Gessner','Professor','rick@artofproducts.com',datetime.datetime.now()),
 ('Marcus Schaller','Teaching Assistant','marcus@artofproducts.com', datetime.datetime.now()),
 ('Manas Bedmutha','Teaching Assistant','manas@artofproducts.com', datetime.datetime.now()),
 ('Gandhar Deshpande','Tutor','gandhar@artofproducts.com',datetime.datetime.now()),
 ('Sriram Sreedharan','Tutor','sriram@artofproducst.com',datetime.datetime.now())
]
cursor.executemany(query, values)
db.commit()