import os
import glob

os.chdir('c:/webDev/pyworks')   # webDev로 이동
dir = os.popen('dir')   # 'dir' 명령 실행

# print(dir.read())

# glob 모듈로 file_io의 파일 이름 알아내기 - txt 파일 읽어오기
data = glob.glob("c:/webDev/pyworks/Day28/file_io/*.txt")
print(data)

# animal.txt 읽기
with open("c:/webDev/pyworks/Day28/file_io/animal.txt", 'r') as f:
    data = f.read()
    print(data)

