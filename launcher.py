import pygame
import sys
from game import Game

# from game import HumanVSBotGame
import utils
import scale

# import time

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (200, 215, 200)
BLACK = (0, 0, 0)

# Get the dimensions of the screen
S = scale.scale

# Paramètres de la fenêtre
SCREEN_WIDTH = 900 * S
SCREEN_HEIGHT = 600 * S
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexagonal Board Game")


# Générer un plateau aléatoire
num_rows = 8  # Nombre de lignes
num_cols = 10  # Nombre de colonnes

# partie humain vs humain
test = Game(num_rows, num_cols)

# ou partie humain vs bot
# test = HumanVSBotGame(num_rows, num_cols)

test.generate()
print(test.deck[0].event_type)
frame_rate = 15
clock = pygame.time.Clock()

# Initial Menu to choose bot configuration
font = utils.font(40)
screen.fill(WHITE)
text = "Choose bot configuration"
info_text = font.render(text, True, (255, 0, 0))
text_rect = info_text.get_rect(center=(SCREEN_WIDTH / 2, 130 * S))
screen.blit(info_text, text_rect)
while test.config is None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = pygame.mouse.get_pos()
            if pygame.Rect(
                (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3), (180 * S, 40 * S)
            ).collidepoint(clicked):
                test.config = "no bot"

    utils.drawButton_config(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)
    pygame.display.flip()
    clock.tick(frame_rate)

# Boucle principale
screen.fill(WHITE)
test.draw(screen)
test.defender.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)
test.attacker.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

# time.sleep(5)

# version initiale humain contre humain
players = [test.defender, test.attacker]
for i in range(2):
    running = True

    # time.sleep(5)
    if (
        test.current_player.name == "AttackerBot"
        or test.current_player.name == "DefenderBot"
    ):
        test.current_player.clicks_for_ini(test)

    while test.current_player.end_ini() and running:
        for event in pygame.event.get():
            if (
                test.current_player.name == "AttackerBot"
                or test.current_player.name == "DefenderBot"
            ):
                test.current_player.clicks_for_ini(test)
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                test.current_player.initialize_troops(pygame.mouse.get_pos(), test)

        screen.fill(WHITE)
        test.draw(screen)
        test.display_info(screen)
        test.current_player.draw_button(screen, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK)

        pygame.display.flip()
        clock.tick(frame_rate)

    test.current_player = players[(i + 1) % 2]


while running and test.time > 0 and test.winner is None:
    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            test.end_tour(pygame.mouse.get_pos(), SCREEN_WIDTH, SCREEN_HEIGHT, screen)
            test.current_player.make_move(pygame.mouse.get_pos(), test)
            test.eliminations()

    screen.fill(WHITE)  # Display handling
    mousePos = pygame.mouse.get_pos()
    for troop in test.attacker.troops:
        if troop.isHovered(mousePos):
            troop.info(screen)
    for troop in test.defender.troops:
        if troop.isHovered(mousePos):
            troop.info(screen)
    test.draw(screen)
    test.display_info(screen)
    utils.drawButton_end_tour(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.time.delay(1500)
screen.fill(WHITE)
if test.winner is None:
    test.winner = test.defender
test.display_winner(screen)

pygame.quit()
sys.exit()

# version alternative pour tester les bots

"""
# partie humain vs bot
human_vs_bot_game = HumanVSBotGame(num_rows, num_cols)
human_vs_bot_game.generate()

# initialisation du bot défenseur
bot_defender = DefenderBot()
bot_defender.initialize_troops(human_vs_bot_game)

# initialisation des joueurs
human_attacker = human_vs_bot_game.attacker
human_defender = human_vs_bot_game.defender

# initialisation des joueurs
for current_player in [bot_defender, human_attacker]:
    i = 0
    running = True

    while current_player.end_ini() and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if isinstance(current_player, DefenderBot):
                    i = current_player.selected_button(pygame.mouse.get_pos())
                else:
                    i = current_player.selected_button(pygame.mouse.get_pos(), i)
                current_player.initialize_troops(pygame.mouse.get_pos(), i, human_vs_bot_game)
"""

"""
running = True
test.apply_events()
i = 0
current_player = players[i]"""
