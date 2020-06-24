from ..keyboard_behavior.keyboard_behavior import keyboardBehavior

class lobbyKeyboardBehavior(keyboardBehavior):

    def __init__(self,function=None):
        self.function = function
        self.backAction = None
        self.readyAction = None

    def handle_event(self,key):
        if key == 'escape':
            self.backAction()
        if key == 'enter':
            self.function()
            self.readyAction()

    def setBackAction(self,action):
        self.backAction = action

    def setReadyAction(self,action):
        self.readyAction = action
