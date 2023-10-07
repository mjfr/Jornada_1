import pygame.sprite
from personagem import Personagem
from ambiente import Blockage
from lixeira import TrashCan

# Cores usadas (testes de rects)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MATERIAL = ['papel', 'metal', 'vidro', 'organico', 'plastico']
COLORS_TC = [(0, 0, 200), (255, 255, 0), (0, 200, 0), (110, 32, 32), (200, 0, 0)]

# Inicializando o Pygame e Criando a Janela do Jogo
pygame.init()
display = pygame.display.set_mode([840, 600])
pygame.display.set_caption("Recycle Rush")

# Objetos
objectGroup = pygame.sprite.Group()
personagem = Personagem(objectGroup)

# Criando os obstáculos (testes de rects) para implementar quando o design do mapa estiver completo
sprites_list = pygame.sprite.Group()
house = Blockage(RED, 80, 50)
house.rect.x = 100
house.rect.y = 300
building = Blockage(GREEN, 125, 200)
building.rect.x = 250
building.rect.y = 100
hangar = Blockage(BLUE, 300, 100)
hangar.rect.x = 450
hangar.rect.y = 300
sprites_list.add(house)
sprites_list.add(building)
sprites_list.add(hangar)
personagem.blockage_group = sprites_list

# Criando as lixeiras
sprites_list2 = pygame.sprite.Group()
paper_tc = TrashCan(COLORS_TC[0], 20, 20)
paper_tc.rect.x = 30
paper_tc.rect.y = 30
paper_tc.material = MATERIAL[0]
# metal_tc = TrashCan(COLORS_TC[1], 20, 20)
# metal_tc.rect.x = 810
# metal_tc.rect.y = 30
# metal_tc.material = MATERIAL[1]
glass_tc = TrashCan(COLORS_TC[2], 20, 20)
glass_tc.rect.x = 30
glass_tc.rect.y = 570
glass_tc.material = MATERIAL[2]
organic_tc = TrashCan(COLORS_TC[3], 20, 20)
organic_tc.rect.x = 810
organic_tc.rect.y = 570
organic_tc.material = MATERIAL[3]
plastic_tc = TrashCan(COLORS_TC[4], 20, 20)
# plastic_tc.rect.x = 420
# plastic_tc.rect.y = 300
plastic_tc.rect.x = 810
plastic_tc.rect.y = 30
plastic_tc.material = MATERIAL[4]
sprites_list2.add(paper_tc)
# sprites_list2.add(metal_tc)
sprites_list2.add(glass_tc)
sprites_list2.add(organic_tc)
sprites_list2.add(plastic_tc)
personagem.trashcan_group = sprites_list2

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

    # Update:
    objectGroup.update()
    sprites_list.update()

    # Draw:
    display.fill([152, 250, 239])
    objectGroup.draw(display)
    sprites_list.draw(display)
    sprites_list2.draw(display)
    pygame.display.flip()
    pygame.display.update()
