import random
from os import path
import pygame
from event import Sandstorm, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from players import Attacker, Defender
from bot import DefenderBot
import scale
import utils

S = scale.scale


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

    def generate(self):
        self.board.generate_board(self.num_rows, self.num_cols)
        self.create_deck()

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

    def apply_events(self):
        self.deck[self.event_counter % 54].apply_effect(self)
        self.event_counter += 1
        print(self.deck[self.event_counter % 54].event_type)

    def get_hexagon_at(self, x, y):
        for hexagon in self.board.list:
            if hexagon.contains(x, y):
                return hexagon
        return None

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

    def change_player(self):
        if self.current_player == self.attacker:
            self.current_player = self.defender
        else:
            self.current_player = self.attacker
            self.apply_events()
            self.time -= 1

    def display_info(self, screen):
        font = utils.font(20)
        text = "Time left: " + str(self.time)
        text += ", Current player: " + str(self.current_player.name)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(400 * S, 550 * S))
        screen.blit(info_text, text_rect)

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

    def display_Event(self, screen):
        font = utils.font(20)
        text = "Event is " + str(self.deck[(self.event_counter - 1) % 54].event_type)
        print(text)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(800 * S, 150 * S))
        screen.blit(info_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1500)

    def eliminations(self):
        self.attacker.troops = [
            troop for troop in self.attacker.troops if troop.status != "dead"
        ]
        self.defender.troops = [
            troop for troop in self.defender.troops if troop.status != "dead"
        ]
        if len(self.attacker.troops) == 0:
            self.winner = self.defender
        if len(self.defender.troops) == 0:
            self.winner = self.attacker

        for troop in self.attacker.troops:
            if troop.hex.hex_type == "Defended":
                self.winner = self.attacker

    def end_tour(self, clicked_pos, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        clicked = clicked_pos

        if pygame.Rect(
            (SCREEN_WIDTH - 190 * S, SCREEN_HEIGHT - 60 * S), (180 * S, 40 * S)
        ).collidepoint(clicked):
            self.change_player()
            self.current_player.regenerate_speed()
            if self.current_player.name == "Attacker":
                self.display_Event(screen)


class HumanVSBotGame(Game):
    def __init__(self, num_rows, num_cols):
        super().__init__(num_rows, num_cols)
        self.attacker = Attacker()
        self.defender = DefenderBot()
        self.current_player = self.defender
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
