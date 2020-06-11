from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('connect')
def test_connect():
    print('connect !!!!')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('key_press')
def handle_key_press(arg):
    print('key_press')
    print(arg)

    res = ''
    if(arg == 'left'):
        res = '<'
    if(arg == 'right'):
        res = '>'
    if(arg == 'down'):
        res = 'v'
    if(arg == 'x'):
        res = '|>'
    if(arg == 'z'):
        res = '<|'

    emit('return_key_press', res)

socketio.run(app)

from .views.game import game
from .views.player import player

@app.route('/')
def hello_world():
    return 'Hello, World!'