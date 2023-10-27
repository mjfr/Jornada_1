import pygame


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
        points_txt = self.fonte.render(f'Pontuação: {self.pontuacao}', True, (0, 255, 255))
        tela.blit(points_txt, points_txt.get_rect(center=(500, 30)))
        life_txt = self.fonte.render(f'Vidas: {self.life}', True, (0, 255, 255))
        tela.blit(life_txt, life_txt.get_rect(center=(150, 30)))

    def decrementar_pontuacao(self, pontos):
        self.pontuacao -= pontos
