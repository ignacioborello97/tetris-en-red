from ..keyboard_behavior.keyboard_behavior import keyboardBehavior

class joinKeyboardBehavior(keyboardBehavior):

    def __init__(self):
        self.backAction = None
        self.joinAction = None

    def handle_event(self,key):
        if key == 'escape':
            self.backAction()
        if key == 'enter':
            self.joinAction()

    def setBackAction(self,action):
        self.backAction = action

    def setJoinAction(self,action):
        self.joinAction = action