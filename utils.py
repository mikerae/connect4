"""
Utilitie functions and program navigation functions
"""
import gspread


def get_played_games_list(games_ss):
    """ gets list of worksheet objects """
    wks = games_ss.worksheets()
    wks_titles = []
    for w in wks:
        wks_titles.append(w.title)
    return wks_titles
