from flask import request, jsonify
from .. import error_400, error_404, error_500
from ...index import app
from ...controllers.player.player import PlayerController

playerControl = PlayerController()


@app.route('/player', methods=['POST'])
def player_test():
    try:
        data = request.json
        player = playerControl.set(None, data)
        return jsonify(player.json())
    except Exception as error:
        return error_400(error.args[0])


@app.route('/player', methods=['GET'])
def get_player_test():
    try:
        return jsonify([player.json() for player in playerControl.list()])
    except Exception as error:
        return error_400(error.args[0])


@app.route('/player/<string:id>', methods=['GET'])
def get_player_test_id(id):
    try:
        player = playerControl.set(None, data)
        if player is not None:
            return player.json()
        else:
            return error_404('Player Not Found')
    except:
        return error_500(None)
