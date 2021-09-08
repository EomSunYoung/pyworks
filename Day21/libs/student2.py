# 접근 제한 - 멤버(private), 함수(public)
# 접근하는 방법 - get + 멤버 이름 (), set + 멤버 이름 ()
import random

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def learn(self):
        print("학생이 배웁니다.")

    def getname(self):
        return self._name

    def setgrade(self, grade):
        self._grade = grade

    def getgrade(self):
        return self._grade


    """
    def __str__(self):  # 객체의 정보 출력
        return "이름 : {0}, 학년 : {1}".format(self.name, self.grade)
    """

s1 = Student("흥부")
print("이름 :", s1.getname())
print("학년 :", s1.getgrade())

