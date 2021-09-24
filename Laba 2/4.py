import turtle as t
from math import sqrt

def new_coord(x, y, Vx, Vy, time):
    dt = 0.05
    time += dt
    ay = -9.81
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    new_coordinates = [0] * 5
    new_coordinates[0] = x
    new_coordinates[1] = y
    new_coordinates[2] = Vx
    new_coordinates[3] = Vy
    new_coordinates[4] = time
    return new_coordinates


coord = [0] * 5
coord[0] = -250
t.goto(250, 0)
t.goto(coord[0], 0)
coord[2] = 20
coord[3] = 50

while coord[4] < 25:
    if coord[1] > 0 or coord[3] > 0 or coord[4] == 0:
        coord = new_coord(coord[0], coord[1], coord[2], coord[3], coord[4])
        t.goto(coord[0], coord[1])
    else:
        coord[3] = (-1) * (coord[3] / sqrt(2))
        coord = new_coord(coord[0], coord[1], coord[2], coord[3], coord[4])
        t.goto(coord[0], coord[1])
