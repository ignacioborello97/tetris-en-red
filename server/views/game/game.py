from functools import partial
from flask import request, jsonify, make_response
from .game_namespace import GameNamespace
from .. import error_404, error_500, error_400
from ...index import app, socketio
from ...controllers.game.game import GameController
from ...controllers.player.player import PlayerController
from ...models.game.game import Game

game_subjects = []
game_namespaces = []

gameControl = GameController()
playerControl = PlayerController()


@app.route('/game', methods=['POST'])
def game_test():
    game = gameControl.set(None, data={})
    game_namespace = GameNamespace(game.id)
    game_namespaces.append(game_namespace)
    return game.json()


@app.route('/game', methods=['GET'])
def get_game_test():
    games = jsonify(gameControl.list())
    return games

# Devuelve el juego con el id correspondiente como JSON o 404 si no esta
@app.route('/game/<string:id>', methods=['GET'])
def get_game_test_id(id):
    try:
        game = gameControl.get(id)
        if game is not None:
            return game.json()
        else:
            return error_404('Game Not Found')
    except:
        return error_500(None)

# Devuelve una lista de los jugadores del juego con el id correspondiente como JSON o 404 si no esta
@app.route('/game/<string:id>/players', methods=['GET'])
def get_game_players_test(id):
    try:
        game = gameControl.get(id)
        if game is not None:
            return jsonify([player.json() for player in game.players])
        else:
            return error_404('Game Not Found')
    except:
        return error_500(None)

# Agrega el jugador con el id pasado por body en el juego del id correspondiente y lo retorna como JSON o 404 si no existe
@app.route('/game/<id>/players', methods=['POST'])
def add_game_player_test(id):
    try:
        data = request.json
        game = gameControl.get(id)
        player = playerControl.get(data['id'])
        if player is not None:
            game.players.append(player)
            return player.json()
        else:
            return error_404('Game Not Found')
    except Exception as e:
        return error_500(e.args)
