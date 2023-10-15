import pygame.sprite
from personagem import Personagem
from ambiente import Blockage
from lixeira import TrashCan
from lixos import Trash
import random
from placar import Placar

# Cores usadas (testes de rects)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MATERIAL = ['papel', 'vidro', 'organico', 'plastico']
COLORS_TC = [(0, 0, 200), (0, 200, 0), (110, 32, 32), (200, 0, 0)]
PAPER_IMG = {0: 'sprites/papel0.png', 1: 'sprites/papel1.png', 2: 'sprites/papel2.png'}
GLASS_IMG = {0: 'sprites/vidro0.png', 1: 'sprites/vidro1.png', 2: 'sprites/vidro2.png'}
ORGANIC_IMG = {0: 'sprites/organico0.png', 1: 'sprites/organico1.png', 2: 'sprites/organico2.png'}
PLASTIC_IMG = {0: 'sprites/plastico0.png', 1: 'sprites/plastico1.png', 2: 'sprites/plastico2.png'}
MATERIAL_IMG = [PAPER_IMG, GLASS_IMG, ORGANIC_IMG, PLASTIC_IMG]
# MATERIAL_DICT = dict(zip(MATERIAL, MATERIAL_IMG))

background = pygame.image.load('sprites/mapa_pronto.png')

# Utilizado para testes
# MATERIAL = ['papel', 'metal', 'vidro', 'organico', 'plastico']
# COLORS_TC = [(0, 0, 200), (255, 255, 0), (0, 200, 0), (110, 32, 32), (200, 0, 0)]

# Inicializando o Pygame e Criando a Janela do Jogo
pygame.init()
display = pygame.display.set_mode([1000, 800])
pygame.display.set_caption("Recycle Rush")

# Objetos
objectGroup = pygame.sprite.Group()
placar = Placar()
personagem = Personagem(objectGroup, placar=placar)

# Criando os espaços dos obstáculos (casas e carros)
sprites_list = pygame.sprite.Group()
blockages = [
    Blockage(RED, 190, 163, x=60),
    Blockage(RED, 58, 68, x=310),
    Blockage(RED, 145, 154, x=437),
    Blockage(RED, 209, 156, x=722),
    Blockage(RED, 100, 38, x=537, y=220),
    Blockage(RED, 186, 157, x=48, y=290),
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
    TrashCan(32, 46, 'sprites/lixeira_papel.png', x_flip=1, x=2, y=175, material=MATERIAL[0]),
    TrashCan(32, 46, 'sprites/lixeira_vidro.png', x_flip=1, x=2, y=530, material=MATERIAL[1]),
    TrashCan(32, 46, 'sprites/lixeira_organica.png', x=965, y=530, material=MATERIAL[2]),
    TrashCan(32, 46, 'sprites/lixeira_plastico.png', x=965, y=175, material=MATERIAL[3])
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
    trash_test.character_group = objectGroup
    return trash_test


# Música de fundo do jogo
# pygame.mixer.music.load("dados/Juhani Junkala [Chiptune Adventures] 1. Stage 1.wav")
# pygame.mixer.music.play(-1)

# Efeitos sonoros
# andando = pygame.mixer.Sound("dados/Fantozzi-StoneR1.FLAC")


gameLoop = True
clock = pygame.time.Clock()

# Criando o botão de fechar no X
while gameLoop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    # Se a lista de sprites de lixo estiver vazia, adiciona outro lixo ao mapa
    if not sprites_list3.sprites():
        sprites_list3.add(create_trash())

    # Update:
    objectGroup.update()
    # trash_test.update()
    sprites_list3.update()

    # Draw:
    # display.fill([152, 250, 239])
    sprites_list.draw(display)
    display.blit(background, (0, 0))
    sprites_list2.draw(display)
    sprites_list3.draw(display)
    objectGroup.draw(display)
    placar.render(display)
    pygame.display.flip()
    pygame.display.update()
