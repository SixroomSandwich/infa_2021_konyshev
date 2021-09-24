import turtle as t
from math import sqrt

def number(num):
    
    for lenth, angle in font[num]:
        t.left(angle)
        t.forward(lenth)
        
    t.penup()
    for lenth, angle in font[num][::-1]:
        t.backward(lenth)
        t.right(angle)
    t.pendown()
    

L1 = 30
L2 = sqrt(2) * L1
L3 = 2 * L1

chislo = input()

font = [] * 10

def read_file(file_name):
    input = open(file_name, encoding = 'utf8')
    lines = input.read().split('\n')
    for each_line in lines:
        font.append(eval(each_line))

t.speed(10)
t.width(3)

t.penup()
t.goto(-1 * (len(chislo) // 2) * L3, 0)
t.pendown()

read_file('font.txt')

for counter in range(len(chislo)):
    number(int(chislo[counter]))
    t.penup()
    t.forward(L3)
    t.pendown()
