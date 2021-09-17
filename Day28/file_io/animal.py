with open('animal.txt', 'w') as f:
    animal = ['dog', 'cat', 'horse', 'cow']

    for i in animal:
        f.write(i + '\n')
f.close()

with open('animal.txt', 'r') as f:
    # line = f.readline()     # 한줄 읽기
    # print(line)

    lines = f.readlines()
    print(lines)

    for i in lines:
        print(i, end='')

# 2차원 리스트로 만들기
animal = []
for i in lines:
    # animal.append([i])
    animal.append(i[0:-1])
print(animal)