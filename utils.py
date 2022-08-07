"""
Utilitie functions and program navigation functions
"""


def get_played_games_list(games_ss):
    """ gets list of worksheet objects """
    wks = games_ss.worksheets()
    wks_titles = []
    for w in wks:
        wks_titles.append(w.title)
    return wks_titles


def display_games_list(list):
    """ Displays a list of played games
    with index """
    for idl, l in enumerate(list):
        print(f'type {idl} to select {l}')