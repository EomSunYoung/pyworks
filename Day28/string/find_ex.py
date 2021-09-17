# find() 함수 : 문자열을 찾는(검색)하는 함수
# 인덱스(위치)를 반환

str = "Hello"
x = str.find('H')
print(x)    # 0 찾음

x = str.find('ll')
print(x)

x = str.find('m')
print(x)

if x >= 0:
    print("찾음")
else:
    print("찾는 문자가 없음")