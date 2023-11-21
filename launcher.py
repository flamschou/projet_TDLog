import pygame
import sys
import utils
from game import Game

# Initialisation de Pygame
pygame.init()

# Couleurs

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexagonal Board Game")


# Générer un plateau aléatoire
num_rows = 8  # Nombre de lignes
num_cols = 10  # Nombre de colonnes

test = Game(num_rows, num_cols)
test.generate()
print(test.deck[0].event_type)

# Boucle principale


screen.fill(WHITE)
test.draw(screen)

# Dessiner les boutons
def drawButtons():
    pos_y = SCREEN_HEIGHT - 150  # Position verticale initiale des boutons
    i = 0
    for troop in test.troops_available:
        utils.drawButton_troop(troop[0], screen, troop[1], SCREEN_WIDTH, pos_y, BLACK, test.troops_available[i])
        i += 1

        pos_y -= 30  # Ajustement vertical pour chaque bouton


drawButtons()

i = 0
running = True

while test.end_ini() and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            i = test.selected_button(pygame.mouse.get_pos(), i)
            test.initialize_troops(pygame.mouse.get_pos(), i)

    screen.fill(WHITE)

    #  test.apply_events()
    test.draw(screen)
    drawButtons()

    pygame.display.flip()

# Boucle principale

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            test.attacker.make_move(pygame.mouse.get_pos(), test)

    screen.fill(WHITE)

    #  test.apply_events()
    test.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
