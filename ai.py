"""
AI code derived from Keith Galli: How to Program a Connect 4 AI
(https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6)
and adapted as approriate. See Readme
"""
import random
import math
from colorama import Fore
from game import check_win

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


def evaluate_window(window, xo):
    score = 0
    if xo == xo_X:
        opp_xo = xo_O
    else:
        opp_xo = xo_X

    if window.count(xo) == 4:
        score += 100
    elif window.count(xo) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(xo) == 2 and window.count(EMPTY == 2):
        score += 2

    if window.count(opp_xo) == 3 and window.count(EMPTY) == 1:
        score -= 4
    return score


def pick_best_move(board, xo):  # heuristic value of node
    """ Calculate the best column for next move
    assuming depth is zero for minimax() """
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = [x[:] for x in board]
        drop_xo(temp_board, row, col, xo)
        score = score_position(temp_board, xo)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col


def score_position(board, xo):
    """ Calculates board Static Scoring Method """
    score = 0

    # Score Centre Column
    center_array = []
    for row in board:
        cell = row[COLUMN_COUNT//2]
        center_array.append(cell)
    center_count = center_array.count(xo)
    score += center_count * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = board[(ROW_COUNT-1) - r]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c: (c + WINDOW_LENGTH)]
            score += evaluate_window(window, xo)

    # Score Verticle
    for c in range(COLUMN_COUNT):
        col_array = []
        for row in board:
            cell = row[c]
            col_array.append(cell)
        col_array.reverse()
        for r in range(ROW_COUNT - 3):
            window = col_array[r: (r + WINDOW_LENGTH)]
            score += evaluate_window(window, xo)

    # Score Positive Sloped Diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[((ROW_COUNT-1) - r) - i][c + i]
                      for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, xo)

    # Score Negetively Sloped Diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[(ROW_COUNT-1) - (3 + r) + i][c + i]
                      for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, xo)
    return score


def is_terminal_node(board, xo):
    check_win_tuple = check_win(board, xo)
    return check_win_tuple[WIN] or len(get_valid_locations(board)) == 0


def minimax(board, depth, alpha, beta, maximizing_player, xo):
    """ returns best column and the score for the board for this
    column """

    # The minimax algorithm requires that the initial call has
    # maximizing_player set to True => the initial value for xo is
    # computor_xo
    if xo == xo_X:
        computer_xo = xo_X
        player_xo = xo_O
    else:
        computer_xo = xo_O
        player_xo = xo_X

    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board, xo)
    win_comp = check_win(board, computer_xo)[1]
    win_ply = check_win(board, player_xo)[1]
    if depth == 0 or is_terminal:
        if is_terminal:
            if win_comp:  # Edgecase: Computor wins
                # col = check_win_comp[COL]
                return (None, 10000000000000000)
            elif win_ply:  # Edgecase: Player wins
                # col = check_win_ply[COL]
                return (None, -10000000000000000)
            else:  # Draw
                # draw_move = pick_best_move(board, xo)
                return (None, 0)
        else:  # depth is zero
            # best_move = pick_best_move(board, xo)
            # score = score_position(board, computer_xo)
            return (None, score_position(board, computer_xo))

    if maximizing_player:
        value = - math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [x[:] for x in board]
            drop_xo(b_copy, row, col, computer_xo)
            new_score = minimax(b_copy, depth - 1, alpha, beta,
                                False, computer_xo)[1]
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
    """ Computor AI """

    # """ Computer makes a random move """
    # col = random.randint(0, 6)
    # if len(columns[col]) < 6:
    #     columns[col].push(computer_xo)
    #     board[6 - len(columns[col])][col] = \
    #         columns[col].peek()
    #     if len(columns[col]) >= 6:
    #         column_full.append(True)
    # else:
    #     computer_move(board, columns, computer_xo, column_full)

    minimax_tuple = minimax(board, 1, -math.inf, math.inf,
                            True, computer_xo)
    col = minimax_tuple[0]
    columns[col].push(computer_xo)
    board[6 - len(columns[col])][col] = \
        columns[col].peek()
    if len(columns[col]) >= 6:
        column_full.append(True)
    return board, columns, column_full
