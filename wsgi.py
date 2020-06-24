from server.main import app ,socketio
  
if __name__ == "__main__": 
    socketio.run(app)

from server.views.game import game
from server.views.player import player