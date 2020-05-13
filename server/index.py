from flask import Flask
app = Flask(__name__)

from .views.game import game
from .views.player import player

@app.route('/')
def hello_world():
    return 'Hello, World!'

