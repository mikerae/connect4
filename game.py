"""
The game Class provides the functionality to store game data in the cloud
via google worksheets.
"""
from datetime import datetime
from random import randint
from slugify import slugify
from colorama import Fore


class Game:
    """ Game data storage """
    def __init__(self, board, player, xo):
        self._id = slugify(str(datetime.now()))
        self.player = player
        self.xo = xo
        self.winner = ""
        self.moves = 0
        self.start = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self._end = ""
        self._duration = 0.0
        self.board = board

    def welcome(self):
        """ Initial Instructions """
        print(f'To win, join four {self.xo}s:\n\
horizontaly, verticaly or diagonaly.\n\
Good Luck {self.player}!')

    def process_win(self, winner, PLAYER, draw):
        """ Displays winner message """
        if draw:
            print(Fore.WHITE + f'Its a draw! Nice game {self.player}.')
            self.winner = "draw"
        elif PLAYER == winner:
            print(Fore.WHITE + f'{self.player}, you have won!\n')
            self.winner = self.player
        else:
            print(Fore.WHITE + 'I won this time!')
            print(f'Better luck next time {self.player}!\n')
            self.winner = "Computer"

    def final_update(self, board):
        """ Add final data in string form to game object:
        The final state of board,
        The end time of the game,
        The calculated duration of the game in minuets and seconds
        """
        self.board = board
        self._end = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        # Calculate and set game duration (in seconds)
        start_dt = datetime.strptime(self.start, "%d/%m/%Y, %H:%M:%S")
        end_dt = datetime.strptime(self._end, "%d/%m/%Y, %H:%M:%S")
        delta = end_dt - start_dt
        self._duration = delta.total_seconds()

    def display_game_data(self):
        """ Displays final game data in terminal"""
        print(Fore.WHITE + f'Game ID: {self._id}')
        print(f'The game was played by: {self.player}')
        print(f'{self.player} played: {self.xo}' + Fore.WHITE)
        print(f'The winner was: {self.winner}')
        print(f'{self.player} made {self.moves} moves.')
        print(f'The game started at {self.start}')
        print(f'The game ended at {self._end}')
        delta_min_sec = divmod(float(self._duration), 60)
        mins = int(delta_min_sec[0])
        secs = int(delta_min_sec[1])
        print(f'The game lasted {mins}m {secs}s')
        display_board(self.board)

    def write_game_data(self, SHEET):
        """
        Stores current game data in a
        google whorsheet (connect4) on
        google drive. Solution to storing board
        list from Stack Overflow (https://stackoverflow.
        com/questions/34400635/
        how-to-write-a-table-list-of-lists-
        to-google-spreadsheet-using-gspread)
        """
        SHEET.add_worksheet(self._id, rows=15, cols=7)
        worksheet = SHEET.worksheet(self._id)
        game_data = [
            ["game_id", self._id],
            ["player", self.player],
            ["xo", self.xo],
            ["winner", self.winner],
            ["moves", self.moves],
            ["start", self.start],
            ["end", self._end],
            ["duration", self._duration]
        ]
        worksheet.update(game_data)
        # Code from @Burnash (gspread developer)
        SHEET.values_update(
            f'{self._id}!A10',
            params={'valueInputOption': 'RAW'},
            body={'values': self.board}
        )

    def read_game_data(self, worksheet):
        """ Reads game data into game object """
        self._id = worksheet.acell('B1').value
        self.player = worksheet.acell('B2').value
        self.xo = worksheet.acell('B3').value
        self.winner = worksheet.acell('B4').value
        self.moves = worksheet.acell('B5').value
        self.start = worksheet.acell('B6').value
        self._end = worksheet.acell('B7').value
        self._duration = worksheet.acell('B8').value
        self.board = worksheet.get_values("A10:G15")


def build_empty_board(board):
    """ Initialises empty board"""
    for row in range(6):
        row = ["-"] * 7
        board.append(row)
    return board


def display_board(board):
    """ Displays the current state of the board """
    dec_row = ("----" * 7) + "-\n"
    col_nums = "  1   2   3   4   5   6   7"
    board_row = ""
    print(Fore.BLUE + dec_row)
    print(Fore.WHITE + col_nums)
    for row in board:
        for cell in row:
            board_row += f'| {cell} ' + Fore.BLUE
        board_row += Fore.BLUE + "|\n"
    print(Fore.BLUE + board_row)
    print(dec_row)


def check_player_input(column, columns):
    """
    Checks if white space or "" is input
    Checks chosen column is string in range 1 - 7
    Checks if chosen column is full
    """
    try:
        if column == "" or column.isspace():
            raise ValueError(
                'Please choose a column between 1 and 7'
            )
        elif int(column) not in range(1, 8):
            raise ValueError(
                'Please choose a column between 1 and 7'
            )
        elif len(columns[int(column) - 1]) >= 6:
            raise ValueError(
                f'Column {column} is full, please choose another column'
            )
        else:
            return True
    except ValueError as e:
        print(f'{e}')
        return False


def player_move(board, columns, player_xo, column_full):
    """ Player makes a move"""
    display_board(board)
    column = (input(Fore.WHITE + "Choose column 1 - 7: \n"))
    if check_player_input(column, columns):
        columns[int(column) - 1].push(player_xo)
        board[6 - len(columns[int(column) - 1])][int(column) - 1] = \
            columns[int(column) - 1].peek()
        if len(columns[int(column) - 1]) >= 6:
            column_full.append(True)
    else:
        player_move(board, columns, player_xo, column_full)
    return board, columns, column_full


def computer_move(board, columns, computer_xo, column_full):
    """ Computer makes a move """
    col = randint(0, 6)
    if len(columns[col]) < 6:
        columns[col].push(computer_xo)
        board[6 - len(columns[col])][col] = \
            columns[col].peek()
        if len(columns[col]) >= 6:
            column_full.append(True)
    else:
        computer_move(board, columns, computer_xo, column_full)
    return board, columns, column_full


def check_win(board, xo, turn):
    """ Check if win conditions are met """
    result = False
    # Horizonatal check
    for row in range(6):
        for col in range(4):
            if board[5 - row][col] == board[5 - row][col + 1] ==\
                    board[5 - row][col + 2] == board[5 - row][col + 3] == xo:
                result = True
                break
    # Verticle check
    for col in range(7):
        for row in range(4):
            if board[5 - row][col] == board[5 - (row + 1)][col] ==\
                    board[5 - (row + 2)][col] ==\
                    board[5 - (row + 3)][col] == xo:
                result = True
                break
    # +ve slope Diagonal or -ve slope Diagonal check
    for row in range(6):
        for col in range(4):
            if board[5 - row][col] ==\
                    board[5 - (row + 1)][col + 1] ==\
                    board[5 - (row + 2)][col + 2] ==\
                    board[5 - (row + 3)][col + 3] == xo or\
                    board[5 - row][col + 3] ==\
                    board[5 - (row + 1)][col + 2] ==\
                    board[5 - (row + 2)][col + 1] ==\
                    board[5 - (row + 3)][col] == xo:
                result = True
                break
    return result, turn


def check_draw(column_full):
    """ Check for draw """
    draw = False
    if len(column_full) >= 7:
        draw = True
    return draw
