import pygame.sprite
from personagem import Personagem
from ambiente import Blockage

# Cores usadas (testes de rects)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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
    pygame.display.flip()
    pygame.display.update()
