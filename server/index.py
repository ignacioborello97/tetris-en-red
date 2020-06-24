from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

socketio.run(app)

from .views.game import game
from .views.player import player