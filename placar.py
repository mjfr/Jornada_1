import pygame


class Placar:
    def __init__(self):
        self.pontuacao = 0
        self.fonte = pygame.font.Font('assets/pixeloid_sans.ttf', 36)
        self.cor = (255, 255, 255)

    def incrementar_pontuacao(self, pontos):
        self.pontuacao += pontos

    def obter_pontuacao(self):
        return self.pontuacao

    def reset(self):
        self.pontuacao = 0

    def render(self, tela):
        texto = self.fonte.render(f'Pontuação: {self.pontuacao}', True, (255, 0, 0))
        tela.blit(texto, (377, 10))  # Ajuste as coordenadas (320, 10) conforme necessário

    def decrementar_pontuacao(self, pontos):
        self.pontuacao -= pontos
