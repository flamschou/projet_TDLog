import random
from event import Rain, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from troop import Assassin, Magician, Turret


class Game:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = None
        self.troops = []
        self.deck = []
        self.time = 20
        self.adrenalin = 1

    def generate(self):
        self.board = Board()
        self.board.generate_board(self.num_rows, self.num_cols)
        self.create_deck()
        self.place_troops()
        # initialize players

    def draw(self, screen):
        for hexagon in self.board.list:
            hexagon.draw(screen)
        for troop in self.troops:
            troop.draw(screen)

    def handle_event(self, event):
        for hexagon in self.board.list:
            hexagon.handle_event(event)

    def add_troop(self, troop):
        self.troops.append(troop)

    def place_troops(self):
        a1 = Assassin(self.board.list[0])
        self.add_troop(a1)
        m1 = Magician(self.board.list[10])
        self.add_troop(m1)
        t1 = Turret(self.board.list[1])
        self.add_troop(t1)

    def apply_events(self):
        for event in self.deck:
            event.apply_effect(self)
        self.events = []

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
