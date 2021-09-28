# 예외 만들기 : 사용자가 직접 만들기
# Exception 클래스를 상속하여 만든다.

class MyError(Exception):
    # pass
    def __str__(self):  # 문자를 리턴해줌
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '레리아':
        raise MyError()     # Error를 발생시킴(미뤄놓음)
    print(nick)

# Error를 사용하는 곳에서 try ~ except 처리해야 함
try:
    say_nick('Reria')
    say_nick('Miz')
    say_nick('레리아')
except MyError as e:    # e : exception을 줄임
    # print("허용되지 않은 별명입니다.")
    print(e)