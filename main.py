
import pygame
import pygame.sprite
from personagem import personagem

# Inicializando o Pygame e Criando a Janela do Jogo

pygame.init()
display = pygame.display.set_mode([840, 600])
pygame.display.set_caption("Super Lixo")

#Objetos

objectGroup = pygame.sprite.Group()
personagem = personagem(objectGroup)



#Música de fundo do jogo

pygame.mixer.music.load("dados/Juhani Junkala [Chiptune Adventures] 1. Stage 1.wav")
pygame.mixer.music.play(-1)

#Efeitos sonoros

andando = pygame.mixer.Sound("dados/Fantozzi-StoneR1.FLAC")

gameLoop = True
clock = pygame.time.Clock()

# Criando o botão de fechar no X

while gameLoop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

# Criando o reconhecimento de teclas precionadas!

    isPressingWDAS = False

    #Update:

    objectGroup.update()

    #Draw:

    display.fill([152, 250, 239])
    objectGroup.draw(display)
    pygame.display.update()