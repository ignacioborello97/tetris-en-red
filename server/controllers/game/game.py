from ...models.game.game import Game
from ...controllers import Controller


class GameController(Controller):
    def __init__(self):
        super().__init__(Game)
