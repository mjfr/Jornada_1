import pygame


class TxtBtn(pygame.sprite.Sprite):
    def __init__(self, img, x, y, text_input, font, size, base_color, hovering_color, img_size=None, img_hover=None):
        """
        Construtor da classe TxtBtn.
        :param str or None img: Caminho do sistema para a imagem;
        :param int x: Posição horizontal. Quanto menor o valor de 'x' mais à esquerda estará, quanto maior, mais à
         direita;
        :param int y: Posição vertical. Quanto menor o 'y' mais acima estará, quanto maior, mais abaixo;
        :param str or None text_input: String passada pelo usuário;
        :param str font: Caminho do sistema para a fonte;
        :param int size: Valor inteiro que representa o tamanho da fonte;
        :param tuple or str base_color: Cor da fonte passada em tupla no formato HEX;
        :param tuple or str hovering_color: Cor da fonte ao interagir com o cursor, passada em tupla no formato HEX;
        :param tuple or int img_size: Tamanho da imagem passada em tupla representando largura e altura;
        :param str img_hover: Caminho do sistema para a imagem quando o mouse interage com o objeto.
        """
        super().__init__()

        self.img_size = img_size
        self.img = None if img is None else image_loader(img, self.img_size)
        self.img_aux = self.img
        self.img_hover = None if img_hover is None else image_loader(img_hover, self.img_size)
        self.x_pos = x
        self.y_pos = y
        self.font = pygame.font.Font(font, size)
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.img is None and self.text_input is not None:
            self.img = self.text
        self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen) -> None:
        """
        Função de atualização do objeto, define se um texto ou uma imagem será mostrada na interface.
        :param pygame.Surface screen: O display que terá o objeto renderizado.
        :return: None
        """
        if self.img is not None:
            screen.blit(self.img, self.rect)
        screen.blit(self.text, self.text_rect)

    def add_text(self, text) -> None:
        """
        Função que por meio de um parâmetro adiciona o valor da String no atributo text.
        :param str text: Texto que será renderizado junto ao objeto.
        :return: None
        """
        self.text = text

    def check_click(self, mouse_pos) -> bool:
        """
        Função que obtém a posição do mouse e verifica colisão com o objeto.
        :param tuple mouse_pos: Posição do cursor do mouse, tupla obtida por pygame.mouse.get_pos().
        :return: True se colidiu. False se não colidiu com o objeto.
        """
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def change_state(self, mouse_pos) -> None:
        """
        Função que altera o estado do objeto quando é detectada a colisão com o cursor do mouse.
        :param tuple mouse_pos: Posição do cursor do mouse, tupla obtida por pygame.mouse.get_pos().
        :return: None
        """
        if self.rect.collidepoint(mouse_pos):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            self.img = self.img_hover
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.img = self.img_aux


def image_loader(image, size=None) -> pygame.Surface:
    """
    Função que carrega e converte uma imagem.
    :param str image: Caminho do sistema para a imagem;
    :param int size: Valor inteiro que representa o tamanho da fonte.
    :return: Retorna a imagem carregada e convertida, escalada no tamanho definido.
    """
    image = pygame.image.load(image).convert_alpha()
    if size is None:
        size = (image.get_width(), image.get_height())
    return pygame.transform.scale(image, size)
