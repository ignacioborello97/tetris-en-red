import pygame
import sys
from pygame.locals import *
from views import ViewBuilder


class informationViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title='', buttons=[], texts=[], menuView=None):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.screen.fill(self.bg)
        self.buttons = buttons
        self.texts = texts
        self.menuView = menuView

    def run(self):
        while True:

            for b in self.buttons:
                b.draw(self.screen)

            for t in self.texts:
                t.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                for b in self.buttons:
                    b.handle_event(event)

            pygame.display.update()
