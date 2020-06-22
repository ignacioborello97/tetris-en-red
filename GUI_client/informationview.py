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
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)
        self.buttons = []
        self.texts = []
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
    
    def create(self):
        backButton = Button('<------', 30, 250, 100, 40, white,
                        (200, 200, 200), 3, main_menu_screen)
        self.buttons = [backButton]

        t1 = Text('Tetris en Red', 60, black, 200, 40)
        t2 = Text('Tetricos', 50, black, 200, 110)
        t3 = Text('Copyright © 2020-2020', 20, black, 200, 180)
        t4 = Text('Version 1.0.0 - Build 1', 20, black, 200, 210)
        self.texts = [t1, t2, t3, t4]
