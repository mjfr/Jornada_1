import pygame
import os.path


def sprite_loader(path):
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()


class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups, placar):
        super().__init__(*groups)

        self.sprites2 = {
            'front': sprite_loader('assets/personagem_frente.png'),
            'back': sprite_loader('assets/personagem_costas.png'),
            pygame.K_w: [sprite_loader('assets/personagem_costas_1.png'), sprite_loader('assets/personagem_costas_2.png')],
            pygame.K_s: [sprite_loader('assets/personagem_frente_1.png'), sprite_loader('assets/personagem_frente_2.png')],
            pygame.K_a: [sprite_loader('assets/personagem_esquerda_1.png'), sprite_loader('assets/personagem_esquerda_2.png')],
            pygame.K_d: [sprite_loader('assets/personagem_direita_1.png'), sprite_loader('assets/personagem_direita_2.png')]
        }
        self.current_sprite = 0
        self.speed = 5
        # Valores de velocidade para eixos
        self.x_value = 0
        self.y_value = 0
        # Usado para receber um grupo de assets de bloqueio
        self.blockage_group = None
        self.trashcan_group = None
        self.holding = None
        self.placar = placar
        self.e_key_pressed = False
        self.life = 3
        self.image = pygame.transform.scale(self.sprites2['front'], [25, 50])
        self.rect = pygame.Rect(360, 370, 25, 50)

    def sprite_setter(self, key):
        if self.current_sprite >= len(self.sprites2[key]):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites2[key][int(self.current_sprite)], [25, 50])
        self.current_sprite += 0.1

    # Atualiza os valores das velocidades de eixo, faz a lógica de limite de tela e move o personagem
    def update(self):
        # Reseta a velocidade axial (evita movimento infinito ao soltar as teclas)
        self.x_value = 0
        self.y_value = 0

        # keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()

        # Limites da janela
        if keys[pygame.K_d] and not self.rect.right >= 1000:
            self.x_value = self.speed
            self.sprite_setter(pygame.K_d)
        if keys[pygame.K_a] and not self.rect.left <= 0:
            self.x_value = -self.speed
            self.sprite_setter(pygame.K_a)
        if keys[pygame.K_w] and not self.rect.top <= 0:
            self.y_value = -self.speed
            self.sprite_setter(pygame.K_w)
        if keys[pygame.K_s] and not self.rect.bottom >= 805:
            self.y_value = self.speed
            self.sprite_setter(pygame.K_s)

        self.move(self.x_value, 0)
        self.move(0, self.y_value)
        
        if keys[pygame.K_e]:
            if not self.e_key_pressed:
                self.use_trashcan()
            self.e_key_pressed = True
        else:
            self.e_key_pressed = False

        self.placar.life = self.life

    # Atualiza os valores de movimento e verifica assets de bloqueio para impedir o movimento
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        # Pega cada bloqueio dentro do grupo de assets e impede a movimentação em cada um deles
        for block in pygame.sprite.spritecollide(self, self.blockage_group, False):
            if x > 0:
                self.rect.right = block.rect.left
            if x < 0:
                self.rect.left = block.rect.right
            if y > 0:
                self.rect.bottom = block.rect.top
            if y < 0:
                self.rect.top = block.rect.bottom

    def use_trashcan(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            for trashcan in pygame.sprite.spritecollide(self, self.trashcan_group, False):
                if self.holding == trashcan.material:
                    self.placar.incrementar_pontuacao(1)  # Adicione 1 ponto (ou a quantidade desejada)
                    self.holding = None
                elif self.holding is not None:
                    self.holding = None
                    self.placar.decrementar_pontuacao(1)
                    self.life -= 1
                    print(f'Vidas: {self.life}')
