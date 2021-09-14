# 1번
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(6))

# 2번
def avg_numbers(*args):
    result = 0  # 합계
    for i in args:
        result += i
    return result / len(args)   # 평균 = 합계 / 개수

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# 3번
input1 = input("첫번째 숫자를 입력하세요 : ")
x = int(input1)
input2 = input("두번째 숫자를 입력하세요 : ")
y = int(input2)

# total = int(input1) + int(input2)
total = x + y
print("두 수의 합은 %s 입니다." % total)

# 4번
print("you""need""python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
# join() : 리스트 요소를 문자열로 바꿈

# 5번
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close

f2 = open("test.txt", 'r')
print(f2.read())
f2.close
"""

with open("test.txt", 'w') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r') as f2:
    print(f2.read())

# 6번
user_input = input("저장할 내용을 입력하세요 : ")
f = open("test2.txt", 'a')
f.write(user_input)
f.write('\n')
f.close