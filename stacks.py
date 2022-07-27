"""
Oscar Nieves, in his article 'Programming a Connect-4 game on Python'
suggests using Stacks as a data structure for the 7 columns in
Connect4. His code for defining a Stack class is copied here.
https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
A game of connect-4 Versus the computer
Author: Oscar A. Nieves
Updated: August 9, 2021
"""


class Stack:
    """ Class stack for each column """
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push(self, element):
        """ Add element to top of stack if there is room """
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return

    def peek(self):
        """ Get last element of stack """
        return self._list[-1]
