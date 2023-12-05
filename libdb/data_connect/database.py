import sqlite3
from sqlite3 import Error
import os

folder_db = os.path.dirname(__file__)
db_path = os.path.join(folder_db, "books.db")


def connect_database():
	con=None
	try:
		con=sqlite3.connect(db_path)
	except Error as ex:
		print(ex)
	return con

def login(data):
    con = connect_database()
    cursor = con.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE email ='{data["email"]}' AND password = '{data["password"]}' """)
    result = cursor.fetchone() is not None
    con.close()
    if result is True:
        return True
	
	
def register(data):
	print(data)
	con = connect_database()
	cursor = con.cursor()
	cursor.execute(f"""INSERT INTO users values(
		NULL,
		'{data["firstName"]}', 
		'{data["lastName"]}', 
		'{data["password"]}', 
		'{data["email"]}', 
		'{data["gender"]}', 
		'{data["age"]}', 
		'{data["address"]}')""")
	con.commit()
	con.close()
	

def dql(query):  # select
    con = connect_database()
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    con.close()
    return result

def dml(query): # insert, delete
    try:
        con = connect_database()
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        con.close()
    except Error as ex:
        print(ex)

