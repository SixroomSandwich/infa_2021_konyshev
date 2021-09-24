import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (255, 255, 255), (0, 0, 500, 500))

circle(screen, (255, 255, 0), (250, 250), 150)
circle(screen, (0, 0, 0), (250, 250), 150, 1)

circle(screen, (255, 0, 0), (180, 220), 30)
circle(screen, (0, 0, 0), (180, 220), 30, 1)
circle(screen, (0, 0, 0), (180, 220), 12)

circle(screen, (255, 0, 0), (320, 220), 25)
circle(screen, (0, 0, 0), (320, 220), 25, 1)
circle(screen, (0, 0, 0), (320, 220), 12)

rect(screen, (0, 0, 0), (180, 320, 140, 30))

polygon(screen, (0, 0, 0), [[130, 127], [220, 217],[230, 207], [140, 117]])
polygon(screen, (0, 0, 0), [[400, 170], [280, 210], [275, 197], [395, 157]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()



