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
        self.start = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self._end = ""
        self._duration = ""
        self._id = slugify(str(datetime.now()))

    def final_update(self, board):
        """ Add final data in string form to game object:
        The final state of board,
        The end time of the game,
        The calculated duration of the game in minuets and seconds
        """
        self.board = board
        self._end = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        # Calculate and set game duration
        start_dt = datetime.strptime(self.start, "%d/%m/%Y, %H:%M:%S")
        end_dt = datetime.strptime(self._end, "%d/%m/%Y, %H:%M:%S")
        delta = end_dt - start_dt
        delta_min_sec = divmod(delta.total_seconds(), 60)
        self._duration = f'{int(delta_min_sec[0])}m {int(delta_min_sec[1])}s'

    def display_game_data(self):
        """ Displays final game data in terminal"""
        print(f'Game ID: {self._id}')
        print(f'The human player was: {self.player}')
        print(f'{self.player} played: {self.xo}')
        print(f'The winner was: {self.winner}')
        print(f'{self.player} made {self.moves} moves.')
        print(f'The game started at {self.start}')
        print(f'The game ended at {self._end}')
        print(f'The game lasted {self._duration}')
        print(f'The raw board data is {self.board}')
