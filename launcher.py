# Imports
import pygame
import sys
from game import Game
import utils
import scale

# Pygame initialization
pygame.init()

# Colors
WHITE = (200, 215, 200)
BLACK = (0, 0, 0)

# Scale Parameter
S = scale.scale

# Window Parameters
SCREEN_WIDTH = 900 * S
SCREEN_HEIGHT = 600 * S
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexagonal Board Game")
frame_rate = 15
clock = pygame.time.Clock()

# Board Parameters
num_rows = 8
num_cols = 10

# Game initialization and genration
test = Game(num_rows, num_cols)
test.generate()

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
        if (
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        ):  # Left click on one of the
            clicked = pygame.mouse.get_pos()
            if pygame.Rect(
                (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3), (180 * S, 40 * S)
            ).collidepoint(clicked):
                test.config = "no bot"
                print("no bot")
            if pygame.Rect(
                (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 + 60 * S),
                (180 * S, 40 * S),
            ).collidepoint(clicked):
                test.config = "defender bot"
                print("defender bot")
            if pygame.Rect(
                (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 + 120 * S),
                (180 * S, 40 * S),
            ).collidepoint(clicked):
                test.config = "attacker bot"
                print("attacker bot")
            if pygame.Rect(
                (SCREEN_WIDTH / 2 - 90 * S, SCREEN_HEIGHT / 3 + 120 * S),
                (180 * S, 40 * S),
            ).collidepoint(clicked):
                test.config = "attacker bot"
                print("attacker bot")

    utils.drawButton_config(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)
    pygame.display.flip()
    clock.tick(frame_rate)

# Create players in function of the configuration
if test.config == "defender bot":
    test.switch_to_defenderbot()
if test.config == "attacker bot":
    test.switch_to_attackerbot()
players = [test.defender, test.attacker]


# Display board and initialize troops
screen.fill(WHITE)
test.draw(screen)
test.attacker.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)
test.defender.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)


# Initialisation phase
for i in range(2):
    running = True
    print(test.current_player.name)
    while test.current_player.end_ini() and running:
        test.draw(screen)
        if (
            test.current_player.name == "AttackerBot"
            or test.current_player.name == "DefenderBot"
        ):
            test.current_player.initialize_bot(test, screen)
            print("ini essayée bot")

        else:
            for event in pygame.event.get():
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

# Game phase
while running and test.time > 0 and test.winner is None:
    if (
        test.current_player.name == "AttackerBot"
        or test.current_player.name == "DefenderBot"
    ):
        screen.fill(WHITE)
        test.draw(screen)
        test.display_info(screen)
        pygame.display.flip()
        pygame.time.delay(500)
        test.current_player.make_move_bot(test, screen)
        print("bot essayé")

    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            test.end_turn(pygame.mouse.get_pos(), SCREEN_WIDTH, SCREEN_HEIGHT, screen)
            test.current_player.make_move(pygame.mouse.get_pos(), test)
            test.eliminations()
            test.end_game()

    # Clear the display to avoid remanent images
    screen.fill(WHITE)

    # Hovered troop info
    mousePos = pygame.mouse.get_pos()
    for troop in test.attacker.troops:
        if troop.isHovered(mousePos):
            troop.info(screen)
    for troop in test.defender.troops:
        if troop.isHovered(mousePos):
            troop.info(screen)

    # Display the board and buttons
    test.draw(screen)
    test.display_info(screen)
    utils.drawButton_end_turn(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)
    pygame.display.flip()
    clock.tick(frame_rate)

# End of the game
pygame.time.delay(2000)
screen.fill(WHITE)
if test.winner is None:
    test.winner = test.defender
test.display_winner(screen)

# Close the window
pygame.quit()
sys.exit()
