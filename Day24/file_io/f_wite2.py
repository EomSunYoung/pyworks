# 숫자 포매팅으로 파일 쓰기
f = open("c:/pyfile/number.txt", 'w')
f.write("%d\n" % (100*2))

f.close()