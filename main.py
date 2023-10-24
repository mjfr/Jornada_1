import os.path
import csv
import pygame
import sys
from personagem import Personagem
from ambiente import Blockage
from lixeira import TrashCan
from lixos import Trash
from placar import Placar
from botao import Button
import random

# TODO: Adicionar sprites aos botões (menu, tela de nome, ranking)
# TODO: Refatorar o código se possível
# TODO: Melhorar a visibilidade do placar
# TODO:


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
BACKGROUND = pygame.image.load('assets/mapa_pronto.png')

# Inicializando o Pygame e Criando a Janela do Jogo
pygame.init()
RANKING_FONT = pygame.font.Font('assets/pixeloid_sans.ttf', 18)
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
        Blockage(RED, 190, 156, x=60),
        Blockage(RED, 58, 68, x=310),
        Blockage(RED, 145, 156, x=437),
        Blockage(RED, 209, 156, x=722),
        Blockage(RED, 100, 35, x=537, y=220),
        Blockage(RED, 186, 135, x=48, y=306),
        Blockage(RED, 167, 135, x=424, y=306),
        Blockage(RED, 180, 135, x=791, y=306),
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
        rng = random.randint(0, 3)
        rng_img = random.randint(0, 2)
        trash_test = Trash(MATERIAL_IMG[rng][rng_img], 20, 20, sprites_list, sprites_list2)
        trash_test.material = MATERIAL[rng]
        trash_test.character_group = object_group
        return trash_test

    # Música de fundo do jogo
    pygame.mixer.music.load("assets/Juhani Junkala [Chiptune Adventures] 1. Stage 1.wav")
    pygame.mixer.music.play(-1)

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
        display.blit(BACKGROUND, (0, 0))
        sprites_list2.draw(display)
        sprites_list3.draw(display)
        object_group.draw(display)
        placar.render(display)
        pygame.display.flip()
        pygame.display.update()

        if personagem.life == 0:
            name_screen(personagem.placar.pontuacao)


def ranking():
    player_data = []
    sorted_players = []
    if os.path.exists('save.csv'):
        with open('save.csv', 'r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                player = {
                    'Nome': row['Nome'],
                    'Pontuação': int(row['Pontuação']),
                }
                player_data.append(player)
        sorted_players = sorted(player_data, key=lambda x: x['Pontuação'], reverse=True)

    title = (pygame.font.Font('assets/pixeloid_sans.ttf', 70)
             .render('Ranking', True, '#FFA756'))
    title_rect = title.get_rect(center=(500, 50))
    menu_button = Button(None, 500, 750, "Main Menu", 'assets/pixeloid_sans.ttf', 30,
                         "#FFA756", "White")
    next_page_button = Button(None, 700, 400, "-->", 'assets/pixeloid_sans.ttf', 30,
                              "#FFA756", "White")
    prev_page_button = Button(None, 300, 400, "<--", 'assets/pixeloid_sans.ttf', 30,
                              "#FFA756", "White")
    current_page = 0
    players_per_page = 15
    players_amount = len(sorted_players)

    while True:
        display.fill((42, 1, 52))
        display.blit(title, title_rect)

        current_index = current_page * players_per_page
        final_index = (current_page + 1) * players_per_page

        if final_index > players_amount:
            final_index = players_amount

        y = 200
        for rank, player in enumerate(sorted_players[current_index:final_index], start=current_index + 1):
            player_text = f'{rank}. {player["Nome"]}:'
            player_points_text = f'{player["Pontuação"]}pts'
            player_rendered = RANKING_FONT.render(player_text, True, '#FFA756')
            player_points_rendered = RANKING_FONT.render(player_points_text, True, '#FFA756')
            display.blit(player_rendered, player_rendered.get_rect(topleft=(350, y)))
            display.blit(player_points_rendered, player_points_rendered.get_rect(topright=(650, y)))
            y += 30

        page_render = RANKING_FONT.render(f'Página {current_page}', True, '#FFA756')
        display.blit(page_render, page_render.get_rect(center=(500, 700)))

        mouse_pos = pygame.mouse.get_pos()
        for button in [menu_button, next_page_button, prev_page_button]:
            button.change_color(mouse_pos)
            button.update(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.check_click(mouse_pos):
                    main_menu()
                if next_page_button.check_click(mouse_pos):
                    if final_index < len(sorted_players):
                        current_page += 1
                if prev_page_button.check_click(mouse_pos):
                    if current_page > 0:
                        current_page -= 1
        pygame.display.update()


def name_screen(points):
    pygame.mixer.music.stop()
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
                            with open(file='save.csv', mode='a+', encoding='utf8') as file:
                                file.write('Nome,Pontuação\n')
                        with open(file='save.csv', mode='a+', encoding='utf8') as file:
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
                if ranking_button.check_click(menu_mouse_pos):
                    ranking()
                if quit_button.check_click(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Draw
        pygame.display.update()


main_menu()
