import pygame


class TrashCan(pygame.sprite.Sprite):
    def __init__(self, width, height, image, material=None, x_flip=0, y_flip=0, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = self.image_flip(x_flip, y_flip)
        self.material = material

        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def image_flip(self, x, y):
        return pygame.transform.flip(self.image, x, y)
