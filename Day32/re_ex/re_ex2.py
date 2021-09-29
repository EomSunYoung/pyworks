# match() : 매치된 문자열을 돌려준다.

import re

p = re.compile('[a-z]+')
m = p.match("hello")

print(m)
print(m.group())
print(m.start())    # 시작 위치 0
print(m.end())      # 끝 위치 5
print(m.span())     # (0, 5)