import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, text_input, font, size, base_color, hovering_color):
        super().__init__()

        self.image = image
        self.x_pos = x
        self.y_pos = y
        self.font = pygame.font.Font(font, size)
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def add_text(self, text):
        self.text = text

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def change_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
