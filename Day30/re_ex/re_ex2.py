# '*'와 '+'의 차이
# * : 앞 문자가 0번 이상 반복도 찾음
# + : 앞 문자가 1번 이상 반복

import re

p = re.compile('ca*t')

m1 = re.findall(p, 'caat')
print(m1)

m2 = re.findall(p, "ct")
print(m2)

p2 = re.compile('ca*t')

m1 = re.findall(p2, "caat")
print(m1)

m2 = re.findall(p2, "ct")
print(m2)

