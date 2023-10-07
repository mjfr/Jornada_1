import pygame


class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.speed = 9
        # Valores de velocidade para eixos
        self.x_value = 0
        self.y_value = 0
        # Usado para receber um grupo de sprites de bloqueio
        self.blockage_group = None
        self.trashcan_group = None
        # self.image = pygame.image.load("dados/pixil-frame-0.png")
        # self.image = pygame.transform.scale(self.image, [100, 100])
        self.image = pygame.Surface([25, 50])
        self.image.fill((220, 135, 79))

        self.rect = pygame.Rect(50, 50, 25, 50)

    # Atualiza os valores das velocidades de eixo, faz a lógica de limite de tela e move o personagem
    def update(self, *args):
        # Reseta a velocidade axial (evita movimento infinito ao soltar as teclas)
        self.x_value = 0
        self.y_value = 0

        keys = pygame.key.get_pressed()

        # Limites da janela
        if keys[pygame.K_d] and not self.rect.right >= 840:
            self.x_value = self.speed
        if keys[pygame.K_a] and not self.rect.left <= 0:
            self.x_value = -self.speed
        if keys[pygame.K_w] and not self.rect.top <= 0:
            self.y_value = -self.speed
        if keys[pygame.K_s] and not self.rect.bottom >= 600:
            self.y_value = self.speed

        self.move(self.x_value, 0)
        self.move(0, self.y_value)
        self.use_trashcan(keys)

    # Atualiza os valores de movimento e verifica sprites de bloqueio para impedir o movimento
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        # Pega cada bloqueio dentro do grupo de sprites e impede a movimentação em cada um deles
        for block in pygame.sprite.spritecollide(self, self.blockage_group, False):
            if x > 0:
                self.rect.right = block.rect.left
            if x < 0:
                self.rect.left = block.rect.right
            if y > 0:
                self.rect.bottom = block.rect.top
            if y < 0:
                self.rect.top = block.rect.bottom

    def use_trashcan(self, key):
        for trashcan in pygame.sprite.spritecollide(self, self.trashcan_group, False):
            if self.rect.colliderect(trashcan.rect) and key[pygame.K_e]:
                print(trashcan.material)
