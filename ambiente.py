import pygame


class Blockage(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
