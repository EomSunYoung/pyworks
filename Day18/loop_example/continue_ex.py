# 반복문 : continue
# 1 ~ 10 중 5만 제외 출력
# 반복하다 조건에 맞으면 수행문을 처리하지 않고 다시 반

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 1 ~ 10 중 짝수 출력
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
