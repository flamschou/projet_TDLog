import pygame
import sys
from plateau import Plateau
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

test = Plateau(num_rows, num_cols)
test.generate_board()

# Boucle principale
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    test.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.quit()
