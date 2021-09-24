import sqlite3

def getconn():
    conn = sqlite3.connect("c:/webDB/myDB.db")
    return conn

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO tbl_book(title, publishar, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('점프 투 파이썬', '박응용', 350))
    conn.commit()
    conn.close()

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM tbl_book"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

insert_book()
select_book()