from ...models.game.game import Game
from ..player.player import PlayerController

class GameController:
    
    game_list = []
    
    def __init__(self):
        pass

    def create_game(self):
        new_game = Game()
        GameController.game_list.append(new_game)
        return new_game

    def add_player(self, game_id, player_id):
        playerController = PlayerController()
        player = playerController.get_player(player_id)
        if player is None:
            raise Exception('Player Not Found')
        game = self.get_game(game_id)
        if game is None:
            raise Exception('Game Not Found')
        
        game.add_player(player)
        return player
        
    def get_game(self, game_id):
        for game in GameController.game_list:
            if game.id == game_id:
                return game
        return None

    def list_games(self):
        return [game.json() for game in GameController.game_list]

