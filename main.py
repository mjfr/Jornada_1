import os.path
import csv
import pygame
import sys
from character import Character
from ambiente import Blockage
from lixeira import TrashCan
from lixos import Trash
from placar import Placar
from txtbtn import TxtBtn
from carros import Car
import random

# Cores para testes/debug
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Lista e dicionários auxiliares para setar imagens e randomizar os lixos
MATERIAL = ['papel', 'vidro', 'organico', 'plastico']
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


def play() -> None:
    """
    Função que contém o loop principal do jogo.
    A função possui três funcionalidades principais:
        - Instanciação de objetos;
        - Atualização das ações dos objetos;
        - Atualização visual dos sprites dos objetos.
    :return: None
    """
    # Instanciando o jogador e o placar
    object_group = pygame.sprite.Group()
    placar = Placar()
    character = Character(object_group, placar=placar)
    sprites_list4 = pygame.sprite.Group()
    Car(sprites_list4, character=object_group, pos_x=-100, pos_y=230, horizontal=True)
    Car(sprites_list4, character=object_group, pos_x=1100, pos_y=505, horizontal=True)

    # Criando os espaços dos obstáculos (casas e carros)
    sprites_list = pygame.sprite.Group()
    blockages = [
        Blockage(RED, 149, 147, x=70),
        Blockage(RED, 207, 149, x=360),
        Blockage(RED, 178, 156, x=698),
        Blockage(RED, 53, 39, x=945, y=20),
        Blockage(RED, 100, 35, x=537, y=220),
        Blockage(RED, 186, 135, x=48, y=306),
        Blockage(RED, 167, 135, x=424, y=306),
        Blockage(RED, 180, 135, x=791, y=306),
        Blockage(RED, 191, 157, x=0, y=589),
        Blockage(RED, 140, 135, x=368, y=620),
        Blockage(RED, 53, 39, x=579, y=641),
        Blockage(RED, 162, 135, x=683, y=620),
        Blockage(RED, 98, 40, x=260, y=498)
        ]
    # Adicionando os bloqueios na lista de sprites
    for block in blockages:
        sprites_list.add(block)
    character.blockage_group = sprites_list

    # Criando as lixeiras
    sprites_list2 = pygame.sprite.Group()
    TrashCan(sprites_list2, width=32, height=46, image='assets/lixeira_papel.png', x_flip=1, x=2, y=175,
             material=MATERIAL[0]),
    TrashCan(sprites_list2, width=32, height=46, image='assets/lixeira_vidro.png', x_flip=1, x=2, y=530,
             material=MATERIAL[1]),
    TrashCan(sprites_list2, width=32, height=46, image='assets/lixeira_organica.png', x=905, y=750,
             material=MATERIAL[2]),
    TrashCan(sprites_list2, width=32, height=46, image='assets/lixeira_plastico.png', x=905, y=175,
             material=MATERIAL[3])

    character.trashcan_group = sprites_list2

    sprites_list3 = pygame.sprite.Group()

    # Função para criar uma nova instância de lixo
    # def create_trash() -> Trash:
    #     """
    #     Função auxiliar
    #     :return:
    #     """
    #     rng = random.randint(0, 3)
    #     rng_img = random.randint(0, 2)
    #     trash = Trash(sprites_list3, image=MATERIAL_IMG[rng][rng_img], width=20, height=20,
    #                   blockage_group=sprites_list, trash_can_group=sprites_list2)
    #     trash.material = MATERIAL[rng]
    #     trash.character_group = object_group
    #     return trash

    # Música de fundo do jogo
    pygame.mixer.music.load("assets/Juhani Junkala [Chiptune Adventures] 1. Stage 1.wav")
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    clock.tick(60)

    # Criando o botão de fechar no X
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Se a lista de assets de lixo estiver vazia, adiciona outro lixo ao mapa
        if not sprites_list3.sprites():
            # create_trash()
            rng = random.randint(0, 3)
            rng_img = random.randint(0, 2)
            trash = Trash(sprites_list3, image=MATERIAL_IMG[rng][rng_img],
                          blockage_group=sprites_list, trash_can_group=sprites_list2)
            trash.material = MATERIAL[rng]
            trash.character_group = object_group

        # Update:
        object_group.update()
        sprites_list3.update()
        sprites_list4.update()

        # Draw:
        sprites_list.draw(display)
        display.blit(BACKGROUND, (0, 0))
        sprites_list2.draw(display)
        placar.render(display)
        sprites_list3.draw(display)
        object_group.draw(display)
        sprites_list4.draw(display)
        pygame.display.flip()
        pygame.display.update()

        if character.life == 0:
            name_screen(character.placar.pontuacao)


