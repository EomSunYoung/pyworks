# with ~ as 읽어오기
# kbo2021.txt
# try ~ except 필수
try:
    with open("c:/pyfile/kbo2021.txt", 'r') as f:
        # data = f.read()
        # print(data)

        line = f.readline()
        print(line) # 한 줄 읽기

        lines = f.readlines()
        print(lines)    # 리스트로 읽기

        """
        # data = f.read()   # 전체 읽기
        while True:
            line = f.readline()     # 줄 단위로 읽어오기
            if not line:
                break
        print(line)
        """
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")