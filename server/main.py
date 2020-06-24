from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/") 
def home_view(): 
    return "<h1>Tetris en red!!!</h1>"
