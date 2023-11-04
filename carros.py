import os.path
import pygame


def sprite_loader(path):
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()


class Carro(pygame.sprite.Sprite):
    def __init__(self, *groups, character, pos_x, pos_y, horizontal=False, vertical=False):
        super().__init__(*groups)

        self.sprites = [sprite_loader('assets/test_block.png')]
        self.speed = 10
        self.starting_x = pos_x
        self.starting_y = pos_y
        self.horizontal = horizontal
        self.vertical = vertical
        self.character = character
        self.image = pygame.transform.scale(self.sprites[0], [50, 50])
        self.rect = pygame.Rect(self.starting_x, self.starting_y, 50, 50)
        self.direction = self.starting_direction()

    def update(self):
        self.move()

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

    def starting_direction(self):
        if self.starting_x >= 1000:
            return 'rl'

        if self.starting_x <= 0:
            return 'lr'

        if self.starting_y >= 800:
            return 'bt'

        if self.starting_y <= 0:
            return 'tb'

    def detect_collision(self):
        for _ in pygame.sprite.spritecollide(self, self.character, False):
            self.character.sprites()[0].rect.x = 360
            self.character.sprites()[0].rect.y = 370
            self.character.sprites()[0].life -= 1
