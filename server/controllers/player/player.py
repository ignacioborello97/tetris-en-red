from ...models.player.player import Player

class PlayerController:
    
    player_list = []
    
    def __init__(self):
        pass

    def create_player(self, player_json):
        if "name" in player_json and "avatar" in player_json:
            if type(player_json["name"]) == str:
                new_player = Player(player_json["name"], player_json["avatar"])
                PlayerController.player_list.append(new_player)
                return new_player
            else:
                raise Exception('name must be a string')
        else:
            raise Exception('missing parameter')
    
    def get_player(self, player_id):
        for player in PlayerController.player_list:
            if player.id == player_id:
                return player
        return None
        
    def list_players(self):
        return [player.json() for player in PlayerController.player_list]
