import turtle as t
import math as m

def arc(radius):
    t.speed('fastest')
    step_long = (2 * m.pi * radius) / 360
    for step in range(0, 180):
        t.forward(step_long)
        t.right(1)

t.penup()
t.goto(-150, 0)
t.pendown()
t.left(90)
for arc_num in range(0, 9):
    if arc_num % 2 == 0:
        arc(30)
    else:
        arc(5)
