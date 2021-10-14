import pygame
from pygame.draw import *
from random import randint
from math import sqrt
import time

pygame.init()

FPS = 20
display_height = 900
display_width = 900
panel_height = 200
panel_width = 900

screen = pygame.display.set_mode((display_height, display_width))

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
    '''Функция обновляет экран (для стирания шариков и для отображения верхней панели)'''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, panel_width, panel_height))

    '''Здесь функция рисует текущий счёт игрока'''
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textsurface = myfont.render(str(score), False, BLACK)
    screen.blit(textsurface, (50, 25))

    '''Здесь функция отображает оставшиеся "жизни" игрока'''
    for life_num in range(3 - misses):
            draw_heart(screen, RED, panel_width // 2 + panel_width // 6 * life_num, panel_height // 4, panel_width // 9, panel_height // 9)

def draw_endgame_display(score):
    '''Функция рисует дисплей после проигрыша'''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, panel_width, panel_height))

    myfont = pygame.font.SysFont('Comic Sans MS', 45)
    
    text_letters = myfont.render("GAME OVER. YOU'R SCORE IS ", False, BLACK)
    screen.blit(text_letters, (50, 50))

    text_score = myfont.render(str(score), False, RED)
    screen.blit(text_score, (725, 50))
    
def draw_heart(surface, color, x, y, width, heigth):
    '''
    Функция рисует сердечко
    surface - объект pygame.Surface
    color - цвет сердечка
    x, y - координаты верхнего левого угла прямоугольнгика, в который вписано сердечко
    width, height - ширина и высота сердечка
    '''
    polygon(surface, color, [(x + 5, y + 25), (x + 50, y + 100), (x + 95, y + 25)])
    circle(surface, color, (x + 30, y + 25), 25)
    circle(surface, color, (x + 70, y + 25), 25)

def draw_ball(x, y, r):
    '''
    Рисует шарик 
    Цвет шарика зависит от его радиуса
    '''
    color = COLORS[r // 10 - 1]
    circle(screen, color, (x, y), r)

def new_coordinates():
    '''Функция отдаёт рандомные координаты, скорости и размеры для шариков'''
    coordinates = [0] * 5
    coordinates[0] = randint(109, display_width - 109)
    coordinates[1] = randint(panel_height + 109, display_height - 109)
    coordinates[2] = randint(5, 20)
    coordinates[3] = randint(5, 20)
    coordinates[4] = randint(10, 109)

    return coordinates

def ball_moving(x, y, v_x, v_y, r):
    '''
    Функция отдаёт новые координаты шарика и скорости, в зависимости от его скоростей и расположения относительно стенок
    '''
    if x + r >= display_width or x - r <= 0:
        v_x = -v_x
    x += v_x

    if y + r >= display_height or y - r <= panel_height:
        v_y = -v_y
    y += v_y

    return [x, y, v_x, v_y, r]

pygame.display.update()
clock = pygame.time.Clock()
finished = False


'''Переменные, отвечающие за кол-во набранных очков и за кол-во ошибок'''
score = 0
misses = 0

'''Переменные, отвечающие за время жизни шарика'''
max_life_time = 30
life_time = 0

draw_display(misses)
coordinates = new_coordinates()

while not finished:
    clock.tick(FPS)
    points = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or misses == 3:
            '''Игра заканчивается когда пользователь закрывает окно, или он три раза нажал не по кружочку'''
            time.sleep(1)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''Проверяем, кликнул ли пользователь внутрь шарика'''
            if sqrt((event.pos[0] - coordinates[0])**2 + (event.pos[1] - coordinates[1])**2) <= coordinates[4]:
                '''Считаем очки (чем меньше радиус шарика, по которому мы попали, тем больше очков)'''
                points = (119 - coordinates[4]) // 10
                print("Gotcha! +", points, "points!")
                score += points
            else:
                '''Если игрок кликнул, но не попал по кружочку, то кол-во его ошибок увеличивается на 1'''
                misses += 1

    draw_display(misses)
    
    if points != 0:
        coordinates = new_coordinates()
        draw_ball(coordinates[0], coordinates[1], coordinates[4])
        life_time = 0

    elif life_time == max_life_time:
        coordinates = new_coordinates()
        draw_ball(coordinates[0], coordinates[1], coordinates[4])
        misses += 1
        life_time = 0

    elif misses != 3:
        coordinates = ball_moving(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4]) 
        draw_ball(coordinates[0], coordinates[1], coordinates[4])
        life_time += 1
        pygame.display.flip()
    
    if misses == 3:
        draw_endgame_display(score)
        pygame.display.flip()
        time.sleep(5)
    
    pygame.display.flip()

pygame.quit()
