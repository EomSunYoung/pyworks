# 시간 추측 게임

import time

input("엔터를 누르고 20초를 셉니다.")  # input()이 엔터임
start = time.time()     # 1970. 01. 01 자정 이후로 지금까지 초로 환산한 시간

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end-start
print("실제 시간 : %f초" % (et))
print("차이 : %.2f초" % abs(et-20))