def ranking() -> None:
    """
    Função que trata da interface de ranking e sua lógica.
    :return: None
    """
    player_data = []
    sorted_players = []
    # Se o arquivo de save existir, abre o arquivo e cria um dicionário para o player adicionando em uma lista
    if os.path.exists('save.csv'):
        with open('save.csv', 'r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                player = {
                    'Nome': row['Nome'],
                    'Pontuação': int(row['Pontuação'])
                }
                player_data.append(player)
        # Utiliza a função sorted para ordenar os jogadores através da pontuação
        sorted_players = sorted(player_data, key=lambda x: x['Pontuação'], reverse=True)

    # Criando textos e botões
    title = (pygame.font.Font('assets/pixeloid_sans.ttf', 70)
             .render('Ranking', True, '#FFA756'))
    title_rect = title.get_rect(center=(500, 50))
    menu_button = TxtBtn(None, 500, 750, "Main Menu", 'assets/pixeloid_sans.ttf', 30,
                         "#FFA756", "White")
    next_page_button = TxtBtn(None, 700, 400, "-->", 'assets/pixeloid_sans.ttf', 30,
                              "#FFA756", "White")
    prev_page_button = TxtBtn(None, 300, 400, "<--", 'assets/pixeloid_sans.ttf', 30,
                              "#FFA756", "White")
    current_page = 0
    players_per_page = 15
    players_amount = len(sorted_players)

    while True:
        display.fill((42, 1, 52))
        display.blit(title, title_rect)

        # Index utilizado no enumerate para trazer apenas os jogadores que devem estar no range da página atual
        current_index = current_page * players_per_page
        final_index = (current_page + 1) * players_per_page

        if final_index > players_amount:
            final_index = players_amount

        # Altura inicial do texto do ranking
        y = 200
        # Loop para obter os players ordenados com colocação, nome e pontuação
        for rank, player in enumerate(sorted_players[current_index:final_index], start=current_index + 1):
            player_text = f'{rank}. {player["Nome"]}:'
            player_points_text = f'{player["Pontuação"]}pts'
            player_rendered = RANKING_FONT.render(player_text, True, '#FFA756')
            player_points_rendered = RANKING_FONT.render(player_points_text, True, '#FFA756')
            display.blit(player_rendered, player_rendered.get_rect(topleft=(350, y)))
            display.blit(player_points_rendered, player_points_rendered.get_rect(topright=(650, y)))
            y += 30

        page_render = RANKING_FONT.render(f'Página {current_page+1}', True, '#FFA756')
        display.blit(page_render, page_render.get_rect(center=(500, 700)))

        mouse_pos = pygame.mouse.get_pos()
        for button in [menu_button, next_page_button, prev_page_button]:
            button.change_state(mouse_pos)
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


def name_screen(points) -> None:
    """
    A função name_screen cria e administra a lógica da interface de salvamento de progresso da partida.
    :param points: Pontuação pós-partida obtida através do atributo placar da instância de personagem
    :return: None
    """
    # Parando a música quando o jogador perde
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
                elif len(user_text) <= 15 and event.key != pygame.K_RETURN:
                    user_text += event.unicode

            if not saved:
                input_rect = TxtBtn('assets/nome_retangulo.png', 500, 250, user_text, 'assets/pixeloid_sans.ttf', 26,
                                    "#FFA756", "#FFA756", (400, 70), 'assets/nome_retangulo.png')
                save_rect = TxtBtn(None, 500, 400, "Continuar", 'assets/pixeloid_sans.ttf',
                                   50, "#FFA756", "White")

                # Ao clicar no botão, seu estado é alterado (selecionado)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.check_click(mouse_pos):
                        active = True
                    else:
                        active = False

                for button in [input_rect, save_rect]:
                    button.change_state(mouse_pos)
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


def main_menu() -> None:
    """
    Função que cria e administra a lógica da interface inicial.
    :return: None
    """
    # Setando botões e textos na tela
    title = (pygame.font.Font('assets/pixeloid_sans.ttf', 100)
             .render('Recycle Rush', True, '#FFA756'))
    title_rect = title.get_rect(center=(500, 200))
    play_button = TxtBtn('assets/btn_jogar1.png', 500, 400, None, 'assets/pixeloid_sans.ttf', 50,
                         "#FFA756", "white", (440, 135), 'assets/btn_jogar2.png')
    ranking_button = TxtBtn('assets/btn_ranking1.png', 50, 50, None, 'assets/pixeloid_sans.ttf', 50,
                            "#FFA756", "white", (70, 70), 'assets/btn_ranking2.png')
    quit_button = TxtBtn('assets/btn_shutdown1.png', 950, 750, None, 'assets/pixeloid_sans.ttf', 50,
                         "#FFA756", "white", (70, 70), 'assets/btn_shutdown2.png')
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        display.fill((42, 1, 52))
        display.blit(title, title_rect)

        # Alterando e atualizando botões
        for button in [play_button, ranking_button, quit_button]:
            button.change_state(menu_mouse_pos)
            button.update(display)

        # Capturando eventos
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
