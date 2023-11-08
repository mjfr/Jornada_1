import pygame


class Blockage(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x=0, y=0):
        """
        Construtor da classe Blockage.
        :param tuple color: Cor definida em tupla tripla, formato RGB. Útil para posicionamento ao sobrepor o plano de
         fundo;
        :param int width: Largura do objeto;
        :param int height: Altura do objeto;
        :param int x: Posição horizontal. Quanto menor o valor de 'x' mais à esquerda estará, quanto maior, mais à
         direita.
        :param int y: Posição vertical. Quanto menor o 'y' mais acima estará, quanto maior, mais abaixo.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y) -> None:
        """
        Função para definir o posicionamento do retângulo em tela.
        :param int x: Posição horizontal. Quanto menor o valor de 'x' mais à esquerda estará, quanto maior, mais à
         direita.
        :param int y: Posição vertical. Quanto menor o 'y' mais acima estará, quanto maior, mais abaixo.
        :return: None
        """
        self.rect.x = x
        self.rect.y = y
