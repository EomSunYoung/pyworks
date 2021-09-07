# exercise - 제어문
# 1번

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# 2번
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:  # 3으로 나누어 떨어지면 
        result += i # 누적 합계
    i += 1
print(result)

# 3번
i = 0
while True:
    i += 1
    if i > 5:
        break
    print('*'*i)
print()

for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end='')
    print()

# 4번
for i in range(1, 101):
    print(i)
