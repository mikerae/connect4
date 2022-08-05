"""
The game Class provides the functionality to store game data in the cloud
via google worksheets.
"""
from datetime import datetime
from slugify import slugify
# from run import display_board


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

    def final_update(self, board):
        """ Add final data to game object """
        self.board = board
        self.end = datetime.now()
        self.duration = 0

    def display_game_data(self):
        """ Displays final game data in terminal"""
        print(f'The winner was : {self.winner}')
        print(f'You payed {self.xo}')
        print(f'You made {self.moves} moves.')
        print(f'Your game ID is: {self.id}')
        print(f'The game started at {self.start}')
        print(f'The game ended at {self.end}')
        print(f'The raw board data is {self.board}')
        # print(f'The game lasted {game.duration}')
