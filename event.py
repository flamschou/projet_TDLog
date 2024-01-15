# this file contains the class Event and its subclasses
# it defines a list of events and their effects that can happen during the game

import random

# event_types = ["sandstorm", "fire", "adrenalin", "rescue", "betrayal", "expansion"]


class Event:
    def __init__(self, event_type):
        self.event_type = event_type


# this event turns randoms basics hexagons of the board into a sands hexagons
class Sandstorm(Event):
    def __init__(self):
        super().__init__("sandstorm")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if hexagon.hex_type == "basic":
                test = random.choice(
                    [True, False, False, False, False, False, False, False]
                )
                if test:
                    hexagon.toSand()


# this event turns randoms forests hexagons of the board into a basics hexagons
class Fire(Event):
    def __init__(self):
        super().__init__("fire")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if hexagon.hex_type == "forest":
                test = random.choice([True, False, False, False, False, False])
                if test:
                    hexagon.toBasic()


# this event decreases the time by 1
class Rescue(Event):
    def __init__(self):
        super().__init__("rescue")

    def apply_effect(self, game):
        game.time -= 1


# this event increases the time by 1
class Betrayal(Event):
    def __init__(self):
        super().__init__("betrayal")

    def apply_effect(self, game):
        game.time += 1


# this event activates the adrenalin effect (troops are 2 times faster and their attacks are doubled)
class Adrenalin(Event):
    def __init__(self):
        super().__init__("adrenalin")

    def apply_effect(self, game):
        game.adrenalin = 2


# this event makes random unaccessible hexagons accessible ; the board is expanded
class Expansion(Event):
    def __init__(self):
        super().__init__("expansion")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if not hexagon.accessible:
                test = random.choice([True, False, False, False])
                if test:
                    hexagon.accessible = True
