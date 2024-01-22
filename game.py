# This file defines the class Game
# This class is the most abstract level of architecture of our code
# The launcher uses mostly methods of this class

import random
from os import path
import pygame
from event import Sandstorm, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from players import Attacker, Defender
from bot import DefenderBot, AttackerBot
import scale
import utils

S = scale.scale

WHITE = (200, 215, 200)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 900 * S
SCREEN_HEIGHT = 600 * S


class Game:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = Board()
        self.attacker = Attacker()
        self.defender = Defender()
        self.current_player = self.defender
        self.deck = []
        self.time = 15
        self.defended_hex = None
        self.adrenalin = 1
        self.event_counter = 0
        self.attack = None
        self.heal = None
        self.winner = None
        self.config = None
        # Flake8 noqa
        self.attack_image = pygame.image.load(path.join("Images", "explosion.png"))
        self.attack_image = pygame.transform.scale(self.attack_image, (60 * S, 60 * S))
        self.healing_image = pygame.image.load(path.join("Images", "healing.png"))
        self.healing_image = pygame.transform.scale(
            self.healing_image, (60 * S, 60 * S)
        )

    # this method generates the board and the deck
    def generate(self):
        self.board.generate_board(self.num_rows, self.num_cols)
        self.create_deck()

    # this method is used to display the board, the troops and every animation of the game
    def draw(self, screen):
        for hexagon in self.board.list:
            hexagon.draw(screen)
        for troop in self.attacker.troops:
            troop.draw(screen)
        for troop in self.defender.troops:
            troop.draw(screen)
        if self.attack is not None:
            hex = self.attack
            image = self.attack_image
            image_rect = image.get_rect(center=(hex.x, hex.y))
            print("drawing attack")
            screen.blit(image, image_rect)
            pygame.display.flip()
            pygame.time.delay(1000)
            print("end attack")
            self.attack = None
        if self.heal is not None:
            hex = self.heal
            image = self.healing_image
            image_rect = image.get_rect(center=(hex.x, hex.y))
            print("drawing heal")
            screen.blit(image, image_rect)
            pygame.display.flip()
            pygame.time.delay(1000)
            print("end heal")
            self.heal = None

    # this method applies the effect of the new event
    def apply_events(self):
        self.deck[self.event_counter % 54].apply_effect(self)
        self.event_counter += 1
        print(self.deck[self.event_counter % 54].event_type)

    # this method is used to get the hexagon at the position (x,y)
    def get_hexagon_at(self, x, y):
        for hexagon in self.board.list:
            if hexagon.contains(x, y):
                return hexagon
        return None

    # this method creates the deck of events
    def create_deck(self):
        for i in range(54):
            choice = random.choice(
                ["sandstorm", "fire", "rescue", "betrayal", "adrenalin", "expansion"]
            )
            if choice == "sandstorm":
                self.deck.append(Sandstorm())
            if choice == "fire":
                self.deck.append(Fire())
            if choice == "rescue":
                self.deck.append(Rescue())
            if choice == "betrayal":
                self.deck.append(Betrayal())
            if choice == "adrenalin":
                self.deck.append(Adrenalin())
            if choice == "expansion":
                self.deck.append(Expansion())

    # this method changes the active player
    def change_player(self):
        if self.current_player == self.defender:
            self.current_player = self.attacker
        else:
            self.current_player = self.defender
            self.apply_events()
            self.time -= 1

    # this method displays the time that is left and the current player
    def display_info(self, screen):
        font = utils.font(20)
        text = "Time left: " + str(self.time)
        text += ", Current player: " + str(self.current_player.name)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(400 * S, 550 * S))
        screen.blit(info_text, text_rect)

    # this method displays the winner of the game
    def display_winner(self, screen):
        font = utils.font(60)
        text = "Winner is " + str(self.winner.name)
        print(text)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(450 * S, 300 * S))
        screen.blit(info_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(5000)
        print("end game")

    # this method is used to display the event that is currently active
    def display_Event(self, screen):
        font = utils.font(20)
        text = "Event is " + str(self.deck[(self.event_counter - 1) % 54].event_type)
        print(text)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(800 * S, 150 * S))
        screen.blit(info_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1500)

    # this method eliminates the troops that are dead
    def eliminations(self):
        self.attacker.troops = [
            troop for troop in self.attacker.troops if troop.status != "dead"
        ]
        self.defender.troops = [
            troop for troop in self.defender.troops if troop.status != "dead"
        ]

    # this method ends the game :
    # if a player has no troops left, the other player wins
    # if the defended hexagon is taken by the attacker, the attacker wins
    def end_game(self):
        if len(self.attacker.troops) == 0:
            self.winner = self.defender
        if len(self.defender.troops) == 0:
            self.winner = self.attacker

        for troop in self.attacker.troops:
            if troop.hex.hex_type == "Defended":
                self.winner = self.attacker

    # this method end the turn of the current player if he clicks on the button
    def end_turn(self, clicked_pos, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        clicked = clicked_pos

        if pygame.Rect(
            (SCREEN_WIDTH - 190 * S, SCREEN_HEIGHT - 60 * S), (180 * S, 40 * S)
        ).collidepoint(clicked):
            for troop in self.current_player.troops:
                troop.selected = False
            self.change_player()
            self.current_player.regenerate_speed()
            if self.current_player.name == "Defender":
                self.display_Event(screen)

    def screen_update_bot(self, screen):
        screen.fill(WHITE)
        self.draw(screen)
        self.display_info(screen)
        self.current_player.draw_button(screen, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK)
        pygame.display.flip()
        pygame.time.delay(50)

    def switch_to_defenderbot(self):
        self.defender = DefenderBot()
        self.current_player = self.defender

    def switch_to_attackerbot(self):
        self.attacker = AttackerBot()


class HumanVSBotGame(Game):
    def __init__(self, num_rows, num_cols):
        super().__init__(num_rows, num_cols)
        self.attacker = Attacker()
        self.defender = DefenderBot()
        self.current_player = self.attacker
        self.deck = []
        self.time = 15
        self.adrenalin = 1
        self.event_counter = 0
        self.attack = None
        self.heal = None
        self.winner = None
        # Flake8 noqa
        self.attack_image = pygame.image.load(path.join("Images", "explosion.png"))
        self.attack_image = pygame.transform.scale(self.attack_image, (60 * S, 60 * S))
        self.healing_image = pygame.image.load(path.join("Images", "healing.png"))
        self.healing_image = pygame.transform.scale(
            self.healing_image, (60 * S, 60 * S)
        )
