import pygame


class TrashCan(pygame.sprite.Sprite):
    def __init__(self, *groups, width, height, image, material=None, x_flip=0, y_flip=0, x=0, y=0):
        """
        Construtor da classe TrashCan.
        :param object groups: Instância de pygame.sprite.Group() onde servirá de lista para as instâncias de TrashCan;
        :param int width: Largura do objeto;
        :param int height: Altura do objeto;
        :param str image: Caminho do sistema para a imagem;
        :param str material: String com o nome do material da lixeira;
        :param bool or int x_flip: Parâmetro para inverter o eixo da image. Valor pode ser apenas 1 ou 0;
        :param bool or int y_flip: Parâmetro para inverter o eixo da image. Valor pode ser apenas 1 ou 0;
        :param int x: Posição horizontal. Quanto menor o valor de 'x' mais à esquerda estará, quanto maior, mais à
         direita;
        :param int y: Posição vertical. Quanto menor o 'y' mais acima estará, quanto maior, mais abaixo.
        """
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = self.image_flip(x_flip, y_flip)
        self.material = material

        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y) -> None:
        """
        Função para definir o posicionamento do retângulo em tela
        :param int x: Posição horizontal. Quanto menor o valor de 'x' mais à esquerda estará, quanto maior, mais à
         direita.
        :param int y: Posição vertical. Quanto menor o 'y' mais acima estará, quanto maior, mais abaixo.
        :return: None
        """
        self.rect.x = x
        self.rect.y = y

    def image_flip(self, x, y) -> pygame.Surface:
        """
        :param bool x: Parâmetro para inverter o eixo horizontal da image. Valor pode ser apenas 1 ou 0;
        :param bool y: Parâmetro para inverter o eixo vertical da image. Valor pode ser apenas 1 ou 0.
        :return: Retorna a imagem invertida
        """
        return pygame.transform.flip(self.image, x, y)
