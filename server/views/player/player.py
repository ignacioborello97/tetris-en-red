from flask import request, jsonify
from .. import error_400, error_404, error_500
from ...index import app
from ...controllers.player.player import PlayerController

@app.route('/player', methods=['POST'])
def create_player():
    playerController = PlayerController()
    try:
        data = request.json
        player = playerController.create_player(data)
        return jsonify(player.json())
    except Exception as error:
        return error_400(error.args[0])

@app.route('/player', methods=['GET'])
def list_players():
    playerController = PlayerController()
    try:
        return jsonify(playerController.list_players())
    except:
        return error_500(None)

@app.route('/player/<string:id>', methods=['GET'])
def get_player(id):
    playerController = PlayerController()
    try:
        player = playerController.get_player(id)
        if player is not None:
            return player.json()
        else:
            return error_404('Player Not Found')
    except:
        return error_500(None)
    