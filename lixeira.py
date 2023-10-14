import pygame


class TrashCan(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.material = None

        self.rect = self.image.get_rect()
