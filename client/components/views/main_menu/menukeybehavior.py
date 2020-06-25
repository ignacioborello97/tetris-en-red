from ..keyboard_behavior.keyboard_behavior import keyboardBehavior
import pygame

class menuKeyboardBehavior(keyboardBehavior):

    def __init__(self):
        self.button_list = []
        self.cont_button = 0
    
    def add_buttons(self, button_list):
        for buttons in button_list:
            self.button_list.append(buttons)

    def handle_event(self,key):
        if key == 'down':
            self.cont_button += 1
            if self.cont_button == len(self.button_list):
                self.cont_button = 0
            self.position = self.button_list[self.cont_button]
        if key == 'up':
            self.cont_button -= 1
            if self.cont_button == -1:
                self.cont_button = len(self.button_list) - 1
            self.position = self.button_list[self.cont_button]
        if key == 'enter':
            self.position.do_action()

    def draw_indicador(self,surface):
        self.position = self.button_list[self.cont_button]
        x = self.position.x - (self.position.w)/4
        y = self.position.y + self.position.h/3
        pygame.draw.polygon(surface, (20,20,20), ((x, y),(x + (self.position.w)/6, y + (self.position.h)/4), (x, y + (self.position.h)/2)))
        pygame.draw.polygon(surface, (255,255,255), ((x, y),(x + (self.position.w)/6, y + (self.position.h)/4), (x, y + (self.position.h)/2)),2)