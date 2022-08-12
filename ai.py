"""
AI code derived from Keith Galli: How to Program a Connect 4 AI
(https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6)
and adapted as approriate. See Readme
"""
import random
import math
from colorama import Fore
from game import check_win, display_board

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = "-"
xo_X = Fore.RED + "X" + Fore.WHITE
xo_O = Fore.YELLOW + "O" + Fore.WHITE
WIN = 1
COL = 0


def get_next_open_row(board, col):
    """ For a given column, gets the next available row """
    for r in range(ROW_COUNT):
        if board[5 - r][col] == EMPTY:
            break
    return 5 - r


def drop_xo(board, row, col, xo):
    """ Populates the board with the next piece
    for the purposes of minimax only """
    board[row][col] = xo
    return board


def evaluate_window(window, xo, computer_xo):
    score = 0

    # Set player_xo
    if computer_xo == xo_X:
        player_xo = xo_O
    else:
        player_xo = xo_X

    opp_xo = player_xo
    if xo == player_xo:
        opp_xo = computer_xo

    if window.count(xo) == 4:
        score += 100
    elif window.count(xo) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(xo) == 2 and window.count(EMPTY == 2):
        score += 2

    if window.count(opp_xo) == 3 and window.count(EMPTY) == 1:
        score -= 4
    return score


def score_position(board, xo, computer_xo):
    """ Calculates board Static Scoring Method """
    score = 0

    # Score Centre Column
    center_array = []
    for row in board:
        cell = row[COLUMN_COUNT//2]
        center_array.append(cell)
    center_count = center_array.count(xo)
    score += center_count * 4

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = board[(ROW_COUNT-1) - r]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c: (c + WINDOW_LENGTH)]
            score += evaluate_window(window, xo, computer_xo)

    # Score Verticle
    for c in range(COLUMN_COUNT):
        col_array = []
        for row in board:
            cell = row[c]
            col_array.append(cell)
        col_array.reverse()
        for r in range(ROW_COUNT - 3):
            window = col_array[r: (r + WINDOW_LENGTH)]
            score += evaluate_window(window, xo, computer_xo)

    # Score Positive Sloped Diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[((ROW_COUNT-1) - r) - i][c + i]
                      for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, xo, computer_xo)

    # Score Negetively Sloped Diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[(ROW_COUNT-1) - (3 + r) + i][c + i]
                      for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, xo, computer_xo)
    return score


def set_ply_xo(computer_xo):
    """ set value for player_xo """

    if computer_xo == xo_X:     # Sets player_xo
        player_xo = xo_O
    else:     # Sets player_xo
        player_xo = xo_X
    return player_xo


def is_terminal_node(board, computer_xo):
    """ Checks for win or draw """

    player_xo = set_ply_xo(computer_xo)
    win_ply = check_win(board, computer_xo)[1]
    win_com = check_win(board, player_xo)[1]
    draw = len(get_valid_locations(board)) == 0
    return win_ply or win_com or draw


def minimax(board, depth, alpha, beta, maximizing_player, computer_xo):
    """ returns best column and the score for the board for this
    column using minimax algorithm with alpha beta pruning"""

    player_xo = set_ply_xo(computer_xo)
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board, computer_xo)
    win_com = check_win(board, computer_xo)[1]
    win_ply = check_win(board, player_xo)[1]
    if depth == 0 or is_terminal:
        if is_terminal:
            if win_com:  # Edgecase: Computor wins
                return (None, 10000000000000000)
            elif win_ply:  # Edgecase: Player wins
                return (None, -10000000000000000)
            else:  # Draw
                return (None, 0)
        else:  # depth is zero
            return (None, score_position(board, computer_xo, computer_xo))

    if maximizing_player:
        value = - math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [x[:] for x in board]
            drop_xo(b_copy, row, col, computer_xo)
            new_score = minimax(b_copy, depth - 1, alpha, beta,
                                False, player_xo)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # Minimizing Player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [x[:] for x in board]
            drop_xo(b_copy, row, col, player_xo)
            new_score = minimax(b_copy, depth - 1, alpha, beta,
                                True, computer_xo)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def is_valid_location(board, col):
    """ Checks column choice is not full """
    return board[ROW_COUNT - 6][col] == EMPTY


def get_valid_locations(board):
    """ Make list of available columns """
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def computer_move(board, columns, computer_xo, column_full):
    """ calls AI, writes computer move to stack and board """
    print(Fore.WHITE + "My turn...")
    col = minimax(board, 4, -math.inf, math.inf,
                  True, computer_xo)[0]
    columns[col].push(computer_xo)
    board[6 - len(columns[col])][col] = \
        columns[col].peek()
    if len(columns[col]) >= 6:
        column_full.append(True)
    display_board(board)
    return board, columns, column_full
