import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))

#Background
rect(screen, (135, 206, 235), (0, 0, 800, 250))
rect(screen, (60, 179, 113), (0, 250, 800, 250))

#Boy
ellipse(screen, (119, 136, 153), (200, 150, 100, 220))
circle(screen, (255, 228, 196), (250, 120), 40)
line(screen, (0, 0, 0), (220, 170), (130, 280))
line(screen, (0, 0, 0), (280, 170), (370, 280))
lines(screen, (0, 0, 0), False, [(220, 350), (180, 460), (150, 465)])
lines(screen, (0, 0, 0), False, [(280, 345), (300, 460), (330, 460)])

#Girl
polygon(screen, (255, 20, 147), [(500, 150), (430, 370), (570, 370)])
circle(screen, (255, 228, 196), (500, 140), 40)
line(screen, (0, 0, 0), (490, 185), (370, 280))
lines(screen, (0, 0, 0), False, [(510, 185), (570, 215), (630, 190)])
lines(screen, (0, 0, 0), False, [(480, 370), (480, 450), (450, 455)])
lines(screen, (0, 0, 0), False, [(520, 370), (520, 450), (550, 450)])

#Ice cream
polygon(screen, (255, 165, 0), [(140, 290), (130, 220), (85, 255)])
circle(screen, (255, 0, 0), (110, 215), 20)
circle(screen, (160, 82, 45), (90, 235), 20)
circle(screen, (255, 245, 238), (90, 205), 20)

#Balloon
line(screen, (0, 0, 0), (620, 210), (690, 110))
polygon(screen, (255, 0, 0), [(690, 110), (750, 70), (685, 45)])
circle(screen, (255, 0, 0), (735, 60), 20)
circle(screen, (255, 0, 0), (703, 45), 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
