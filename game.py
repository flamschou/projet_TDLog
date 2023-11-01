# create a game

import board
import turtle


def basic_display(path):
    """
    Display the board in the terminal.
    """

    Board = board.load(path)

    turtle.setup(800, 800)
    turtle.hideturtle()

    for i in range(len(Board)):
        turtle.penup()
        turtle.goto(10*Board[i].x, 10*Board[i].y)
        turtle.fd(10)
        turtle.pendown()
        turtle.left(120)
        for j in range(6):
            turtle.fd(10)
            turtle.left(60)

    print("The board is displayed")


# change the path to the path of the board you want to display
path = "C:\\Data\\2023-24\\TDLOG\\projet_TDLog\\first_board.board"
# cocopath = "C:\\Data\\2023-24\\TDLOG\\projet_TDLog\\first_board.board"
basic_display(path)
