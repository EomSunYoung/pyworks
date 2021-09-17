import sqlite3

def getconn():
    conn = sqlite3.connect("c:/webDB/webDB.db")
    return conn
