# 이름과 전화번호를 분리해서 추출하기
# 그루핑된 문자열에 이름 붙이기 : (?P<그룹이름>)
import re

str = "jang 010-1234-5678"
p = re.compile('[0-9A-Za-z]+')   # [0-9A-Za-z]


m = p.search(str)
print(m.group())
