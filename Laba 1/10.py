import turtle as t
import math as m


def circle(radius):
    t.speed("fastest")
    step_long = (2 * m.pi * radius) / 360
    for step in range(0, 360):
        t.forward(step_long)
        t.left(1)
    for step in range(0, 360):
        t.forward(step_long)
        t.right(1)

radius = 30
for circle_num in range(0, 3):
    circle(radius)
    t.left(60)
