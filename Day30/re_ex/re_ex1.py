# 정규 표현식
import re

# match() 함수 -> find()와 유사
p = re.compile("[a-z]+")    # [] : 매치되는 문자, + : 1번 이상 반복되는 문자
m = p.match('2021 python')  # match() : 첫글자부터 검색. 있으면 찾고, 없으면 none을 반환
print(m)

# search()
s = p.search('2021 python')  # search() 전체를 검색하므로 모두 찾음
print(s)

