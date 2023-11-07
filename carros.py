import os.path
import pygame
import random


def sprite_loader(path):
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()


RED_CAR = {0: 'assets/carro_vermelho_direita.png', 1: 'assets/carro_vermelho_direita2.png'}
YELLOW_CAR = {0: 'assets/carro_amarelo_direita.png', 1: 'assets/carro_amarelo_direita2.png'}
BLUE_CAR = {0: 'assets/carro_azul_direita.png', 1: 'assets/carro_azul_direita2.png'}
PURPLE_CAR = {0: 'assets/carro_roxo_direita.png', 1: 'assets/carro_roxo_direita2.png'}
CARS_IMG = [RED_CAR, YELLOW_CAR, BLUE_CAR, PURPLE_CAR]


class Carro(pygame.sprite.Sprite):
    def __init__(self, *groups, character, pos_x, pos_y, horizontal=False, vertical=False):
        super().__init__(*groups)

        self.speed = 10
        self.starting_x = pos_x
        self.starting_y = pos_y
        self.horizontal = horizontal
        self.vertical = vertical
        self.direction = self.starting_direction()
        self.character = character
        self.current_sprite = 0
        self.rng_aux = random.randint(0, 3)
        self.sprite = self.change_sprite()
        self.image = pygame.transform.scale(self.sprite, [self.sprite.get_width()*1.2, self.sprite.get_height()*1.8])
        self.rect = pygame.Rect(self.starting_x, self.starting_y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.move()
        self.change_sprite()

        if self.rect.x > 1100 and self.direction == 'lr':
            self.reset_position()
        if self.rect.x < -100 and self.direction == 'rl':
            self.reset_position()
        if self.rect.y > 900 and self.direction == 'tb':
            self.reset_position()
        if self.rect.y < -100 and self.direction == 'bt':
            self.reset_position()

        self.detect_collision()

    def move(self, backwards=False):
        if self.horizontal and self.vertical:
            print('Apenas uma direção deve ser verdadeira.')
            return

        if self.direction == 'rl' or self.direction == 'bt':
            backwards = True

        if self.horizontal:
            if not backwards:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        if self.vertical:
            if not backwards:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

    def reset_position(self):
        self.rect.x = self.starting_x
        self.rect.y = self.starting_y
        self.sprite = self.change_sprite(True)

    def starting_direction(self):
        if self.starting_x >= 1000:
            return 'rl'

        if self.starting_x <= 0:
            return 'lr'

        if self.starting_y >= 800:
            return 'bt'

        if self.starting_y <= 0:
            return 'tb'

    def change_sprite(self, change_car=False):
        rng = random.randint(0, 3)
        if change_car:
            self.rng_aux = rng
        if self.current_sprite >= len(CARS_IMG[self.rng_aux])-1:
            self.current_sprite = 0
        self.current_sprite += 0.1
        car = CARS_IMG[self.rng_aux][int(self.current_sprite)]
        if self.direction == 'rl' or self.direction == 'bt':
            car = car.replace('direita', 'esquerda')
        self.sprite = sprite_loader(car)
        self.image = pygame.transform.scale(self.sprite, (self.sprite.get_width()*1.2, self.sprite.get_height()*1.8))
        return self.sprite

    def detect_collision(self):
        for _ in pygame.sprite.spritecollide(self, self.character, False):
            self.character.sprites()[0].rect.x = 360
            self.character.sprites()[0].rect.y = 370
            self.character.sprites()[0].life -= 1
