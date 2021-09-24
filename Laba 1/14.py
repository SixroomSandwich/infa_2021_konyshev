import turtle as t

def star(star_num):
    figure_angle = (180 * (star_num - 2)) / star_num
    star_angle = 360 / star_num
    t.left(180)
    for side_num in range(0, star_num):
        t.forward(100)
        t.left(180 - star_angle)

t.penup()
t.goto(-200, 0)
t.pendown()
star(5)

t.penup()
t.goto(100, 0)
t.pendown()
star(11)
        
