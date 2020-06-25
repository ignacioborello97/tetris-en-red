from ..keyboard_behavior.keyboard_behavior import keyboardBehavior

class configKeyboardBehavior(keyboardBehavior):

    def __init__(self,function=None):
        self.function = function
        self.musicOnAction = None
        self.musicOffAction = None
        self.backAction = None
    
    def handle_event(self,key):
        if key == 'p':
            self.musicOffAction()
        if key == 'espacio':
            self.musicOnAction()
        if key == 'enter':
            self.function()
        if key == 'escape':
            self.backAction()     

    def setBackAction(self,action):
        self.backAction = action

    def setMusicOnAction(self,action):
        self.musicOnAction = action

    def setMusicOffAction(self,action):
        self.musicOffAction = action
