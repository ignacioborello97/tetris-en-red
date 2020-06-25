from ..keyboard_behavior.keyboard_behavior import keyboardBehavior
import pygame
from client.components.views.main_menu.menukeybehavior import menuKeyboardBehavior

class loginKeyboardBehavior(menuKeyboardBehavior):

    def __init__(self):
        super().__init__()