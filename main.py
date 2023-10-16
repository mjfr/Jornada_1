import os.path

import pygame
import sys
from personagem import Personagem
from ambiente import Blockage
from lixeira import TrashCan
from lixos import Trash
from placar import Placar
from botao import Button
import random

# Cores usadas (testes de rects)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MATERIAL = ['papel', 'vidro', 'organico', 'plastico']
COLORS_TC = [(0, 0, 200), (0, 200, 0), (110, 32, 32), (200, 0, 0)]
PAPER_IMG = {0: 'assets/papel0.png', 1: 'assets/papel1.png', 2: 'assets/papel2.png'}
GLASS_IMG = {0: 'assets/vidro0.png', 1: 'assets/vidro1.png', 2: 'assets/vidro2.png'}
ORGANIC_IMG = {0: 'assets/organico0.png', 1: 'assets/organico1.png', 2: 'assets/organico2.png'}
PLASTIC_IMG = {0: 'assets/plastico0.png', 1: 'assets/plastico1.png', 2: 'assets/plastico2.png'}
MATERIAL_IMG = [PAPER_IMG, GLASS_IMG, ORGANIC_IMG, PLASTIC_IMG]
# MATERIAL_DICT = dict(zip(MATERIAL, MATERIAL_IMG))

background = pygame.image.load('assets/mapa_pronto.png')

# Utilizado para testes
# MATERIAL = ['papel', 'metal', 'vidro', 'organico', 'plastico']
# COLORS_TC = [(0, 0, 200), (255, 255, 0), (0, 200, 0), (110, 32, 32), (200, 0, 0)]

# Inicializando o Pygame e Criando a Janela do Jogo
pygame.init()
display = pygame.display.set_mode([1000, 800])
pygame.display.set_caption("Recycle Rush")


def play():
    # Objetos
    object_group = pygame.sprite.Group()
    placar = Placar()
    personagem = Personagem(object_group, placar=placar)

    # Criando os espaços dos obstáculos (casas e carros)
    sprites_list = pygame.sprite.Group()
    blockages = [
        Blockage(RED, 190, 163, x=60),
        Blockage(RED, 58, 68, x=310),
        Blockage(RED, 145, 154, x=437),
        Blockage(RED, 209, 156, x=722),
        Blockage(RED, 100, 38, x=537, y=220),
        Blockage(RED, 186, 150, x=48, y=310),
        Blockage(RED, 167, 135, x=424, y=310),
        Blockage(RED, 180, 145, x=791, y=296),
        Blockage(RED, 178, 166, x=44, y=589),
        Blockage(RED, 152, 166, x=416, y=589),
        Blockage(RED, 56, 40, x=633, y=641),
        Blockage(RED, 200, 166, x=800, y=589),
        Blockage(RED, 98, 40, x=260, y=498)
        ]
    for block in blockages:
        sprites_list.add(block)
    personagem.blockage_group = sprites_list

    # Criando as lixeiras
    sprites_list2 = pygame.sprite.Group()
    trashcans = [
        TrashCan(32, 46, 'assets/lixeira_papel.png', x_flip=1, x=2, y=175, material=MATERIAL[0]),
        TrashCan(32, 46, 'assets/lixeira_vidro.png', x_flip=1, x=2, y=530, material=MATERIAL[1]),
        TrashCan(32, 46, 'assets/lixeira_organica.png', x=965, y=530, material=MATERIAL[2]),
        TrashCan(32, 46, 'assets/lixeira_plastico.png', x=965, y=175, material=MATERIAL[3])
        ]
    for trashcan in trashcans:
        sprites_list2.add(trashcan)
    personagem.trashcan_group = sprites_list2

    sprites_list3 = pygame.sprite.Group()

    # Função para criar uma nova instância de lixo
    def create_trash():
        # TODO: Fazer o lixo spawnar com o material aleatório
        rng = random.randint(0, 3)
        rng_img = random.randint(0, 2)
        trash_test = Trash(MATERIAL_IMG[rng][rng_img], 20, 20, sprites_list, sprites_list2)
        trash_test.material = MATERIAL[rng]
        trash_test.character_group = object_group
        return trash_test

    # Música de fundo do jogo
    pygame.mixer.music.load("assets/Juhani Junkala [Chiptune Adventures] 1. Stage 1.wav")
    pygame.mixer.music.play(-1)

    # Efeitos sonoros
    # andando = pygame.mixer.Sound("dados/Fantozzi-StoneR1.FLAC")

    clock = pygame.time.Clock()

    # Criando o botão de fechar no X
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Se a lista de assets de lixo estiver vazia, adiciona outro lixo ao mapa
        if not sprites_list3.sprites():
            sprites_list3.add(create_trash())

        # Update:
        object_group.update()
        sprites_list3.update()

        # Draw:
        sprites_list.draw(display)
        display.blit(background, (0, 0))
        sprites_list2.draw(display)
        sprites_list3.draw(display)
        object_group.draw(display)
        placar.render(display)
        pygame.display.flip()
        pygame.display.update()

        if personagem.life == 0:
            name_screen(personagem.placar.pontuacao)


