import random
from event import Rain, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from players import Attacker, Defender


class Game:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = Board()
        self.attacker = Attacker()
        self.defender = Defender()
        self.deck = []
        self.time = 20
        self.adrenalin = 1
        self.event_counter = 0

    def generate(self):
        self.board = Board()
        self.board.generate_board(self.num_rows, self.num_cols)
        self.create_deck()
        # initialize players
        # initialize troops

    def draw(self, screen):
        for hexagon in self.board.list:
            hexagon.draw(screen)
        for troop in self.attacker.troops:
            troop.draw(screen)
        for troop in self.defender.troops:
            troop.draw(screen)

    def apply_events(self):
        self.deck[self.event_counter % 54].apply_effect(self)
        self.event_counter += 1

    def get_hexagon_at(self, x, y):
        for hexagon in self.board.list:
            if hexagon.contains(x, y):
                return hexagon
        return None

    def list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.board:
            if abs(hexagon.x-hexagon1.x) < 80 and abs(hexagon.y-hexagon1.y) < 80 and hexagon != hexagon1:
                neighbors.append(hexagon)

        return neighbors

    def neighbors(self, hexagon, hexagon1):
        if hexagon in self.list_neighbors(hexagon1):
            return True
        else:
            return False

    def create_deck(self):
        for i in range(54):
            choice = random.choice(["rain", "fire", "rescue", "betrayal", "adrenalin", "expansion"])
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
