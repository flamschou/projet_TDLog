# create a game

import board


def basic_display(path):
    """
    Display the board in the terminal.
    """

    Board = board.load(path)

    for i in range(len(Board)):
        print(Board[i].index, " ", Board[i].type)

    print("The board is displayed")


# change the path to the path of the board you want to display
path = "C:\\ENPC\\Projects\\TDLOG\\projet_TDLog\\first_board.board"

basic_display(path)
