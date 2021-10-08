import pygame
from pygame.draw import *
from random import randint
from math import sqrt
pygame.init()

FPS = 2
screen = pygame.display.set_mode((900, 900))

'''Добавляем цвета'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

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
    color = COLORS[randint(0, 5)]
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
            print("You're score is ", score)
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
    '''
    if exist < maximum:
        new_ball()
    '''
    new_ball()
    pygame.display.update()
    

pygame.quit()
