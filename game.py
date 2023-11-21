import random
from event import Rain, Fire, Rescue, Betrayal, Adrenalin, Expansion
from board import Board
from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
from players import Attacker, Defender


class Game:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = Board()
        self.attacker = Attacker()
        self.defender = Defender()
        self.troops = []
        self.deck = []
        self.time = 20
        self.adrenalin = 1
        self.event_counter = 0
        self.button_selected = False
        self.troops_available = [["assassin", 2], ["archer", 2], ["magician", 1], ["engineer", 1], ["turret", 1], ["shield", 1]]

    def generate(self):
        self.board = Board()
        self.board.generate_board(self.num_rows, self.num_cols)
        self.create_deck()
        # initialize players
        # initialize troops

    def draw(self, screen):
        for hexagon in self.board.list:
            hexagon.draw(screen)
        for troop in self.troops:
            troop.draw(screen)

    def add_troop(self, troop):
        self.troops.append(troop)

    def selected_button(self, clicked, i):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        for j in range(len(self.troops_available)):
            if self.troops_available[j][2].collidepoint(clicked_pos) and self.troops_available[j][1] > 0:
                self.button_selected = True
                return (j)

        else:
            return (i)

    def initialize_troops(self, clicked, i):
        # beginning of the game, the attacker starts by placing his troops

        clicked_pos = clicked
        print("clicked at", clicked_pos)

        for hexagon in self.board.list:
            if hexagon.rect.collidepoint(clicked_pos) and self.button_selected:
                if not hexagon.occupied and hexagon.accessible:
                    hexagon.occupied = True
                    if self.troops_available[i][0] == "archer":
                        troop = Archer(hexagon)

                    elif self.troops_available[i][0] == "assassin":
                        troop = Assassin(hexagon)
                    
                    elif self.troops_available[i][0] == "magician":
                        troop = Magician(hexagon)

                    elif self.troops_available[i][0] == "engineer":
                        troop = Engineer(hexagon)
                    
                    elif self.troops_available[i][0] == "turret":
                        troop = Turret(hexagon)

                    elif self.troops_available[i][0] == "shield":
                        troop = Shield(hexagon)

                    self.add_troop(troop)
                    self.attacker.troops.append(troop)
                    print("troop placed")
                    self.troops_available[i][1] -= 1
                    print(self.troops_available[i][1])
                    self.button_selected = False
                elif hexagon.occupied:
                    print("this hexagon is already occupied")
                else:
                    print("this hexagon is not accessible")

    def end_ini(self):
        S = 0
        for troop in self.troops_available:
            S += troop[1]

        if S == 0:
            return False
        else:
            return True

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
