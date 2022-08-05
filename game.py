"""
The game Class provides the functionality to store game data in the cloud
via google worksheets.
"""
from datetime import datetime
from slugify import slugify


class Game:
    """ Game data storage """
    def __init__(self, board, player, xo):
        self.board = board
        self.player = player
        self.xo = xo
        self.winner = ""
        self.moves = 0
        self.start = datetime.now()
        self.end = 0
        self.duration = 0
        self.id = slugify(str(self.start))
