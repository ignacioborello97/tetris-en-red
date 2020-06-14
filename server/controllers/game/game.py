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

    def ready_player(self, game_id, player_id):
        playerController = PlayerController()
        game = self.get_game(game_id)
        if game is not None:
            player = game.get_player(player_id)
            player_ready = playerController.ready_player(player_id)
            return player_ready
        else:
            return False

    def get_player(self, game_id, player_id):
        game = self.get_game(game_id)
        if game is not None:
            return game.get_player(player_id)
        else:
            return None

    def get_game(self, game_id):
        for game in GameController.game_list:
            if game.id == game_id:
                return game
        return None

    def list_games(self):
        return [game.json() for game in GameController.game_list]

    def get_game_ready(self, game_id):
        playerController = PlayerController()
        game = self.get_game(game_id)
        if game is not None:
            all_ready = True
            for player in game.players:
                all_ready = all_ready and playerController.is_ready_player(player.id)
            return all_ready
        else:
            return False

    def start_game(self, game_id):
        game = self.get_game(game_id)
        if game is not None:
            game.state = Game.STARTED
            return True
        else:
            return False

    def get_board(self, game_id, player_id):
        print('get_board game_id --> ',str(game_id))
        print('get_board player_id --> ',str(player_id))
        game = self.get_game(game_id)
        if game is not None and game.state == Game.STARTED:
            player = self.get_player(game_id,player_id)
            return player.board.get_board_state()

    def distribute_pieces(self, game_id):
        game = self.get_game(game_id)
        if game is not None and game.state == Game.STARTED:
            game.refresh_pieces()
            for player in game.players:
                if(not player.has_piece()):
                    piece = game.get_piece(player.count)
                    player.drop_piece(piece)
                    player.count += 1
                
            

