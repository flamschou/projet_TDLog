import pygame
from board import Board


class Player:
    def __init__(self, name):
        self.name = name
        self.troops = []

    def make_move(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
                clicked_pos = pygame.mouse.get_pos()
                print("clicked at", clicked_pos)

                # Check if a troop is clicked
                for troop in self.troops:
                    if troop.rect.collidepoint(clicked_pos):
                        troop.selected = True
                        print("troop selected")
                    else:
                        troop.selected = False

                # Check if a hexagon is clicked
                for hexagon in Board.hexagons:
                    if hexagon.rect.collidepoint(clicked_pos) and any(troop.selected for troop in self.troops):
                        # Move the selected troop to the clicked hexagon
                        for troop in self.troops:
                            if troop.selected:
                                troop.move(hexagon)


class Attacker(Player):
    def __init__(self):
        super().__init__("Attacker")

    def make_move(self):
        # Implement attacker's move logic
        pass  # Placeholder, implement your logic


class Defender(Player):
    def __init__(self):
        super().__init__("Defender")

    def make_move(self):
        # Implement defender's move logic
        pass  # Placeholder, implement your logic
