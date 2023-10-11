import pygame


class TrashCan(pygame.sprite.Sprite):
    def __init__(self, color, width, height, image):
        super().__init__()

        # self.image = pygame.Surface([width, height])
        # self.image.fill(color)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        # self.image = pygame.Surface([width, height])
        self.material = None

        # pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
