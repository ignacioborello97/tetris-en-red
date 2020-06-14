import socketio
import threading
from pynput import keyboard

sio = socketio.Client()
# sio.connect('http://localhost:5000')

class GameNamespace(socketio.ClientNamespace):
    def add_observer(self, observer):
        try:
            self.observers.append(observer)
        except:
            self.observers = [observer]

    def set_player(self, player):
        self.player = player
    
    def on_connect(self):
        print('connected to namespace '+self.namespace)
        pass

    def on_disconnect(self):
        print('disconnected from namespace '+self.namespace)
        pass

    def on_game_state(self, data):
        if "game_state" in data.keys():
            self.next("game_state", data)

    def on_board_state(self, data):
        if "board_state" in data.keys():
            self.next("board_state", data)

    def press_key(self, key):
        sio.emit('key_press', {"key":key, "player_id":self.player}, self.namespace)     

    def ready(self):
        sio.emit('ready', {"player_id":self.player}, self.namespace)

    def next(self, channel, data):
        for observer in self.observers:
            if(channel == "game_state"):
                observer.update_game_state(data)
            
            if(channel == "board_state"):
                observer.update_board_state(data)

    def update_piece_fall(self):
        sio.emit('piece_fall', {"player_id":self.player}, self.namespace)



class GameObserver:
    def __init__(self):
        #aca adentro creo que meteria el game
        self.subjects = []

    def observe(self, subject):
        subject.add_observer(self)
        self.subjects.append(subject)

    def update_game_state(self, data):
        if(data["game_state"] == "STARTED"):
            threading.Timer(1.5, self.make_piece_fall).start()
        # ver que hacer con los otros estados

    def update_board_state(self, data):
        positions = data["board_state"]

        output = '\n\n'
        for row in positions:
            output += '                                  '
            for x, y, shape in row:
                output += shape
            output += '\n'
        output += '\n\n'
        
        print(output)

    def make_piece_fall(self):
        level_time_lambda = 0 #esto seria la variable que cambia en base al nivel
        for subject_observer in self.subjects:
            subject_observer.update_piece_fall()
        threading.Timer(1.5 - level_time_lambda, self.make_piece_fall).start()


id = input('Enter your game id: ')
player = input('Enter your name: ')

print(id)

sio.connect('http://localhost:5000', namespaces=['/game/'+id])
# sio.namespaces.append('/game/'+id)
game_channel = GameNamespace('/game/'+id)
game_channel.set_player(player)
sio.register_namespace(game_channel)

game_observer = GameObserver()
game_observer.observe(game_channel)

def on_press(key):
    
    key_send = ''
    try:
        if(key.char == 'z'):
            key_send = 'z'
        if(key.char == 'x'):
            key_send = 'x'

    except AttributeError:
        if(key == keyboard.Key.right):
            key_send = 'right'
        if(key == keyboard.Key.left):
            key_send = 'left'
        if(key == keyboard.Key.down):
            key_send = 'down'
        if(key == keyboard.Key.enter):
            key_send = 'enter'

    if (key_send == 'enter'):
        game_channel.ready()
        #change behavior
    else:
        game_channel.press_key(key_send)

listener = keyboard.Listener(
    on_press=on_press)
listener.start()