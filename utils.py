import pygame


def drawButton(texte, place, button_pos, button_size, text_center, font, col):
    pygame.draw.rect(place, col, (button_pos, button_size), 2)
    text = font.render(texte, True, (0, 0, 0))
    text_rect = text.get_rect(center=text_center)
    place.blit(text, text_rect)


def drawButton_troop(texte, place, nbre, SCREEN_WIDTH, pos_y, col, troops_available):

    button_pos = (SCREEN_WIDTH - 150, pos_y)
    button_size = (100, 20)
    troops_available.append(pygame.Rect(button_pos, button_size))
    text_center = (SCREEN_WIDTH - 100, pos_y + 10)
    font = pygame.font.Font(None, 20)
    drawButton(texte + " x" + str(nbre), place, button_pos, button_size, text_center, font, col)
