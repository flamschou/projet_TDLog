# create a game

import board
import turtle
import pygame


def basic_display(path):
    """
    Display the board in the terminal.
    """

    Board = board.load(path)

    turtle.setup(800, 800)
    turtle.hideturtle()
    turtle.speed(25)

    for i in range(len(Board)):
        if Board[i].type == "basic":
            turtle.color('black')
        else:
            turtle.color('orange')
        turtle.penup()
        turtle.goto(20*Board[i].x, 20*Board[i].y)
        turtle.fd(20)
        turtle.pendown()
        turtle.left(120)
        for j in range(6):
            turtle.fd(20)
            turtle.left(60)

    print("The board is displayed")


# change the path to the path of the board you want to display
path = "C:\\Data\\2023-24\\TDLOG\\projet_TDLog\\first_board.board"
# cocopath = "C:\\Data\\2023-24\\TDLOG\\projet_TDLog\\first_board.board"
basic_display(path)
