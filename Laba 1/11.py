import turtle as t
import math as m


def circle2(radius):
    t.speed("fastest")
    step_long = (2 * m.pi * radius) / 360
    for step in range(0, 360):
        t.forward(step_long)
        t.left(1)
    for step in range(0, 360):
        t.forward(step_long)
        t.right(1)

t.left(90)
for circle_num in range(0, 7):
    radius = 15 + 5 * circle_num
    circle2(radius)
