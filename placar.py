import pygame
from txtbtn import TxtBtn


class Placar:
    def __init__(self):
        """
        Construtor da classe Placar.
        """
        self.pontuacao = 0
        self.life = None
        self.fonte = pygame.font.Font('assets/pixeloid_sans.ttf', 36)
        self.cor = (255, 255, 255)

    def incrementar_pontuacao(self, pontos) -> None:
        """
        Função que incrementa o atributo pontuacao de acordo com a pontuação geral.
        :param int pontos: Quantidade de pontos a serem incrementados.
        :return: None
        """
        if self.pontuacao == 0:
            self.pontuacao += pontos
        else:
            self.pontuacao += (pontos * -(-self.pontuacao//10))

    def obter_pontuacao(self) -> int:
        """
        Função que retorna a quantidade de pontos adicionados na instância de Placar.
        :return: Retorna a pontuação em formato int.
        """
        return self.pontuacao

    def reset(self) -> None:
        """
        Função que define a quantidade de pontos novamente para zero.
        :return: None
        """
        self.pontuacao = 0

    def render(self, tela) -> None:
        """
        Função que renderiza o objeto na interface.
        :param pygame.Surface tela: O display que terá o objeto renderizado.
        :return: None
        """
        points_txt = TxtBtn('assets/nome_retangulo.png', 500, 30, f'Pontuação: {self.pontuacao}',
                            'assets/pixeloid_sans.ttf', 26, (0, 0, 0), (0, 0, 0),
                            (250, 40), 'assets/nome_retangulo.png')
        life_txt = TxtBtn('assets/nome_retangulo.png', 150, 30, f'Vidas: {self.life}',
                          'assets/pixeloid_sans.ttf', 26, (255, 0, 0), (255, 0, 0),
                          (150, 40), 'assets/nome_retangulo.png')
        for text in [points_txt, life_txt]:
            text.update(tela)

    def decrementar_pontuacao(self, pontos) -> None:
        """
        Função que decrementa o valor do atributo pontuacao de acordo com a pontuação geral.
        :param int pontos: Quantidade de pontos a serem decrementados;
        :return: None
        """
        self.pontuacao -= (pontos * -(-self.pontuacao//10))
