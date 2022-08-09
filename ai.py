"""
AI code derived from Keith Galli: How to Program a Connect 4 AI
(https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6)
See Readme
"""
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = "-"


def get_next_open_row(board, col):
    """ For a given column, gets the next available row """
    for r in range(ROW_COUNT):
        if board[5 - r][col] == EMPTY:
            break
    return 5 - r


def drop_piece(board, row, col, piece):
    """ Populates the board with the next piece """
    board[row][col] = piece
    return board


def score_position(board, piece):
    """ Calculates board Static Scoring Method """
    score = 0
    # # Score Horizontal
    # for r in range(ROW_COUNT):
    #     row_array = board[(ROW_COUNT-1) - r]
    #     for c in range(COLUMN_COUNT - 3):
    #         window = row_array[c: (c + WINDOW_LENGTH)]
    #         if window.count(piece) == 4:
    #             score += 100
    #         elif window.count(piece) == 3 and window.count(EMPTY) == 1:
    #             score += 10

    # # Score Verticle
    # for c in range(COLUMN_COUNT):
    #     col_array = []
    #     for row in board:
    #         cell = row[c]
    #         col_array.append(cell)
    #     col_array.reverse()
    #     for r in range(ROW_COUNT - 3):
    #         window = col_array[r: (r + WINDOW_LENGTH)]
    #         if window.count(piece) == 4:
    #             score += 100
    #         elif window.count(piece) == 3 and window.count(EMPTY) == 1:
    #             score += 10

    # Score Positive Sloped Diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[((ROW_COUNT-1) - r) - i][c + i]
                      for i in range(WINDOW_LENGTH)]
            if window.count(piece) == 4:
                score += 100
            elif window.count(piece) == 3 and window.count(EMPTY) == 1:
                score += 10

    # # Score Negetively Sloped Diagonals
    # for r in range(ROW_COUNT - 3):
    #     for c in range(COLUMN_COUNT - 3):
    #         window = [board[(r + 3) - i][c + i] for i in range(WINDOW_LENGTH)]
    #         if window.count(piece) == 4:
    #             score += 100
    #         elif window.count(piece) == 3 and window.count(EMPTY) == 1:
    #             score += 10
    return score


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


def pick_best_move(board, piece):
    """ Calculate the best column for next move """
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = [x[:] for x in board]
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col


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
    col = pick_best_move(board, computer_xo)
    columns[col].push(computer_xo)
    board[6 - len(columns[col])][col] = \
        columns[col].peek()
    if len(columns[col]) >= 6:
        column_full.append(True)
    return board, columns, column_full
