import random

# event_types = ["rain", "fire", "adrenalin", "rescue", "betrayal", "expansion"]


class Event:
    def __init__(self, event_type):
        self.event_type = event_type


class Rain(Event):
    def __init__(self):
        super().__init__("rain")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if hexagon.hex_type == "basic":
                test = random.choice([True, False, False, False])
                if test:
                    hexagon.toSwamp()


class Fire(Event):
    def __init__(self):
        super().__init__("fire")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if hexagon.hex_type == "forest":
                test = random.choice([True, False, False, False])
                if test:
                    hexagon.toBasic()


class Rescue(Event):
    def __init__(self):
        super().__init__("rescue")

    def apply_effect(self, game):
        game.time -= random.randint(1, 3)


class Betrayal(Event):
    def __init__(self):
        super().__init__("betrayal")

    def apply_effect(self, game):
        game.time += random.randint(1, 3)


class Adrenalin(Event):
    def __init__(self):
        super().__init__("adrenalin")

    def apply_effect(self, game):
        game.adrenaline = 2


class Expansion(Event):
    def __init__(self):
        super().__init__("expansion")

    def apply_effect(self, game):
        for hexagon in game.board.list:
            if not hexagon.accessible:
                test = random.choice([True, False, False, False])
                if test:
                    hexagon.accessible = True
