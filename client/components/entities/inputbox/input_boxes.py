import pygame
from ..colors.colores import *

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.font = pygame.font.SysFont('comicsansms', 32)
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = black
        self.color_active = red
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.user_name = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.user_name = self.text                   
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        # if self.txt_surface.get_width()+10 < 200:
        #     self.rect.w = width
        # else: self.rect.w = 200

    def draw(self, screen):
        pygame.draw.rect(screen, white, self.rect)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
    
    def get_username(self):
        return self.text