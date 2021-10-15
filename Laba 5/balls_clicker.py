import pygame
from pygame.draw import *
from random import randint
from math import sqrt
import time

pygame.init()

'''Переменные, связанные с параметрами экрана и  скоростью программы'''
FPS = 30
display_height = 900
display_width = 900
panel_height = 200
panel_width = 900

'''Переменные, отвечающие за кол-во набранных очков и за кол-во ошибок'''
score = 0
misses = 0
misses_flag = 0
gotcha_flag = 0

'''Кол-во одновременно существующих шариков'''
balls_number = 2

'''Переменные, отвечающие за время жизни шарика'''
max_life_time = 100
life_time = [0] * balls_number
deth_counter = [0] * balls_number

'''Добавляем цвета'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

'''Цвета для шариков'''
DARK_VIOLET = (148, 0, 211)
BLUE_VIOLET = (138, 43, 226)
MEDIUM_PURPLE = (147, 112, 219)
MEDIUM_ORCHID = (186, 85, 211)
MAGENTA = (255, 0, 255)
ORCHID = (218, 112, 214)
VIOLET = (238, 130, 238)
PLUM = (221, 160, 221)
THISTLE = (216, 191, 216)
LAVENDER = (230, 230, 250)

COLORS = [DARK_VIOLET, BLUE_VIOLET, MEDIUM_PURPLE, MEDIUM_ORCHID, MAGENTA, ORCHID, VIOLET, PLUM, THISTLE, LAVENDER]

def draw_display(misses):
    '''
    Функция обновляет экран (стирает шарики и рисует верхнюю панель)
    misses - кол-во ошибок (кол-во жизней = 3 - кол-во ошибок)
    '''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, panel_width, panel_height))

    '''Здесь функция рисует текущий счёт игрока'''
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textsurface = myfont.render(str(score), False, BLACK)
    screen.blit(textsurface, (50, 25))

    '''Здесь функция рисует оставшиеся "жизни" игрока'''
    for life_num in range(3 - misses):
            draw_heart(screen, RED, panel_width // 2 + panel_width // 6 * life_num, panel_height // 4, panel_width // 9, panel_height // 2)

def draw_endgame_display(score):
    '''
    Функция рисует экран после проигрыша
    score - кол-во очков, набранное игроком за игру
    '''
    '''Рисует чёрный экран и белую панель сверху'''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, panel_width, panel_height))

    '''Пишет прощальную фразу и счёт'''
    myfont = pygame.font.SysFont('Comic Sans MS', 45)
    
    text_letters = myfont.render("GAME OVER. YOU'R SCORE IS ", False, BLACK)
    screen.blit(text_letters, (50, 50))

    text_score = myfont.render(str(score), False, RED)
    screen.blit(text_score, (725, 50))
    
def draw_heart(surface, color, x, y, width, height):
    '''
    Функция рисует сердечко
    surface - объект pygame.Surface
    color - цвет сердечка
    x, y - координаты верхнего левого угла прямоугольнгика, в который вписано сердечко
    width, height - ширина и высота сердечка
    '''
    polygon(surface, color, [(x + width // 20, y + height // 4), (x + width // 2, y + height), (x + width * 19 // 20, y + height // 4)])
    circle(surface, color, (x + width * 3 // 10, y + height // 4), width // 4)
    circle(surface, color, (x + width * 7 // 10, y + height // 4), width // 4)

def draw_ball(x, y, r, kind):
    '''
    Рисует шарик 
    x, y - координаты центра шарика
    r - радиус шарика
    Цвет шарика зависит от его радиуса
    '''
    if kind == 0:
        color = COLORS[r // 10 - 1]
        circle(screen, color, (x, y), r)
    else:
        draw_heart(screen, RED, x - r, y - r, 2 * r, 2 * r)

def new_coordinates():
    '''
    Функция отдаёт рандомные координаты, скорости и размеры для шариков
    На выходе отдаёт массив из шести эллементов:
    0, 1 эллементы - координаты центра шарика x, y
    2,3 эллементы - скорости вдоль каждой оси v_x, v_y
    4 эллемент - радиус шарика r
    5 эллемент - явлеяется ли шарик сердечком. 0 - если он шарик, 1 - если сердечко
    '''
    coordinates = [0] * 6
    coordinates[0] = randint(109, display_width - 109)
    coordinates[1] = randint(panel_height + 109, display_height - 109)
    coordinates[2] = (-1) ** randint(0, 1) * randint(5, 10)
    coordinates[3] = (-1) ** randint(0, 1) * randint(5, 10)
    
    coordinates[5] = randint(2, 11) // 10
    if coordinates[5] == 1:
        coordinates[4] = 40
    else:
        coordinates[4] = randint(10, 109)

    return coordinates

def ball_moving(x, y, v_x, v_y, r, kind):
    '''
    Функция отдаёт новые координаты шарика и скорости, в зависимости от его скоростей и расположения относительно стенок
    '''
    if x + r >= display_width or x - r <= 0:
        v_x = -v_x
    x += v_x

    if y + r >= display_height or y - r <= panel_height:
        v_y = -v_y
    y += v_y

    return [x, y, v_x, v_y, r, kind]

def read_file(file_name):
    file = [] * 10
    inp = open(file_name, encoding = 'utf8')
    lines = inp.read().split('\n')
    for each_line in lines:
        file.append(str(each_line))
    inp.close()
    return file

screen = pygame.display.set_mode((display_height, display_width))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
draw_display(misses)

'''Задаем параметры для всех шариков'''
coordinates = [[0] * 6 for i in range(balls_number)]
for num in range(balls_number):
    coordinates[num] = new_coordinates()

'''Начинаем играть'''
while not finished:
    clock.tick(FPS)
    points = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or misses == 3:
            '''Игра заканчивается когда пользователь закрывает окно, или он три раза нажал не по кружочку'''
            time.sleep(1)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for num in range(balls_number):
                '''Проверяем, кликнул ли пользователь внутрь сердечка'''
                if coordinates[num][5] == 1 and abs(event.pos[0] - coordinates[num][0]) <= coordinates[num][4] and abs(event.pos[1] - coordinates[num][1] <= coordinates[num][4]):
                    '''Если было нажато сердечко, то отмечаем смерть сердечка числом 2'''
                    deth_counter[num] = 2
                    gotcha_flag = 1
                elif coordinates[num][5] == 0 and sqrt((event.pos[0] - coordinates[num][0])**2 + (event.pos[1] - coordinates[num][1])**2) <= coordinates[num][4]:
                    '''Считаем очки (чем меньше радиус шарика, по которому мы попали, тем больше очков)'''
                    points = (119 - coordinates[num][4]) // 10
                    print("Gotcha! +", points, "points!")
                    score += points
                    '''В специальном массиве отмечаем смерть шарика с номеров num'''
                    deth_counter[num] = 1
                    '''
                    Фиксируем попадание по одному из шариков (В дальнейшем это используется, чтобы понять, что игрок попал по шарику,
                    так как для других шариков программа зафиксирует промах)
                    '''
                    gotcha_flag = 1
                else:
                    '''
                    Если игрок кликнул, но не попал по кружочку, то мы фиксируем, что в этом цикле была совершенна ошибка 
                    (Делаем так, а не просто misses += 1, чтобы за одну ошибку программа не отнимала кол-во жизней, равное balls_number)
                    '''
                    misses_flag = 1

    '''Проверяем, была ли совершенна ошибка, если да, то отнимаем жизнь'''
    if gotcha_flag == 0 and misses_flag == 1:
        misses += 1
    misses_flag = 0
    gotcha_flag = 0

    draw_display(misses)
    for num in range(balls_number):    
        if deth_counter[num] != 0:
            '''Проверяем, попал ли игрок по сердечку, если да, то даём ему жизнь, максимум 3'''
            if deth_counter[num] == 2 and misses > 0:
                misses -= 1
            '''Игрок попал по шарику, создаётся новый шарик'''
            coordinates[num] = new_coordinates()
            for i in range(balls_number):
                if num != 1 and coordinates[i][5] == 1:
                    coordinates[num][5] = 0
            draw_ball(coordinates[num][0], coordinates[num][1], coordinates[num][4], coordinates[num][5])
            '''Так же продлевается время жизни оставшихся шариков'''
            for i in range(balls_number):
                if i != num:
                    life_time[i] -= max_life_time // 5
            life_time[num] = 0
            deth_counter[num] = 0

        elif life_time[num] == max_life_time:
            '''шарик умирает, у игрока теряется жизнь'''
            coordinates[num] = new_coordinates()
            for i in range(balls_number):
                if num != 1 and coordinates[i][5] == 1:
                    coordinates[num][5] = 0
            draw_ball(coordinates[num][0], coordinates[num][1], coordinates[num][4], coordinates[num][5])
            if coordinates[num][5] == 0:
                misses += 1
            life_time[num] = 0

        elif misses != 3:
            '''Шарик перемещается'''
            coordinates[num] = ball_moving(coordinates[num][0], coordinates[num][1], coordinates[num][2], coordinates[num][3], coordinates[num][4], coordinates[num][5]) 
            draw_ball(coordinates[num][0], coordinates[num][1], coordinates[num][4], coordinates[num][5])
            life_time[num] += 1
            pygame.display.flip()
            
    '''Игра заканчивается, если у игрока не остаётся жизней'''
    if misses >= 3:

        draw_endgame_display(score)
        pygame.display.flip()
        time.sleep(5)
            
    pygame.display.flip()

'''Здесь программа записывает счёт в общий рейтинг'''
file = read_file('top.txt')
top = [0] * 10
for i in range(10):
    a = int(file[i])
    top[i] = a

for i in range(10):
    if score >= top[i]:
        smth = score
        score = top[i]
        top[i] = smth

print(top)

out = open('top.txt', 'w')
for i in range(9):
    out.write(str(top[i]) + '\n')

out.write(str(top[9]))
out.close()

print('Noted')

pygame.quit()
