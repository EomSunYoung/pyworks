# 최고 점수
def find_max(a):    # 매개변수로 list가 전달
    max_v = a[0]    # 최대값을 0번 인덱스 기억
    for i in a:     # i = 70, 80, ...
        if max_v < i:
            max_v = i
    return max_v

# 최고 점수의 위치
def find_max_idx(a):
    max_idx = 0     # 위치로 0번을 기억
    n = len(a)
    for i in range(1, n):   # 반복 횟수 변수를 비교
        if a[max_idx] < a[i]:   #
            max_idx = i
    return max_idx

v = [70, 80, 55, 60, 90, 40]
print(find_max(v))
print(find_max_idx(v))

