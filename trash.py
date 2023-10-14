import pygame
import random


class papel(pygame.sprite.Sprite): #saco
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/papelhigienico.png")
        self.image = pygame.transform.scale(self.image, [50, 50])

        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect.x = random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

class garrafa(pygame.sprite.Sprite): #vidro
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/garrafa.png")
        self.image = pygame.transform.scale(self.image, [100, 100])

        self.rect = pygame.Rect(500, 50, 50, 50)
        self.rect.x = random.randint(1, 400)
        self.rect.y = random.randint(1, 400)


