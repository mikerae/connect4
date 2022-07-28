"""
Connect4 game for player v. computer
Mike Rae
August 2022
"""
from stacks import Stack


def build_empty_board(board):
    """ Initialises empty board"""
    for row in range(6):
        row = ["-"] * 7
        board.append(row)
    return board


def build_empty_cols(columns):
    """ Initialises empty column Stacks """
    for col in range(7):
        col = Stack()
        columns.append(col)
    return columns


def display_board(board):
    """ Displays the current state of the board """
    dec_row = ("-*" * 7) + "-"
    col_nums = " 1 2 3 4 5 6 7 "
    board_row = ""
    print(dec_row)
    print(col_nums)
    for row in board:
        for cell in row:
            board_row += f'|{cell}'
        board_row += "|\n"
    print(board_row)
    print(dec_row)


def make_move(board, columns):
    """ Players take turns to make thier move"""
    display_board(board)


def main():
    """ Main Game """
    print("\n********************")
    print(" Welcome to Connect4")
    print("********************\n")

    player = ""
    player_position = ""
    board = []
    columns = []
    board = build_empty_board(board)
    columns = build_empty_cols(columns)

    while player.isspace() or player == "":
        player = input("Please tell me your name...\n")

    print(f'\nHello {player}')

    not_valid = True
    while not_valid:
        player_position = input("Type X to play first, or O to play second: ")
        if (player_position.isspace() or player_position == ""):
            continue
        elif player_position.upper() == "X":
            print(f'\nYou go first {player}, Make your move...\n')
            not_valid = False
        elif player_position.upper() == "O":
            print(f"\nI'll  go first then, {player}...\n")
            not_valid = False
    make_move(board, columns)


main()
