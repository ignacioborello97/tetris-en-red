from flask import request, jsonify, make_response
from .. import error_404, error_500, error_400
from ...index import app
from ...controllers.game.game import GameController

@app.route('/game', methods=['GET'])
def list_games():
    gameController = GameController()
    try:
        return jsonify(gameController.list_games())
    except:
        return error_500(None)

@app.route('/game', methods=['POST'])
def create_game():
    gameController = GameController()
    try:
        data = request.json
        game = gameController.create_game()
        return jsonify(game.json())
    except Exception as error:
        return error_400(error.args[0])

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

@app.route('/game/<id>/players', methods=['POST'])
def add_game_player(id):
    gameController = GameController()
    try:
        print('id : ',id)
        data = request.json
        player = gameController.add_player(id, data["id"])
        if player is not None:
            return player.json()
        else:
            return error_404('Game Not Found')
    except Exception as e:
        print(e.args)
        return error_500(e.args)