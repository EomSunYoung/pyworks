# 입력 받아 파일 쓰기

f = open('input.txt', 'a')

text = input("저장할 내용을 입력해 주세요 : ")
f.write(text)
f.write('\n')
f.close