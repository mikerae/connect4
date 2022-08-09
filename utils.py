"""
Utilitie functions and program navigation functions
"""
from colorama import Fore
from game import Game


def get_played_games_list(sheet):
    """ gets list of worksheet objects """
    wks = sheet.worksheets()
    wks_titles = []
    for w in wks:
        wks_titles.append(w.title)
    return wks_titles


def display_games_list(g_list):
    """ Displays a list of played games
    with index """
    for idl, l in enumerate(g_list):
        print(f'type {idl} to select {l}')


def choose_game(sheet):
    """ Player selcts game to view """
    print("If you would like to see the results of past games\n\
Here is a list of games you can review...\n")
    played_games = get_played_games_list(sheet)
    display_games_list(played_games)
    played_game = Game([], "", "")
    while True:
        print(Fore.WHITE + f'Choose 0 - {len(played_games) - 1} to select a game,\n\n\
    Or choose "N" to play a new game.')
        try:
            choice = input('Please make your choice :\n')
            if (choice.isspace() or choice == ""):
                raise ValueError
            elif choice.upper() == "N":
                break
            elif 0 <= int(choice) <= len(played_games):
                wks = sheet.get_worksheet(int(choice))
                played_game.read_game_data(wks)
                played_game.display_game_data()
                continue
        except ValueError:
            continue
