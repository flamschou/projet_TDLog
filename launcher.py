import pygame
import sys
from game import Game
# from evenement import Evenement
# from hexagone import Hexagone
# import hexagone
# from troupe import Troupe

# Initialisation de Pygame
pygame.init()

# Couleurs

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
SCREEN_WIDTH = 800
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
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_pos = pygame.mouse.get_pos()
            print("clicked at", clicked_pos)
            for hexagon in test.board.list:
                if hexagon.rect.collidepoint(clicked_pos):
                    print("hexagon", hexagon.index, "clicked")
            for troop in test.troops:
                if troop.rect.collidepoint(clicked_pos):
                    print("troop", troop.index, "clicked")

    screen.fill(WHITE)

    test.handle_event()
    test.draw(screen)
    test.attacker.make_move()

    pygame.display.flip()

pygame.quit()
sys.exit()
