import pygame


class TxtBtn(pygame.sprite.Sprite):
    def __init__(self, img, x, y, text_input, font, size, base_color, hovering_color, img_size=None, img_hover=None):
        super().__init__()

        self.img_size = img_size
        self.img = None if img is None else image_loader(img, self.img_size)
        self.img_aux = self.img
        self.img_hover = None if img_hover is None else image_loader(img_hover, self.img_size)
        self.x_pos = x
        self.y_pos = y
        self.font = pygame.font.Font(font, size)
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.img is None and self.text_input is not None:
            self.img = self.text
        self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.img is not None:
            screen.blit(self.img, self.rect)
        screen.blit(self.text, self.text_rect)

    def add_text(self, text):
        self.text = text

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def change_state(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            self.img = self.img_hover
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.img = self.img_aux


def image_loader(image, size=None):
    image = pygame.image.load(image).convert_alpha()
    if size is None:
        size = (image.get_width(), image.get_height())
    return pygame.transform.scale(image, size)
