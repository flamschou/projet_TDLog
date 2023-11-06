import pygame
import sys
import player as p
import board as b
import random
import troops as t
import card as c
import hexagone as h


pygame.init()
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexagonal Board Game")
board = []
num_rows = 8
num_cols = 10

for row in range(num_rows):
    for col in range(num_cols):
        hex_type = random.choice(["basic", "swamp", "forest"])
        x = col * 60 + (30 if row % 2 == 0 else 60) + 60
        y = row * 52 + 60
        hexagon = h.hexagone(hex_type, x, y)
        board.append(hexagon)

assassin = t.troops("assassin", board[0].x, board[0].y)

# Boucle principale
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Dessiner l'hexagone
    for hexagon in board:
        hexagon.draw(screen)
    assassin.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
