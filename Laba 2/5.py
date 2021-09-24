from random import randint
from math import sqrt
import turtle

#Рисуем рамку
turtle.width(3)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
turtle.goto(-300, -300)
turtle.goto(300, -300)
turtle.goto(300, 300)
turtle.goto(-300, 300)

#Генерируем параметры черепашек
number_of_turtles = 20
steps_of_time_number = 1000
coord = [[0] * 4 for i in range(number_of_turtles)]
counter = 0

for turtle_number in range(number_of_turtles):
    for i in range(2):
        coord[turtle_number][i] = randint(-280, 280)
        coord[turtle_number][i + 2] = randint(-10, 10)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(coord[counter][0], coord[counter][1])
    #unit.pendown()
    counter += 1



for i in range(steps_of_time_number):
    counter = 0
    for unit in pool:
        x_1 = coord[counter][0]
        y_1 = coord[counter][1]
        v_x_1 = coord[counter][2]
        v_y_1 = coord[counter][3]

        #Проверка на столкновение со стенкой
        if abs(x_1) >= 295:
            v_x_1 = -1 * v_x_1
            coord[counter][2] = v_x_1
        if abs(y_1) >= 295:
            v_y_1 = -1 * v_y_1
            coord[counter][3] = v_y_1
        #Проверка на столкновение с другой точкой
        for another_turtle_number in range(number_of_turtles):
            if another_turtle_number != counter:
                x_2 = coord[another_turtle_number][0]
                y_2 = coord[another_turtle_number][1]
                if sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2) <= 20:
                    v_x_2 = coord[another_turtle_number][2]
                    v_y_2 = coord[another_turtle_number][3]

                    #система до соударения
                    p_1 = [v_x_1, v_y_1] #Вектор импульса первой точки
                    p_2 = [v_x_2, v_y_2] #Вектор импульса второй точки
                    p = [x_2 - x_1, y_2 - y_1]#Направляющий вектор прямой, соединяющей точки
                    len_p = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
                    s = [p[0] / len_p, p[1] / len_p] #Единичный направляющий вектор
                    len_l_1 =(p_1[0] * p[0] + p_1[1] * p[1]) / len_p
                    l_1 = [s[0] * len_l_1, s[1] * len_l_1] #Проекция p1 на прямую
                    k_1 = [p_1[0] - l_1[0], p_1[1] - l_1[1]] #p1 - l1

                    len_l_2 =(p_2[0] * p[0] + p_2[1] * p[1]) / len_p
                    l_2 = [s[0] * len_l_2, s[1] * len_l_2] #Проекция p2 на прямую
                    k_2 = [p_2[0] - l_2[0], p_2[1] - l_2[1]] #p2 - l2

                    #Система после соударения
                    p_1 = [l_2[0] + k_1[0], l_2[1] + k_1[1]]
                    p_2 = [l_1[0] + k_2[0], l_1[1] + k_2[1]]

                    v_x_1 = p_1[0]
                    v_y_1 = p_1[1]
                    coord[another_turtle_number][2] = p_2[0]
                    coord[another_turtle_number][3] = p_2[1]

        unit.goto(x_1 + v_x_1, y_1 + v_y_1)
        coord[counter][0] = x_1 + v_x_1
        coord[counter][1] = y_1 + v_y_1
        coord[counter][2] = v_x_1
        coord[counter][3] = v_y_1
        counter += 1

