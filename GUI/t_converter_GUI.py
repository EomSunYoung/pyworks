# 온도 변환기 - 완성
from tkinter import *
from GUI.converter import Converter

class App:
    def __init__(self, root):
        self.con = Converter('C', 'F', 1.8, 32)
        frame = Frame(root)
        frame.pack()

        Label(frame, text="dog C").grid(row=0, column=0)
        self.c = DoubleVar()    # 실수형 자료를 c 변수에 저장
        Entry(frame, width=10, textvariable=self.c).grid(row=0, column=1)

        Label(frame, text="dog F").grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1)    # 출력

        Button(frame, text="변환", command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get()    # 입력된 섭씨 온도 가져오기
        con_f ="{0: .2f}".format(self.con.convert(c))
        self.f.set(con_f)

root = Tk()
root.title("온도 변환기")
root.geometry('250x100+200+200')
app = App(root)

root.mainloop()
