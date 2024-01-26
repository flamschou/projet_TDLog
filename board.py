# This file contains the Board class, which is used to generate the hexagonal board
# It also contains various functions to find neighbors of hexagons, to check if hexagons are neighbors, etc.

# Imports
import random
from hexagon import Basic, Sand, Forest, Rock
import scale
import pygame

S = scale.scale


class Board:
    def __init__(self):
        self.list = []
        self.mat_distance = []

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
                if random.randint(1, 8) == 1:
                    hexagon.accessible = False
                self.list.append(hexagon)
                hexagon.index = len(self.list) - 1

    # gives the distance between two hexagons
    def distance_between_hexagons(self, index1, index2, num_cols):
        # checks for valid indexs
        if (
            index1 < 0
            or index2 < 0
            or index1 >= len(self.list)
            or index2 >= len(self.list)
        ):
            raise ValueError("Invalid indices")

        row1, col1 = divmod(index1, num_cols)
        row2, col2 = divmod(index2, num_cols)

        delta_col = abs(col1 - col2)
        delta_row = abs(row1 - row2)

        # gives the distance between two hexagons
        if delta_col != 0:
            if delta_col <= delta_row:
                if delta_row % 2 != 0:
                    delta_col += 1
                return delta_row + (delta_col) // 2
            if delta_col > delta_row:
                if delta_row % 2 != 0:
                    delta_row += 1
                return delta_col + (delta_row) // 2
        else:
            return delta_row

    # gives list of the neighbors of an hexagon
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

    # check if hexagons are neighbors
    def neighbors(self, hexagon, hexagon1):
        if hexagon in self.list_neighbors(hexagon1):
            return True
        else:
            return False

    # check if hexagons are at distance k or lower
    def isdistance(self, hexagon, hexagon1, k):
        if k == 0:
            return hexagon == hexagon1
        else:
            for hexagon2 in self.list_neighbors(hexagon1):
                if self.isdistance(hexagon, hexagon2, k - 1):
                    return True
            return False

    # creates a list of heaxgons at distance larger than in the list_neighbors function
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

    # again but with a larger distance again (we should have made a function with a parameter k but we didn't)
    def quite_larger_list_neighbors(self, hexagon1):
        neighbors = []

        for hexagon in self.list:
            if (
                abs(hexagon.x - hexagon1.x) < 150 * S
                and abs(hexagon.y - hexagon1.y) < 150 * S
                and hexagon != hexagon1
            ):
                neighbors.append(hexagon)
        random.shuffle(neighbors)
        return neighbors

    # test for larger neighbors
    def larger_neighbors(self, hexagon, hexagon1):
        if hexagon in self.larger_list_neighbors(hexagon1):
            return True
        else:
            return False

    # select a hexagon far from the defended hexagon
    def select_far_hex(self, defended_hex):
        i = 0
        j = 0
        entiers = list(range(0, len(self.list)))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        provided_list = self.quite_larger_list_neighbors(defended_hex)
        while j == 0:
            if self.list[entiers_aleatoires[i]] not in provided_list:
                far_hex = self.list[entiers_aleatoires[i]]
                j += 1
            else:
                i += 1
        return far_hex

    # select a destination hexagon for a troop to go towards any hexagon
    def find_destination_hex(self, hexagon1, hexagon2):
        hexagon1_neighbors = self.list_neighbors(hexagon1)
        desti = None
        for neighbor in hexagon1_neighbors:
            if neighbor.accessible and not neighbor.occupied:
                pygame.time.delay(10)
                if (
                    self.distance_between_hexagons(neighbor.index, hexagon2.index, 10)
                    == self.distance_between_hexagons(
                        hexagon1.index, hexagon2.index, 10
                    )
                    - 1
                ):
                    desti = neighbor

        return desti
