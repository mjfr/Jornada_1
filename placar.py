import pygame
from txtbtn import TxtBtn


class Placar:
    def __init__(self):
        self.pontuacao = 0
        self.life = None
        self.fonte = pygame.font.Font('assets/pixeloid_sans.ttf', 36)
        self.cor = (255, 255, 255)

    def incrementar_pontuacao(self, pontos):
        self.pontuacao += pontos

    def obter_pontuacao(self):
        return self.pontuacao

    def reset(self):
        self.pontuacao = 0

    def render(self, tela):
        points_txt = TxtBtn('assets/nome_retangulo.png', 500, 30, f'Pontuação: {self.pontuacao}',
                            'assets/pixeloid_sans.ttf', 26, (0, 0, 0), (0, 0, 0), (250, 40),
                            'assets/nome_retangulo.png')
        life_txt = TxtBtn('assets/nome_retangulo.png', 150, 30, f'Vidas: {self.life}', 'assets/pixeloid_sans.ttf', 26,
                          (255, 0, 0), (255, 0, 0), (150, 40), 'assets/nome_retangulo.png')
        for text in [points_txt, life_txt]:
            text.update(tela)

    def decrementar_pontuacao(self, pontos):
        self.pontuacao -= pontos
