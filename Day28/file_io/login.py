# 아이디와 비밀번호 입력 후 로그인 구현
from getpass import getpass

def login():
    userid = input("Eter userID : ")
    # userpa = input("Enter password : ")
    userpa = getpass("Enter password : ")

    member = []     # 이차원 리스트 생성
    with open('member.txt', 'r') as f:
        lines = f.readlines()
        # print(lines)
    for i in lines:
        member.append([i[0:10], i[10:]])
    # print(member)

    access = False  # 로그인 성공 여부 변수
    for user, passwd in member:    # member에 있는 아이디, 비밀번호
        if user.strip() == userid and passwd.strip() == userpa:
            print("로그인에 성공했습니다.")
            access = True
            break
    if access == False:
        print("아이디나 비밀번호가 다릅니다.")
login()