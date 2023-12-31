import pygame
import os.path
from placar import Placar


def sprite_loader(path) -> pygame.Surface:
    """
    Função que carrega a imagem e a converte.
    :param str path: Caminho para a pasta do sistema que contém as imagens
    :return: Retorna uma imagem convertida
    """
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()


class Character(pygame.sprite.Sprite):
    def __init__(self, *groups, placar):
        """
        Construtor da classe Character.
        :param object groups: Instância de pygame.sprite.Group() onde servirá de lista para as instâncias de Character;
        :param Placar placar: Instância de Placar.
        """
        super().__init__(*groups)

        self.sprites = {
            'front': sprite_loader('assets/personagem_frente.png'),
            'back': sprite_loader('assets/personagem_costas.png'),
            pygame.K_w: [
                sprite_loader('assets/personagem_costas_1.png'),
                sprite_loader('assets/personagem_costas_2.png')
            ],
            pygame.K_s: [
                sprite_loader('assets/personagem_frente_1.png'),
                sprite_loader('assets/personagem_frente_2.png')
            ],
            pygame.K_a: [
                sprite_loader('assets/personagem_esquerda_1.png'),
                sprite_loader('assets/personagem_esquerda_2.png')
            ],
            pygame.K_d: [
                sprite_loader('assets/personagem_direita_1.png'),
                sprite_loader('assets/personagem_direita_2.png')
            ]
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
        self.image = pygame.transform.scale(self.sprites['front'], [25, 50])
        self.rect = pygame.Rect(360, 370, 25, 50)

    def sprite_setter(self, key) -> None:
        """
        Função que altera o sprite do personagem de acordo com sua posição e um delay.
        :param int key: Tecla obtida pelo evento retornado por get_pressed().
        :return: None
        """
        if self.current_sprite >= len(self.sprites[key]):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[key][int(self.current_sprite)], [25, 50])
        self.current_sprite += 0.1

    # Atualiza os valores das velocidades de eixo, faz a lógica de limite de tela e move o personagem
    def update(self) -> None:
        """
        Função de atualização das funções do objeto.
        :return: None
        """
        # Reseta a velocidade axial (evita movimento infinito ao soltar as teclas)
        self.x_value = 0
        self.y_value = 0

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
    def move(self, x, y) -> None:
        """
        Função que define o movimento do objeto.
        :param int x: Valor inteiro que será adicionado ou subtraído do eixo x;
        :param int y: Valor inteiro que será adicionado ou subtraído do eixo y.
        :return: None
        """
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

    def use_trashcan(self) -> None:
        """
        Função de interação com o objeto instanciado de TrashCan.
        :return: None
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            for trashcan in pygame.sprite.spritecollide(self, self.trashcan_group, False):
                if self.holding == trashcan.material:
                    self.placar.incrementar_pontuacao(1)  # Adicione 1 ponto (ou a quantidade desejada)
                    self.holding = None
                    if self.speed >= 2:
                        self.speed *= 0.99
                elif self.holding is not None:
                    self.holding = None
                    self.placar.decrementar_pontuacao(1)
                    self.life -= 1
