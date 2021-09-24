# member 테이블 생성 및 관리
from Day28.libs.dbconn import getconn
# import sqlite3

def create_table():
    # conn = sqlite3.connect("c:/webDB/webDB.db")   # db 연결 객체 생성
    conn = getconn()
    cur = conn.cursor()    # db 작업객체 생성
    sql = """
        CREATE TABLE member(
            memberid char(5) PRIMARY KEY,
            passwd   char(5) NOT NULL,
            name     TEXT NOT NULL,
            age      INTEGER,
            reg_date DATETIME DEFAULT CURRENT_TIMESTAMP 
        )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert_member():
    # conn = sqlite3.connect("c:/webDB/webDB.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(memberid, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10004', 'd1234567', '팥쥐', 15))
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()    # 전체 자료 반환
    for i in rs:
        print(i)
    conn.close()

# 1개 정보 찾기
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT memberid, passwd FROM member WHERE memberid = ?"
    cur.execute(sql, ('10002', ))   # 1개를 매칭할 때 , 를 씀
    rs = cur.fetchone()
    print(rs)
    conn.commit()
    conn.close()

# 자료 수정
def update_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET age = ? WHERE memberid = ?"
    cur.execute(sql, (37, '10001'))   # 순서대로 매핑
    conn.commit()
    conn.close()

def delete_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberid = ?"
    cur.execute(sql, ('10002', ))  # 순서대로 매핑
    conn.commit()
    conn.close()

# create_table()
# insert_member()
select_member()
# select_one()
# update_member()
delete_member()