def name_screen(points):
    title = (pygame.font.Font('assets/pixeloid_sans.ttf', 100)
             .render('Salvar Partida', True, '#FFA756'))
    title_rect = title.get_rect(center=(500, 100))
    user_text = ''

    # Booleans
    # Se o objeto for clicado, active = True
    active = False
    # Ao salvar o nome, saved = True
    saved = False

    name_frame = pygame.image.load('assets/nome_retangulo.png').convert_alpha()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        # Obtendo eventos que ocorrem no jogo
        for event in pygame.event.get():
            display.fill((42, 1, 52))
            display.blit(title, title_rect)
            # Ao clicar no X da janela, fecha o processo do pygame e fecha o processo do python
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Pressionar uma tecla enquanto o objeto for selecionado, captura a tecla pressionada até o limite de
            # caractere
            if event.type == pygame.KEYDOWN and active:
                # Faz com que a string seja igual a si mesma menos sua última posição
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    # Adiciona na string o caractere capturado
                elif len(user_text) <= 15:
                    user_text += event.unicode

            if not saved:
                input_rect = Button(name_frame, 500, 250, user_text, 'assets/pixeloid_sans.ttf', 26,
                                    "#FFA756", "#FFA756")
                save_rect = Button(None, 500, 400, "Continuar", 'assets/pixeloid_sans.ttf',
                                   50, "#FFA756", "White")

                # Ao clicar no botão, seu estado é alterado (selecionado)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.check_click(mouse_pos):
                        active = True
                    else:
                        active = False

                for button in [input_rect, save_rect]:
                    button.change_color(mouse_pos)
                    button.update(display)

                # Se o nome possuir um ou mais caracteres
                if event.type == pygame.MOUSEBUTTONDOWN and len(user_text) > 0:
                    # se a posição em que o cursor do mouse clicado for o botão de salvar:
                    if save_rect.check_click(event.pos):
                        # Apenas por testes: abrindo um arquivo no modo append
                        if not os.path.exists('save.csv'):
                            with open(file='save.csv', mode='a+', encoding='utf-8') as file:
                                file.write('Nome, Pontuação\n')
                        with open(file='save.csv', mode='a+', encoding='utf-8') as file:
                            # Salvando o nome do jogador e sua pontuação
                            file.write(f'{user_text}, {points}\n')
                        saved = True
                        main_menu()
        pygame.display.update()


def main_menu():
    title = (pygame.font.Font('assets/pixeloid_sans.ttf', 100)
             .render('Recycle Rush', True, '#FFA756'))
    title_rect = title.get_rect(center=(500, 100))
    play_button = Button(None, 500, 250, "PLAY", 'assets/pixeloid_sans.ttf', 50,
                         "#FFA756", "White")
    ranking_button = Button(None, 500, 400, "RANKING", 'assets/pixeloid_sans.ttf', 50,
                            "#FFA756", "White")
    quit_button = Button(None, 500, 550, "QUIT", 'assets/pixeloid_sans.ttf', 50,
                         "#FFA756", "White")
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        display.fill((42, 1, 52))
        display.blit(title, title_rect)

        for button in [play_button, ranking_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_click(menu_mouse_pos):
                    play()
                if quit_button.check_click(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Draw
        pygame.display.update()


main_menu()
