import pygame
from pygame.draw import *
from random import randint
from math import sqrt
import time

pygame.init()

FPS = 2
screen = pygame.display.set_mode((900, 900))

'''Добавляем цвета'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLORS = [DARK_VIOLET, BLUE_VIOLET, MEDIUM_PURPLE, MEDIUM_ORCHID, MAGENTA, ORCHID, VIOLET, PLUM, THISTLE, LAVENDER]

def draw_display(misses):
    '''Функция обновляет экран (для стирания шариков и для отображения верхней панели)'''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, 900, 200))

    '''Здесь функция рисует текущий счёт игрока'''
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textsurface = myfont.render(str(score), False, BLACK)
    screen.blit(textsurface, (50, 25))

    '''Здесь функция отображает оставшиеся "жизни" игрока'''
    for life_num in range(3 - misses):
            draw_heart(screen, RED, 450 + 150 * life_num, 50, 100, 100)

def draw_endgame_display(score):
    '''Функция рисует дисплей после проигрыша'''
    screen.fill(BLACK)
    rect(screen, WHITE, (0, 0, 900, 200))

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

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 900)
    y = randint(300, 900)
    r = randint(10, 109)
    '''Цвет шарика зависит от его радиуса'''
    color = COLORS[r // 10 - 1]
    circle(screen, color, (x, y), r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


'''Переменные, отвечающие за кол-во набранных очков и за кол-во ошибок'''
score = 0
misses = 0
exist = 1
maximum = 1

draw_display(misses)

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or misses == 3:
            '''Игра заканчивается когда пользователь закрывает окно, или он три раза нажал не по кружочку'''
            time.sleep(1)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''Проверяем, кликнул ли пользователь внутрь шарика'''
            if sqrt((event.pos[0] - x)**2 + (event.pos[1] - y)**2) <= r:
                '''Считаем очки (чем меньше радиус шарика, по которому мы попали, тем больше очков)'''
                points = (119 - r) // 10
                print("Gotcha! +", points, "points!")
                score += points
            else:
                '''Если игрок кликнул, но не попал по кружочку, то кол-во его ошибок увеличивается на 1'''
                misses += 1

    draw_display(misses)
    
    if misses != 3:
        new_ball()
        pygame.display.flip()
    else:
        draw_endgame_display(score)
        pygame.display.flip()
        time.sleep(5)
    
    pygame.display.flip()

pygame.quit()
