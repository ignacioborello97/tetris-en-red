from ..keyboard_behavior.keyboard_behavior import keyboardBehavior

class playKeyboardBehavior(keyboardBehavior):

    def __init__(self,function=None):
        self.function = function
    
    def handle_event(self,key):
        if key == 'left':
            self.function('left')
        if key == 'right':
            self.function('right')
        if key == 'down':
            self.function('down')
        if key == 'z':
            self.function('z')        
        if key == 'x':
            self.function('x')

    