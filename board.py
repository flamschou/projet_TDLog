# This file contains the Board class, which is used to generate the hexagonal board
# It also contains various functions to find neighbors of hexagons, to check if hexagons are neighbors, etc.

# Imports
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
                )  # 40% basic, 10% sand, 30% forest and 20% rock
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
                '''if random.randint(1, 6) == 1:
                    hexagon.accessible = False'''
                self.list.append(hexagon)
                hexagon.index = len(self.list) - 1

    def list_neighbors(self, hexagon1):  # gives list of the neighbors of an hexagon
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 80 * S
                and abs(hexagon.y - hexagon1.y) < 80 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)

        return neighbors

    def neighbors(self, hexagon, hexagon1):  # check if hexagons are neighbors
        if hexagon in self.list_neighbors(hexagon1):
            return True
        else:
            return False

    def isdistance(self, hexagon, hexagon1, k):  # check if hexagons are at distance k or lower
        if k == 0:
            return hexagon == hexagon1
        else:
            for hexagon2 in self.list_neighbors(hexagon1):
                if self.isdistance(hexagon, hexagon2, k - 1):
                    return True
            return False

    def distance_on_board(self, hex1, hex2):  # gives the distance between two hexagons
        k = 15
        s = 0
        for i in range(1, 16):
            while s == 0 and i < 16:
                if self.isdistance(hex1, hex2, i):
                    k = i
                    s = 1
        return k

    def larger_list_neighbors(self, hexagon1):  
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 100 * S
                and abs(hexagon.y - hexagon1.y) < 100 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)
        random.shuffle(neighbors)

        return neighbors

    def quite_larger_list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 250 * S
                and abs(hexagon.y - hexagon1.y) < 250 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)
        random.shuffle(neighbors)
        return neighbors

    def larger_neighbors(self, hexagon, hexagon1):
        if hexagon in self.larger_list_neighbors(hexagon1):
            return True
        else:
            return False

    def select_far_hex(self, defended_hex):  # select a hexagon far from the defended hexagon
        i = 0
        j = 0
        entiers = list(range(0, len(self.list)))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        provided_list = self.larger_list_neighbors(defended_hex)
        while j == 0:
            if self.list[entiers_aleatoires[i]] not in provided_list:
                far_hex = self.list[entiers_aleatoires[i]]
                i = 1
            else:
                j += 1
        return far_hex

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
