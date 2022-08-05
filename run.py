"""
Connect4 game for player v. computer
Mike Rae
August 2022
"""
from random import randint
from datetime import datetime, timedelta
from stacks import Stack
from game import Game


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
            print(f'You chose column {column}...')
            return True
    except ValueError as e:
        print(f'{e}')
        return False


def player_move(board, columns, player_xo, column_full):
    """ Player makes a move"""
    display_board(board)
    column = (input("Choose column 1 - 7: "))
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


def start_again(name):
    """ Gives player option to return to the top of the program """
    again_set = ("Y", "N")
    again = input("Would you like to start again? Type 'y' or 'n'")
    try:
        if again == "" or again.isspace():
            raise ValueError(
                'Please type "y" or "n":'
            )
        elif again.upper() not in again_set:
            raise ValueError(
                'Please type "y" or "n":'
            )
    except ValueError as e:
        print(f'{e}')
        start_again(name)
    if again.upper() == "Y":
        main()
    else:
        print(f'Thanks for playing, {name},\n See you again soon!')


def process_win(winner, PLAYER, player_xo, name, draw, game):
    """ Displays winner message """
    if draw:
        print(f'Its a draw! Nice game {name}.')
        game.winner = "draw"
    elif PLAYER == winner:
        print(f' {name}, you have won!\n\
            You played {player_xo}')
        game.winner = name
    else:
        print(f'I won this time!\n\
            Better luch next time {name}!')
        game.winner = "Computer"


def main():
    """ Main Game """
    print("\n********************")
    print(" Welcome to Connect4")
    print("********************\n")

    name = ""
    player_xo = ""
    computer_xo = ""
    board = []
    columns = []
    board = build_empty_board(board)
    columns = build_empty_cols(columns)
    win = False
    draw = False
    column_full = []
    winner = 0
    turn = 0

    while name == "" or name.isspace():
        name = input("Please tell me your name...\n")
        if name == "" or name.isspace():
            print("Please try again...")
    print(f'\nHello {name}')

    not_valid = True
    while not_valid:
        player_xo = input("Type X to play first, or O to play second: ")
        if (player_xo.isspace() or player_xo == ""):
            continue
        elif player_xo.upper() == "X":
            print(f'\nYou go first {name}, Make your move...\n')
            player_xo = "X"
            computer_xo = "O"
            PLAYER = 0
            not_valid = False
        elif player_xo.upper() == "O":
            print(f"\nI'll  go first then, {name}...\n")
            player_xo = "O"
            computer_xo = "X"
            PLAYER = 1
            not_valid = False

    game = Game(board, name, player_xo)
    print(f' Hi {game.player}, your game started at {game.start}')

    # Main game loop
    while not win:
        if turn == PLAYER:
            # Player Move
            board, columns, column_full =\
                player_move(board, columns, player_xo, column_full)
            win, winner = check_win(board, player_xo, turn)
            draw = check_draw(column_full)
            game.moves += 1
        else:
            # Computer Move
            board, columns, column_full =\
                computer_move(board, columns, computer_xo, column_full)
            win, winner = check_win(board, computer_xo, turn)
            draw = check_draw(column_full)
        turn += 1
        turn = turn % 2
        if draw:
            break
    display_board(board)
    process_win(winner, PLAYER, player_xo, name, draw, game)
    game.final_update(board)
    game.display_game_data()
    start_again(name)


main()
