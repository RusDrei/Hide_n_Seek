import pygame
import random
import os

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, hide_or_seek):
        pygame.sprite.Sprite.__init__(self)
        if hide_or_seek == 'H':
            self.img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
            self.img_m = pygame.image.load(os.path.join(img_folder, 'p1_jump_m.png')).convert()
            self.image = self.img

            self.image.set_colorkey(BLACK)
            self.rect = self.img.get_rect()
            self.rect.center = (1830, 90)
        elif hide_or_seek == 'S':
            self.img = pygame.image.load(os.path.join(img_folder, 'seek.png')).convert()
            self.img_m = pygame.image.load(os.path.join(img_folder, 'seek_m.png')).convert()

            self.image = self.img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = (90, 990)
        self.looking_dir = 1

    def update(self):
        keystate = pygame.key.get_pressed()
        cur_x = self.rect.x

        if keystate[pygame.K_a]:
            self.rect.x += -6
        if keystate[pygame.K_d]:
            self.rect.x += 6
        if keystate[pygame.K_w]:
            self.rect.y += -6
        if keystate[pygame.K_s]:
            self.rect.y += 6

        if self.rect.x - cur_x != 0:
            self.looking_dir = 1 if self.rect.x - cur_x > 0 else -1
            if self.looking_dir == 1:
                self.image = self.img
            elif self.looking_dir == -1:
                self.image = self.img_m

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# class Seek(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.seek_img = pygame.image.load(os.path.join(img_folder, 'seek.png')).convert()
#         self.seek_img_m = pygame.image.load(os.path.join(img_folder, 'seek_m.png')).convert()
#
#         self.image = self.seek_img
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.center = (90, 990)
#
#         self.looking_dir = 1
#
#     def update(self):
#         keystate = pygame.key.get_pressed()
#
#         cur_x = self.rect.x
#         if keystate[pygame.K_LEFT]:
#             self.rect.x += -6
#         if keystate[pygame.K_RIGHT]:
#             self.rect.x += 6
#         if keystate[pygame.K_UP]:
#             self.rect.y += -6
#         if keystate[pygame.K_DOWN]:
#             self.rect.y += 6
#
#         if self.rect.x - cur_x != 0:
#             self.looking_dir = 1 if self.rect.x - cur_x > 0 else -1
#             if self.looking_dir == 1:
#                 self.image = self.seek_img
#             elif self.looking_dir == -1:
#                 self.image = self.seek_img_m
#
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0
#         if self.rect.top < 0:
#             self.rect.top = 0
#         if self.rect.bottom > HEIGHT:
#             self.rect.bottom = HEIGHT


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("nedopackman")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

# Цикл игры
running = True
hide = Player('H')
seek = Player('S')

all_sprites.add(seek)
all_sprites.add(hide)
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
