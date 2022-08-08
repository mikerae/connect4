"""
Programing AI is well beyond the scope of this project.
Hoever in the interests of fun and challenge, I have followed
Keith Galli: How to Program a Connect 4 AI
(https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6)
All code is copied from his walkthrough, exept where modifications
were needed to run with my other code.
Mike Rae 8/8/2022
"""
from random import randint


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
