# try ~ except ~ else
# 오류가 없을 때는 try ~ else가 실행
# 오류가 있을 때는 try ~ except가 실행
# finally는 항상 실행 : 외부 장치를 초기화, 종료할 때 사용
try:
    print('1번')
    with open('animal.txt', 'r') as f:
        lines = f.readlines()

except:
    print('2번')

else:
    print('3번')
    for i in lines:
        print(i, end='')

finally:
    print('4번')