# 학생 클래스
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("학생이 배웁니다.")

    def __str__(self):
        return "이름 : {0}, 학년 : {1}".format(self.name, self.grade)

# 인스턴스 = 생성자()
s1 = Student("흥부", 2)
print(s1)
s1.learn()

s2 = Student("놀부", 1)
print(s2)
s2.learn()

