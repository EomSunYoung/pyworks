# employee 테이블 관리
from Day28.libs.dbconn import getconn

# 전체 자료 검색
def select_data():
    conn = getconn()
    cur = conn.cursor()     # cur : 모든 작업을 하는 객체
    sql = "SELECT * FROM employee"
    cur.execute(sql)        # 데이터베이스에서 sql 문을 실행
    rs = cur.fetchall()     # 데이터베이스에서 가져온 모든 자료 기억(ResultSet)
    for i in rs:
        print(i)
    conn.close()

# 자료 추가
def insert_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('e1005', '박인비', 33, 15000))   # 동작 바인딩 방식
    conn.commit()   # 삽입, 수정, 삭제시는 반드시 명시해야 함
    conn.close()

# 자료 수정
def update_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age = ?, salary = ? WHERE emp_id = ?"
    cur.execute(sql, (20, 5000, 'e1004'))
    conn.commit()
    conn.close()

# 자료 삭제
def delete_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = ?"
    cur.execute(sql, ('e1003', ))   # 튜플은 1개 추가할 때 뒤에 ,(콤마)를 붙인다. ☆주의
    conn.commit()
    conn.close()

# 자료 1개 검색
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE emp_id = ?"
    cur.execute(sql, ('e1004',))
    rs = cur.fetchone()
    print(rs)
    conn.close()

if __name__ == "__main__":
    # delete_data()
    # insert_data()
    # update_data()
    # select_data()
    select_one()
