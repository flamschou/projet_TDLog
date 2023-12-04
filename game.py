import random
import pygame
from event import Rain, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from players import Attacker, Defender
from bot import DefenderBot
import scale

S = scale.scale


class Game:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = Board()
        self.attacker = Attacker()
        self.defender = Defender()
        self.current_player = self.attacker
        self.deck = []
        self.time = 35
        self.adrenalin = 1
        self.event_counter = 0
        self.attack = None

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
            hex = self.attack.hex
            image = self.attack.attack_image
            image_rect = image.get_rect(center=(hex.x, hex.y))
            print("drawing attack")
            screen.blit(image, image_rect)
            pygame.display.flip()
            pygame.time.delay(1000)
            print("end attack")
            self.attack = None

    def apply_events(self):
        self.deck[self.event_counter % 54].apply_effect(self)
        self.event_counter += 1
        print(self.deck[self.event_counter % 54].event_type)

    def get_hexagon_at(self, x, y):
        for hexagon in self.board.list:
            if hexagon.contains(x, y):
                return hexagon
        return None

    def list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.board:
            if (
                abs(hexagon.x - hexagon1.x) < 80*S
                and abs(hexagon.y - hexagon1.y) < 80*S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)

        return neighbors

    def neighbors(self, hexagon, hexagon1):
        if hexagon in self.list_neighbors(hexagon1):
            return True
        else:
            return False

    def create_deck(self):
        for i in range(54):
            choice = random.choice(
                ["rain", "fire", "rescue", "betrayal", "adrenalin", "expansion"]
            )
            if choice == "rain":
                self.deck.append(Rain())
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

    def display_info(self, screen):
        font = pygame.font.Font(None, 25)
        text = "Time left: " + str(self.time) + ", Adrenalin : " + str(self.adrenalin)
        info_text = font.render(text, True, (255, 0, 0))
        text_rect = info_text.get_rect(center=(120*S, 550*S))
        screen.blit(info_text, text_rect)


class HumanVSBotGame(Game):
    def __init__(self, num_rows, num_cols):
        super().__init__(num_rows, num_cols)
        self.attacker = Attacker()
        self.defender = DefenderBot()

    """def make_move(self, clicked, game, screen):
        self.bot_logic.make_move(clicked, game, screen)

    def make_attack(self, clicked, game):
        self.bot_logic.make_attack(clicked, game)

    def end_ini(self):
        return self.bot_logic.end_ini()

    def initialize_troops(self, clicked, i, game):
        self.bot_logic.initialize_troops(clicked, i, game)

    def draw_button(self, screen, height, width, col):
        self.bot_logic.draw_button(screen, height, width, col)

    def selected_button(self, clicked, i):
        return self.bot_logic.selected_button(clicked, i)"""
