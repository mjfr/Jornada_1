
import pygame
import random


class Trash(pygame.sprite.Sprite):
    def __init__(self, color, width, height, blockage_group, trash_can_group):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.blockage_group = blockage_group
        self.trash_can_group = trash_can_group
        self.character_group = None
        self.material = None

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.spawn_trash()

    def update(self):
        keys = pygame.key.get_pressed()
        # Verificando se o personagem colidiu com o lixo e apertou a tecla de ação
        if pygame.sprite.spritecollide(self, self.character_group, False) and keys[pygame.K_e]:
            # Atribuindo o material do lixo a uma variável que o personagem está segurando
            if self.character_group.sprites()[0].holding is None:
                self.character_group.sprites()[0].holding = self.material
                self.kill()
            else:
                # TODO: Fazer com que haja algum aviso, seja visual ou auditivo para indicar
                print("Pode segurar apenas um lixo")

    def spawn_trash(self):
        # Enquanto o lixo não estiver em uma área disponível para spawn, ele terá sua posição alterada
        while True:
            self.rect.x = random.randint(20, 800)
            self.rect.y = random.randint(20, 550)
            # Verifica se o lixo não está colidindo com os bloqueios ou lixeiras
            if (not pygame.sprite.spritecollide(self, self.blockage_group, False) and
                    not pygame.sprite.spritecollide(self, self.trash_can_group, False)):
                break
