# 마음대로 걷는 거북이

import turtle as t
import random

t.shape("turtle")
t.bgcolor("orange")
t.color("green")
t.speed(0)

for x in range(300):
    angle = random.randint(1, 360)  # 1~360도 랜덤한 각도

    t.setheading(angle)
    t.forward(10)
