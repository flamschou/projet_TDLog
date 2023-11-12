import random
from hexagon import Basic, Swamp, Forest, Rock


class Board():
    def __init__(self):
        self.list = []

    def generate_board(self, num_rows, num_cols):
        for row in range(num_rows):
            for col in range(num_cols):
                hex_type = random.choice(["basic", "basic", "basic", "swamp", "forest", "rock"])
                x = col * 60 + (30 if row % 2 == 0 else 60) + 80
                y = row * 52 + 100
                if hex_type == "basic":
                    hexagon = Basic(x, y)
                if hex_type == "swamp":
                    hexagon = Swamp(x, y)
                if hex_type == "forest":
                    hexagon = Forest(x, y)
                if hex_type == "rock":
                    hexagon = Rock(x, y)
                if random.randint(1, 5) == 1:
                    hexagon.accessible = False
                self.list.append(hexagon)
                hexagon.index = len(self.list) - 1
