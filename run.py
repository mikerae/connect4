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
    dec_row = ("----" * 7) + "-\n"
    col_nums = "  1   2   3   4   5   6   7"
    board_row = ""
    print(dec_row)
    print(col_nums)
    for row in board:
        for cell in row:
            board_row += f'| {cell} '
        board_row += "|\n"
    print(board_row)
    print(dec_row)


def player_move(board, columns, player_XO, name):
    """ Player makes a move"""
    display_board(board)
    print(f'{name} makes a move')
    input("Choose column 1 - 7: ")


def computer_move(board, columns, computer_XO):
    """ Computer makes a move """
    print("Computer makes a move")
    input("Choose column 1 - 7: ")


def check_win():
    """ Check if win conditions are met """
    print("check_win is called")
    return False


def main():
    """ Main Game """
    print("\n********************")
    print(" Welcome to Connect4")
    print("********************\n")

    name = ""
    player_XO = ""
    computer_XO = ""
    board = []
    columns = []
    board = build_empty_board(board)
    columns = build_empty_cols(columns)

    while name.isspace() or name == "":
        name = input("Please tell me your name...\n")

    print(f'\nHello {name}')

    not_valid = True
    while not_valid:
        player_XO = input("Type X to play first, or O to play second: ")
        if (player_XO.isspace() or player_XO == ""):
            continue
        elif player_XO.upper() == "X":
            print(f'\nYou go first {name}, Make your move...\n')
            player_XO = "X"
            computer_XO = "O"
            PLAYER = 0
            COMPUTER = 1
            not_valid = False
        elif player_XO.upper() == "O":
            print(f"\nI'll  go first then, {name}...\n")
            player_XO = "O"
            computer_XO = "X"
            PLAYER = 1
            COMPUTER = 0
            not_valid = False

    win = False
    turn = 0
    # Main game loop
    while not win:
        if turn == PLAYER:
            # Player Move
            player_move(board, columns, player_XO, name)
            win = check_win()
        elif turn == COMPUTER:
            # Computer Move
            computer_move(board, columns, computer_XO)
            win = check_win()
        turn += 1
        turn = turn % 2


main()
