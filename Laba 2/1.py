import turtle as t
from random import *

t.speed(10)
t.color('red')
for move_number in range(50):
    t.forward(randint(1, 50))
    t.left(randint(1, 360))
