"""
The game Class provides the functionality to store game data in the cloud
via google worksheets.
"""
from datetime import datetime


class Game:
    """ Game data storage """
    def __init__(self, board, player, xo):
        self.id = datetime.now()
        self.board = board
        self.player = player
        self.xo = xo
        self.winner = ""
        self.no_of_moves = 0
        self.start = self.id
        self.end = 0
        # self.duration = timedelta(self.start, self.end)
