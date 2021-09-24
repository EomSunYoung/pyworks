# findall() 함수 - 내용을 리스트로 변환
import re

str = "Two is too"
m1 = re.findall("T[ow]o", str)
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE)   # 대, 소문자 허용
print(m2)

m3 = re.findall("T[^w]o", str, re.IGNORECASE)
print(m3)

pat = re.compile("T[^o]o")
m3 = re.findall(pat, str)
print(m3)