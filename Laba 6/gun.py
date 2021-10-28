import math
from random import choice
from random import randint as rnd

import pygame


bullets = 10
death_counter = 0
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 800


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.timer = 0
        self.death_timer = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x >= 800:
            self.vx = -self.vx
        if self.y >= 750:
            if abs(self.vy) <= 5:
                self.vy = 0
            self.vy = -self.vy // 2
            self.vx = self.vx // 2
            self.y = 750

        self.vy -= 5

        if abs(self.vx) <= 5:
            self.vx = 0

        self.x += self.vx
        self.y -= self.vy


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullets
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        bullets -= 1
        print(bullets , "bullets left")

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        pygame.draw.line(self.screen, self.color, [20, 450], [20 + self.f2_power * math.cos(self.an), 450 + self.f2_power * math.sin(self.an)], 3)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            if self.f2_power <= 40:
                self.color = GREEN
            elif self.f2_power <= 70:
                self.color = YELLOW
            else:
                self.color = RED
        else:
            self.color = GREY

class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()
    

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(300, 680)
        y = self.y = rnd(250, 600)
        r = self.r = rnd(10, 50)
        color = self.color = RED
        self.live = 1
        vx = self.vx = (-1)**(2 % rnd(1, 2)) * rnd(5, 15)
        vy = self.vy = (-1)**(2 % rnd(1, 2)) * rnd(5, 15)

    def move(self):
        if self.x + self.r >= 750 or self.x - self.r<= 200:
            self.vx = -self.vx

        if self.y + self.r >= 700 or self.y - self.r <= 200:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy

    def hit(self, points = 1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

def draw_display():
    pygame.draw.line(screen, BLACK, (0, 195), (800, 195))
    '''Пишем кол-во очков, набранные игроком'''
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    text_score = myfont.render(str(score), False, BLACK)
    screen.blit(text_score, (50, 25))
    '''Пишем оставшееся кол-во пуль'''
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    text_bullets = myfont.render("Bullets: ", False, BLACK)
    screen.blit(text_bullets, (250, 25))

    text_bullets_num = myfont.render(str(bullets), False, BLACK)
    screen.blit(text_bullets_num, (450, 25))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
score = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target(screen)
target_2 = Target(screen)
finished = False

while (not finished) and death_counter < 10:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()

    draw_display()
    pygame.display.update()

    clock.tick(FPS)
    if bullets != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)

    for b in balls:
        b.move()
        if abs(b.vx) <= 1 and b.y >= 550:
            b.death_timer += 1
            if b.death_timer >= 10 and b.color != WHITE:
                b.color = WHITE
                death_counter += 1

        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1.new_target()
            score += 1

        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
            score += 1

    target_1.move()
    target_2.move()

    gun.power_up()

pygame.quit()
