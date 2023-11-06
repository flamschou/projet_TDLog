import random
from hexagone import Basic, Swamp, Forest


class Plateau:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = []
        self.troops = []
        self.events = []

    def generate_board(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                hex_type = random.choice(["basic", "swamp", "forest"])
                x = col * 60 + (30 if row % 2 == 0 else 60) + 60
                y = row * 52 + 30
                if hex_type == "basic":
                    hexagon = Basic(x, y)
                if hex_type == "swamp":
                    hexagon = Swamp(x, y)
                if hex_type == "forest":
                    hexagon = Forest(x, y)
                self.board.append(hexagon)

    def draw(self, screen):
        for hexagon in self.board:
            hexagon.draw(screen)
        for troop in self.troops:
            troop.draw(screen)

    def handle_event(self, event):
        for hexagon in self.board:
            hexagon.handle_event(event)

    def add_troop(self, troop):
        self.troops.append(troop)

    def add_event(self, event):
        self.events.append(event)

    def apply_events(self):
        for event in self.events:
            event.apply_effect(self)
        self.events = []

    def get_hexagon_at(self, x, y):
        for hexagon in self.board:
            if hexagon.contains(x, y):
                return hexagon
        return None
    
    def list_voisins(self, hexagon1):
        voisins = []

        for hexagon in self.board:
            if abs(hexagon.x-hexagon1.x) < 80 and abs(hexagon.y-hexagon1.y) < 80 and hexagon != hexagon1:
                voisins.append(hexagon)

        return voisins
    
    def voisin(self, hexagon, hexagon1):
        if hexagon in self.list_voisins(hexagon1):
            return True
        else:    
            return False

