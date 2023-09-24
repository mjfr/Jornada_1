import pygame

class personagem(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/pixil-frame-0.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 50, 50)



    def update(self, *args):

        #Personagem andando

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not self.rect.x >= 775:
            self.rect.x += 3

        if keys[pygame.K_a] and not self.rect.x <= -20:
            self.rect.x -= 3


        if keys[pygame.K_w]:
            self.rect.y -=3

        if keys[pygame.K_s]:
            self.rect.y += 3

        #Limite da área do jogo

        if self.rect.top <0:
            self.rect.top = 0

        if self.rect.bottom > 580:
            self.rect.bottom = 580






