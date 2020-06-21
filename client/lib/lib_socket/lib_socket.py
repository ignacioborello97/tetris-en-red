import socketio
import threading
from pynput import keyboard

# DEFINICION DEL SOCKET
sio = socketio.Client()


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
        sio.emit('key_press', {"key": key,
                               "player_id": self.player}, self.namespace)

    def ready(self):
        sio.emit('ready', {"player_id": self.player}, self.namespace)

    def next(self, channel, data):
        for observer in self.observers:
            if(channel == "game_state"):
                observer.update_game_state(data)

            if(channel == "board_state"):
                observer.update_board_state(data)

    def update_piece_fall(self):
        sio.emit('piece_fall', {"player_id": self.player}, self.namespace)


class GameObserver:
    def __init__(self):
        # aca adentro creo que meteria el game
        self.subjects = []
        self.player_boards = {}
        self.player_states = {}

    def observe(self, subject):
        subject.add_observer(self)
        self.subjects.append(subject)

    def update_game_state(self, data):
        if(data["game_state"] == "STARTED"):
            threading.Timer(1.5, self.make_piece_fall).start()
        # ver que hacer con los otros estados

    def update_board_state(self, data):
        player_id = data["player_id"]
        positions = data["board_state"]
        player_state = data["player_state"]

        self.player_boards[player_id] = positions
        self.player_states[player_id] = player_state

        for player in self.player_states.keys():
            header = '      ' + self.player_states[player]['name']
            for llenar in range(10 - len(self.player_states[player]['name'])):
                header += ' '

        header += '\n'

        output = ''
        for rowi, row in enumerate(positions):
            for player in self.player_boards.keys():
                output += '      '
                for x, y, shape in self.player_boards[player][rowi]:
                    output += shape
            output += '\n'
        output += '\n\n'

        print(header)
        print(output)

    def make_piece_fall(self):
        level_time_lambda = 0  # esto seria la variable que cambia en base al nivel
        for subject_observer in self.subjects:
            subject_observer.update_piece_fall()
        threading.Timer(1.5 - level_time_lambda, self.make_piece_fall).start()


id = input('Enter your game id: ')
player_1 = input('Enter id player 1: ')
player_2 = input('Enter id player 2: ')

# CONECTAR EL SOCKET AL SERVER Y QUE TOME EL CANAL DEL JUEGO ('/game/'+id)
sio.connect('http://localhost:5000', namespaces=['/game/'+id])

# DEFINIS EL GAME SUBJECT
game_channel_cliente_1 = GameNamespace('/game/'+id)
game_channel_cliente_2 = GameNamespace('/game/'+id)
# ASIGNAS EL JUGADOR AL OBJETO
game_channel_cliente_1.set_player(player_1)
game_channel_cliente_2.set_player(player_2)
# ENCHUFAR EL SUBJECT AL socketio
sio.register_namespace(game_channel_cliente_1)
sio.register_namespace(game_channel_cliente_2)

# CREAS UN OBSERVER DEL JUEGO
game_observer = GameObserver()
# PONES AL OBSERVER A MIRAR LOS EVENTOS
game_observer.observe(game_channel_cliente_1)
game_observer.observe(game_channel_cliente_2)


def on_press(key):

    key_player_1 = False
    key_player_2 = False

    key_send = ''
    try:
        if(key.char == 'z'):
            key_send = 'z'
            key_player_1 = True
        if(key.char == 'x'):
            key_send = 'x'
            key_player_1 = True

        # player 2
        if(key.char == 'a'):
            key_send = 'left'
            key_player_2 = True
        if(key.char == 'd'):
            key_send = 'right'
            key_player_2 = True
        if(key.char == 's'):
            key_send = 'down'
            key_player_2 = True
        if(key.char == 'j'):
            key_send = 'z'
            key_player_2 = True
        if(key.char == 'k'):
            key_send = 'x'
            key_player_2 = True

    except AttributeError:
        if(key == keyboard.Key.right):
            key_send = 'right'
            key_player_1 = True
        if(key == keyboard.Key.left):
            key_send = 'left'
            key_player_1 = True
        if(key == keyboard.Key.down):
            key_send = 'down'
            key_player_1 = True
        if(key == keyboard.Key.enter):
            key_send = 'enter'
            key_player_1 = True
        # player 2
        if(key == keyboard.Key.space):
            key_player_2 = True
            key_send = 'enter'

    if(key_player_1):
        if (key_send == 'enter'):
            game_channel_cliente_1.ready()
            # change behavior
        else:
            game_channel_cliente_1.press_key(key_send)

    if(key_player_2):
        if (key_send == 'enter'):
            game_channel_cliente_2.ready()
            # change behavior
            pass
        else:
            pass
            game_channel_cliente_2.press_key(key_send)


listener = keyboard.Listener(
    on_press=on_press)
listener.start()


# PROBAR COMO FUNCA ESTO!!!!!!!!!!!!!!!!
