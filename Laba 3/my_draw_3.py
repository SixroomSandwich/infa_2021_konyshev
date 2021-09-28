import pygame
from pygame.draw import *

pygame.init()

FPS = 30
large = 1258
screen = pygame.display.set_mode((large, 500))

#Background
rect(screen, (135, 206, 235), (0, 0, large, 250))
rect(screen, (60, 179, 113), (0, 250, large, 250))

#Boy
for boy_number in range(2):
    #Переменные, отвечающие за симметрию
    a = (-1)**boy_number 
    b = boy_number * large
    
    ellipse(screen, (119, 136, 153), (a * 200 + b , 150, a * 100, 220))
    circle(screen, (255, 228, 196), (a * 250 + b, 120), 40)
    line(screen, (0, 0, 0), (a * 220 + b, 170), (a * 130 + b, 280))
    line(screen, (0, 0, 0), (a * 280 + b, 170), (a * 370 + b, 280))
    lines(screen, (0, 0, 0), False, [(a * 220 + b, 350), (a * 180 + b, 460), (a * 150 + b, 465)])
    lines(screen, (0, 0, 0), False, [(a * 280 + b, 345), (a * 300 + b, 460), (a * 330 + b, 460)])

#Girl    
for girl_number in range(2):
    #Переменные, отвечающие за симметрию
    a = (-1)**girl_number 
    b = girl_number * large
    
    polygon(screen, (255, 20, 147), [(a * 500 + b, 150), (a * 430 + b, 370), (a * 570 + b, 370)])
    circle(screen, (255, 228, 196), (a * 500 + b, 140), 40)
    line(screen, (0, 0, 0), (a * 490 + b, 185), (a * 370 + b, 280))
    lines(screen, (0, 0, 0), False, [(a * 510 + b, 185), (a * 570 + b, 215), (a * 630 + b, 190)])
    lines(screen, (0, 0, 0), False, [(a * 480 + b, 370), (a * 480 + b, 450), (a * 450 + b, 455)])
    lines(screen, (0, 0, 0), False, [(a * 520 + b, 370), (a * 520 + b, 450), (a * 550 + b, 450)])

#Balloon
line(screen, (0, 0, 0), (140, 280), (100, 175))
polygon(screen, (255, 0, 0), [(100, 175), (90, 105), (45, 140)])
circle(screen, (255, 0, 0), (70, 100), 20)
circle(screen, (255, 0, 0), (50, 120), 20)

#Ice cream 1
line(screen, (0, 0, 0), (630, 190), (640, 110))
polygon(screen, (255, 165, 0), [(640, 110), (660, 50), (620, 50)])
circle(screen, (255, 0, 0), (650, 35), 20)
circle(screen, (160, 82, 45), (630, 35), 20)
circle(screen, (255, 245, 238), (640, 20), 20)

#Ice cream 2
polygon(screen, (255, 165, 0), [(large - 140, 290), (large - 130, 220), (large - 85, 255)])
circle(screen, (255, 0, 0), (large - 110, 215), 20)
circle(screen, (160, 82, 45), (large - 90, 235), 20)
circle(screen, (255, 245, 238), (large - 90, 205), 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
