import pygame
from os import path
import scale

S = scale.scale


def font(size):
    return pygame.font.Font(path.join("Fonts", "NovaSquare-Regular.ttf"), int(size*S))


def drawButton(texte, place, button_pos, button_size, text_center, font, col):
    pygame.draw.rect(place, col, (button_pos, button_size), 2)
    text = font.render(texte, True, (0, 0, 0))
    text_rect = text.get_rect(center=text_center)
    place.blit(text, text_rect)


def drawButton_end_tour(place, SCREEN_WIDTH, SCREEN_HEIGHT, col):
    button_pos = (SCREEN_WIDTH - 190*S, SCREEN_HEIGHT - 60*S)
    button_size = (180*S, 40*S)
    text_center = (SCREEN_WIDTH - 100*S, SCREEN_HEIGHT - 40*S)
    fontObj = font(30)
    drawButton("fin du tour", place, button_pos, button_size, text_center, fontObj, col)


def drawButton_troop(texte, place, nbre, SCREEN_WIDTH, pos_y, col, troops_available):
    button_pos = (SCREEN_WIDTH - 150*S, pos_y)
    button_size = (100*S, 20*S)
    troops_available[2] = pygame.Rect(button_pos, button_size)
    text_center = (SCREEN_WIDTH - 100*S, pos_y + 10*S)
    fontObj = font(13)
    drawButton(
        texte + " x" + str(nbre), place, button_pos, button_size, text_center, fontObj, col
    )


def end_tour(clicked_pos, SCREEN_WIDTH, SCREEN_HEIGHT):
    clicked = clicked_pos

    if pygame.Rect((SCREEN_WIDTH - 190*S, SCREEN_HEIGHT - 60*S), (180*S, 40*S)).collidepoint(
        clicked
    ):
        return True

    return False
