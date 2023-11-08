import pygame
import random


class Trash(pygame.sprite.Sprite):
    def __init__(self, *groups, image, blockage_group, trash_can_group):
        """
        Construtor da classe Trash.
        :param object groups: Instância de pygame.sprite.Group() onde servirá de lista para as instâncias de Trash;
        :param str image: Caminho do sistema para a imagem;
        :param pygame.sprite.AbstractGroup blockage_group: Grupo de bloqueios da instância de Blockage;
        :param pygame.sprite.AbstractGroup trash_can_group: Grupo de lixeiras da instância de TrashCan.
        """
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 33))
        self.blockage_group = blockage_group
        self.trash_can_group = trash_can_group
        self.character_group = None
        self.material = None

        self.rect = self.image.get_rect()
        self.spawn_trash()

    def update(self) -> None:
        """
        Função de atualização das funções do objeto.
        :return: None
        """
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

    def spawn_trash(self) -> None:
        """
        Função para criar lixos em uma posição aleatória
        :return: None
        """
        # Enquanto o lixo não estiver em uma área disponível para spawn, ele terá sua posição alterada
        while True:
            self.rect.x = random.randint(20, 800)
            self.rect.y = random.randint(20, 550)
            # Verifica se o lixo não está colidindo com os bloqueios ou lixeiras
            if (not pygame.sprite.spritecollide(self, self.blockage_group, False) and
                    not pygame.sprite.spritecollide(self, self.trash_can_group, False)):
                break
