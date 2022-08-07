"""
Connect4 game for player v. computer
Mike Rae
August 2022
"""
import gspread
from google.oauth2.service_account import Credentials
from colorama import init, deinit, Fore
import stacks
from utils import choose_game
from game import Game, build_empty_board, display_board,\
    player_move, computer_move, check_win, check_draw

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("connect4")

init()  # initiates colorama


def start_again(name):
    """ Gives player option to return to the top of the program """
    again_set = ("Y", "N")
    again = input(Fore.WHITE +
                  "Would you like to start again? Type 'y' or 'n': \n")
    try:
        if again == "" or again.isspace():
            raise ValueError(
                'Please type "y" or "n":'
            )
        elif again.upper() not in again_set:
            raise ValueError(
                'Please type "y" or "n": '
            )
    except ValueError as e:
        print(f'{e}')
        start_again(name)
    if again.upper() == "Y":
        main()
    else:
        print(f'Thanks for playing, {name}\nSee you again soon!\n')


def main():
    """ Main Game """
    print(Fore.BLUE + "\n********************")
    print(Fore.YELLOW + " Welcome to Connect4")
    print(Fore.BLUE + "********************\n")

    name = ""
    player_xo = ""
    computer_xo = ""
    board = []
    columns = []
    board = build_empty_board(board)
    columns = stacks.build_empty_cols(columns)
    win = False
    draw = False
    column_full = []
    winner = 0
    turn = 0

    while name == "" or name.isspace():
        name = input(Fore.WHITE + "Please tell me your name: \n")
        if name == "" or name.isspace():
            print("Please try again...")
    print(f'\nHello {name}')

    choose_game(SHEET)

    not_valid = True
    while not_valid:
        player_xo = input("Type X to play first, or O to play second: \n")
        if (player_xo.isspace() or player_xo == ""):
            continue
        elif player_xo.upper() == "X":
            print(f'\nYou go first {name}\n')
            player_xo = Fore.RED + "X" + Fore.WHITE
            computer_xo = Fore.YELLOW + "O" + Fore.WHITE
            PLAYER = 0
            not_valid = False
        elif player_xo.upper() == "O":
            print(f"\nI'll  go first then, {name}...\n")
            player_xo = Fore.YELLOW + "O" + Fore.WHITE
            computer_xo = Fore.RED + "X" + Fore.WHITE
            PLAYER = 1
            not_valid = False

    game = Game(board, name, player_xo)
    game.welcome()

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
    game.process_win(winner, PLAYER, draw)
    game.final_update(board)
    game.display_game_data()
    game.write_game_data(SHEET)
    start_again(name)


main()

deinit()  # Restores terminal text output to system colours
