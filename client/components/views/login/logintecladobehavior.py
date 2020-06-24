import pygame
from ..keyboard_behavior.keyboard_behavior import keyboardBehavior

class loginKeyboardBehavior(keyboardBehavior):

    def __init__(self):
        self.key_list = []
        self.button_list = []
        self.cont_button = 0
        self.position = self.button_list[0]

    def add_keys(self, key_list):
        for keys in key_list:
            self.key_list.append(keys)
    
    def add_buttons(self, button_list):
        for buttons in button_list:
            self.button_list.append(buttons)

    # def press_key(self, key):
    #     if key == 'down':
    #         self.cont_button += 1
    #         if self.cont_button == len(self.button_list):
    #             self.cont_button = 0
    #         self.position = self.button_list[self.cont_button]
    #     if key == 'enter':
    #         if self.position.action != None:
    #             if self.position.action2 != None:
    #                 self.position.action2()
    #             self.position.action()
        
        
            
        



        

       
       
# for event in pygame.event.get():
#                 if event.type == QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         key = 'left'
#                         self.press_key(key)
#                     if event.key == pygame.K_RIGHT:
#                         key = 'right'
#                         self.press_key(key)
#                     if event.key == pygame.K_DOWN:
#                         key = 'down'
#                         self.press_key(key)
#                     if event.key == pygame.K_z:
#                         key = 'z'
#                         self.press_key(key)
#                     if event.key == pygame.K_x:
#                         key = 'x'
#                         self.press_key(key)

    