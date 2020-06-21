from ...models.player.player import Player
from .. import Controller


class PlayerController(Controller):
    def __init__(self):
        super().__init__(Player)
