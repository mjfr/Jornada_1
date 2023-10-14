import pygame
import random
import math


class sacoLixo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/sacodelixo.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect.x = random.randint(1, 400)
        self.rect.y = random.randint(1, 400)


