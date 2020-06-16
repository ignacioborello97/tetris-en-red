from functools import partial
from flask import request, jsonify, make_response
from .game_subject import GameSubject
from .. import error_404, error_500, error_400
from ...index import app, socketio
from ...controllers.game.game import GameController

game_subjects = []

# Lista los juegos existentes en ejecucion
@app.route('/game', methods=['GET'])
def list_games():
    gameController = GameController()
    try:
        return jsonify(gameController.list_games())
    except:
        return error_500(None)


def game_ping(game_id, data):
    print(' : '+data)
    socketio.emit('ping_response', 'te respondo wey',
                  namespace='/game/'+game_id)


# Crea un nuevo juego y lo devuelve como JSON
@app.route('/game', methods=['POST'])
def create_game():
    gameController = GameController()
    try:
        data = request.json
        game = gameController.create_game()
        game_subject = GameSubject(game.id)
        game_subjects.append(game_subject)
        return jsonify(game.json())
    except Exception as error:
        return error_400(error.args[0])

# Devuelve el juego con el id correspondiente como JSON o 404 si no esta
@app.route('/game/<string:id>', methods=['GET'])
def get_game(id):
    gameController = GameController()
    try:
        game = gameController.get_game(id)
        if game is not None:
            return game.json()
        else:
            return error_404('Game Not Found')
    except:
        return error_500(None)

# Devuelve una lista de los jugadores del juego con el id correspondiente como JSON o 404 si no esta
@app.route('/game/<string:id>/players', methods=['GET'])
def get_game_players(id):
    gameController = GameController()
    try:
        game = gameController.get_game(id)
        if game is not None:
            return jsonify([player.json() for player in game.players])
        else:
            return error_404('Game Not Found')
    except:
        return error_500(None)

# Agrega el jugador con el id pasado por body en el juego del id correspondiente y lo retorna como JSON o 404 si no existe
@app.route('/game/<id>/players', methods=['POST'])
def add_game_player(id):
    gameController = GameController()
    try:
        data = request.json
        player = gameController.add_player(id, data["id"])
        if player is not None:
            return player.json()
        else:
            return error_404('Game Not Found')
    except Exception as e:
        print(e.args)
        return error_500(e.args)
