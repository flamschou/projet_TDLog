import pygame


def drawButton(texte, place, button_pos, button_size, text_center, font, col):
    pygame.draw.rect(place, col, (button_pos, button_size), 2)
    text = font.render(texte, True, (0, 0, 0))
    text_rect = text.get_rect(center=text_center)
    place.blit(text, text_rect)


def drawButton_end_tour(place, SCREEN_WIDTH, SCREEN_HEIGHT, col):
    button_pos = (SCREEN_WIDTH - 190, SCREEN_HEIGHT-60)
    button_size = (180, 40)
    text_center = (SCREEN_WIDTH - 100, SCREEN_HEIGHT-40)
    font = pygame.font.Font(None, 40)
    drawButton("fin du tour", place, button_pos, button_size, text_center, font, col)


def drawButton_troop(texte, place, nbre, SCREEN_WIDTH, pos_y, col, troops_available):
    button_pos = (SCREEN_WIDTH - 150, pos_y)
    button_size = (100, 20)
    troops_available.append(pygame.Rect(button_pos, button_size))
    text_center = (SCREEN_WIDTH - 100, pos_y + 10)
    font = pygame.font.Font(None, 20)
    drawButton(texte + " x" + str(nbre), place, button_pos, button_size, text_center, font, col)


def end_tour(clicked_pos, SCREEN_WIDTH, SCREEN_HEIGHT):
    clicked = clicked_pos

    if pygame.Rect((SCREEN_WIDTH - 190, SCREEN_HEIGHT-60), (180, 40)).collidepoint(clicked):
        return True

    return False