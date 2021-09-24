import turtle as t
import math as m

def figure(n, radius):
    if n < 3:
        print("Не существует фигур, с кол-вом сторон, меньше 3")
        return
    angle = 360 / n
    angle_rad = (angle * 2 * m.pi) / 360
    side_long = radius * m.sqrt(2 * (1 - m.cos(angle_rad)))
    t.left(angle + (180 - angle) / 2)
    for side in range (0, n):
        t.forward(side_long)
        t.left(angle)
    t.right(angle + (180 - angle) / 2)


for figure_number in range (3, 13):
    radius = 10 * (figure_number - 2)
    t.penup()
    t.goto(radius, 0)
    t.pendown()
    figure(figure_number, radius) 
        
