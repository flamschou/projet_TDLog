# import pygame
import random


class Evenement:
    def __init__(self, event_type):
        self.event_type = event_type


class Rain(Evenement):
    def __init__(self):
        super().__init__("rain")

    def apply_effect(self, plateau):
        for hexagon in plateau.board:
            if hexagon.hex_type == "basic":
                test = random.choice([True, False, False, False])
                if test:
                    hexagon.toSwamp()
