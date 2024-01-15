# This file contains the class Hexagone and its subclasses
# It also contains the images of the hexagons


# Imports
import pygame
from os import path
import scale

S = scale.scale


class Hexagone:
    def __init__(self, hex_type, x, y):
        self.hex_type = hex_type
        self.x = x
        self.y = y
        self.accessible = True
        self.index = None
        self.occupied = False
        self.rect = pygame.Rect(self.x - 20 * S, self.y - 20 * S, 40 * S, 40 * S)

    def draw(self, screen):
        if self.accessible:
            image_rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, image_rect)

    def toBasic(self):
        self.hex_type = "basic"
        self.image = pygame.image.load(path.join("Images", "hexagon basic.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))

    def toSand(self):
        self.hex_type = "sand"
        self.image = pygame.image.load(path.join("Images", "hexagon sand.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))

    def toDefended(self):
        self.hex_type = "Defended"
        self.image = pygame.image.load(path.join("Images", "hexagon defended.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))


class Basic(Hexagone):
    def __init__(self, x, y):
        super().__init__("basic", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon basic.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))


class Defended(Hexagone):
    def __init__(self, x, y):
        super().__init__("Defended", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon defended.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))


class Sand(Hexagone):
    def __init__(self, x, y):
        super().__init__("sand", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon sand.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))


class Forest(Hexagone):
    def __init__(self, x, y):
        super().__init__("forest", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon forest.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))


class Rock(Hexagone):
    def __init__(self, x, y):
        super().__init__("rock", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon rock.png"))
        self.image = pygame.transform.scale(self.image, (60 * S, 60 * S))
