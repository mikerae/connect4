"""
Connect4 game for player v. computer
Mike Rae
August 2022
"""
from stacks import Stack


def build_empty_board(board):
    for row in range(6):
        row = ["-"] * 7
        board.append(row)
    return board


def display_board(board):
    pass


def main():
    """ Main Game """
    print("\n********************")
    print(" Welcome to Connect4")
    print("********************\n")

    player = ""
    player_position = ""
    board = []
    board = build_empty_board(board)

    while player.isspace() or player == "":
        player = input("Please tell me your name...\n")

    print(f'\nHello {player}')

    not_valid = True
    while not_valid:
        player_position = input("Type X to play first, or O to play second: ")
        if (player_position.isspace() or player_position == ""):
            continue
        elif player_position.upper() == "X":
            print(f'\nYou go first {player}, Make your first move...\n')
            not_valid = False
        elif player_position.upper() == "O":
            print(f"\nI'll  go first then, {player}...\n")
            not_valid = False


main()