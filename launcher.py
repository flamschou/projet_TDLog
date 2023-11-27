import pygame
import sys
from game import Game
import utils

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

for current_player in [test.attacker, test.defender]:
    i = 0
    running = True

    while current_player.end_ini() and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                i = current_player.selected_button(pygame.mouse.get_pos(), i)
                current_player.initialize_troops(pygame.mouse.get_pos(), i, test)

        screen.fill(WHITE)

        #  test.apply_events()
        test.draw(screen)
        current_player.draw_button(screen, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK)

        pygame.display.flip()

running = True
players = [test.attacker, test.defender]
i = 0
test.apply_events
current_player = players[i]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if utils.end_tour(pygame.mouse.get_pos(), SCREEN_WIDTH, SCREEN_HEIGHT):
                i += 1
                if i % 2 == 0:
                    test.apply_events
                current_player.regenerate_speed()
                current_player = players[i % 2]
            current_player.make_move(pygame.mouse.get_pos(), test)

    screen.fill(WHITE)

    #  test.apply_events()
    test.draw(screen)
    utils.drawButton_end_tour(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()
