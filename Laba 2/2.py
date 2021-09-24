import turtle as t
from math import sqrt

def number(num):
    
    for lenth, angle in d_font[num]:
        t.left(angle)
        t.forward(lenth)
        
    t.penup()
    for lenth, angle in d_font[num][::-1]:
        t.backward(lenth)
        t.right(angle)
    t.pendown()
    
L1 = 30
L2 = sqrt(2) * L1
L3 = 2 * L1

d0 = [(L1, 180), (L3, 90), (L1, 90), (L3, 90)]
d1 = [(L2, -135), (L2, 180), (L3, -135)]
d2 = [(L1, 180), (L1, 180), (L1, -90), (L2, -45), (L1, 135)]
d3 = [(L1, 180), (L1, 180), (L2, -135), (L1, 135), (L2, -135)]
d4 = [(L3, -90), (L1, 180), (L1, 90), (L1, -90)]
d5 = [(L1, 180), (L1, 90), (L1, 90), (L1, -90), (L1, -90)]
d6 = [(L2, -135), (L1, 45), (L1, 90), (L1, 90), (L1, 90)]
d7 = [(L1, 180), (L1, 180), (L2, -135), (L1, 45)]
d8 = [(L1, 180), (L3, 90), (L1, 90), (L1, 90), (L1, 90), (L1, 180), (L1, 90)]
d9 = [(L1, 180), (L1, 90), (L1, 90), (L1, 90), (L1, 180), (L2, -45)]
    
d_font = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

line = input()

t.speed(10)
t.width(3)

t.penup()
t.goto(-1 * (len(line) // 2) * L3, 0)
t.pendown()

for counter in range(len(line)):
    number(int(line[counter]))
    t.penup()
    t.forward(L3)
    t.pendown()

