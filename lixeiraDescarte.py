import random
import pygame
import math
import random
class lixeira(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/lixobonito.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(20, 20, 50, 50)

        self.rect = self.image.get_rect()