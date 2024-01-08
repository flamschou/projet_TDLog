import pygame
from os import path
import scale

S = scale.scale


def font(size):
    return pygame.font.Font(path.join("Fonts", "NovaSquare-Regular.ttf"), int(size * S))


def drawButton(texte, place, button_pos, button_size, text_center, font, col):
    pygame.draw.rect(place, col, (button_pos, button_size), 2)
    text = font.render(texte, True, (0, 0, 0))
    text_rect = text.get_rect(center=text_center)
    place.blit(text, text_rect)


def drawButton_config(place, SCREEN_WIDTH, SCREEN_HEIGHT, col):
    button_pos = (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 - 20 * S)
    button_size = (180 * S, 40 * S)
    text_center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    fontObj = font(30)
    drawButton("no bot", place, button_pos, button_size, text_center, fontObj, col)

    button_pos = (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 - 20 * S + 60 * S)
    text_center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 60 * S)
    drawButton(
        "defender bot", place, button_pos, button_size, text_center, fontObj, col
    )

    button_pos = (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 - 20 * S + 120 * S)
    text_center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 120 * S)
    drawButton(
        "attacker bot", place, button_pos, button_size, text_center, fontObj, col
    )


def drawButton_end_tour(place, SCREEN_WIDTH, SCREEN_HEIGHT, col):
    button_pos = (SCREEN_WIDTH - 190 * S, SCREEN_HEIGHT - 60 * S)
    button_size = (180 * S, 40 * S)
    text_center = (SCREEN_WIDTH - 100 * S, SCREEN_HEIGHT - 40 * S)
    fontObj = font(30)
    drawButton("fin du tour", place, button_pos, button_size, text_center, fontObj, col)


def drawButton_troop(texte, place, nbre, SCREEN_WIDTH, pos_y, col, troops_available):
    button_pos = (SCREEN_WIDTH - 150 * S, pos_y)
    button_size = (100 * S, 20 * S)

    # Assurez-vous que troops_available a assez d'éléments
    if len(troops_available) < 3:
        troops_available.extend([None] * (3 - len(troops_available)))

    text_center = (SCREEN_WIDTH - 100 * S, pos_y + 10 * S)
    fontObj = font(13)
    drawButton(
        texte + " x" + str(nbre),
        place,
        button_pos,
        button_size,
        text_center,
        fontObj,
        col,
    )
