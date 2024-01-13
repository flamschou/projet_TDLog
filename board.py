import random
from hexagon import Basic, Sand, Forest, Rock
import scale

S = scale.scale


class Board:
    def __init__(self):
        self.list = []

    def generate_board(self, num_rows, num_cols):
        for row in range(num_rows):
            for col in range(num_cols):
                hex_type = random.choice(
                    [
                        "basic",
                        "basic",
                        "basic",
                        "basic",
                        "sand",
                        "forest",
                        "forest",
                        "forest",
                        "rock",
                        "rock",
                    ]
                )
                x = col * 60 * S + (30 * S if row % 2 == 0 else 60 * S) + 80 * S
                y = row * 52 * S + 100 * S
                if hex_type == "basic":
                    hexagon = Basic(x, y)
                if hex_type == "sand":
                    hexagon = Sand(x, y)
                if hex_type == "forest":
                    hexagon = Forest(x, y)
                if hex_type == "rock":
                    hexagon = Rock(x, y)
                if random.randint(1, 6) == 1:
                    hexagon.accessible = False
                self.list.append(hexagon)
                hexagon.index = len(self.list) - 1

    def list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 80 * S
                and abs(hexagon.y - hexagon1.y) < 80 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)

        return neighbors

    def neighbors(self, hexagon, hexagon1):
        if hexagon in self.list_neighbors(hexagon1):
            return True
        else:
            return False

    def isdistance(self, hexagon, hexagon1, k):
        if k == 0:
            return hexagon == hexagon1
        else:
            for hexagon2 in self.list_neighbors(hexagon1):
                if self.isdistance(hexagon, hexagon2, k - 1):
                    return True
            return False

    def larger_list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 200 * S
                and abs(hexagon.y - hexagon1.y) < 200 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)

        return neighbors

    def larger_neighbors(self, hexagon, hexagon1):
        if hexagon in self.larger_list_neighbors(hexagon1):
            return True
        else:
            return False

    # permet de trouver un hexagon accessible à partir d'un hexagon donné
    # qui rapproche d'un deuxième hexagone (bot logic)
    def find_destination_hex(self, hexagon1, hexagon2):
        hexagon1_neighbors = self.list_neighbors(hexagon1)

        for neighbor in hexagon1_neighbors:
            # check if the distance between neighbor and hexagon2 is
            # equal to the distance between hexagon1 and hexagon2 minus 1
            if self.isdistance(neighbor, hexagon2, hexagon1.rect.width / (60 * S) - 1):
                return neighbor

        return None
