import pygame
from os import path


class Hexagone:
    def __init__(self, hex_type, x, y):
        self.hex_type = hex_type
        self.x = x
        self.y = y
        self.accessible = True
        self.index = None
        self.occupied = False
        self.rect = pygame.Rect(self.x - 20, self.y - 20, 40, 40)

    def draw(self, screen):
        if self.accessible:
            image_rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, image_rect)

    def toBasic(self):
        self.hex_type = "basic"
        self.image = pygame.image.load(path.join("Images", "hexagon basic.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))

    def toSand(self):
        self.hex_type = "sand"
        self.image = pygame.image.load(path.join("Images", "hexagon sand.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))

    def toDefended(self):
        self.hex_type = "defended"
        self.image = pygame.image.load(path.join("Images", "hexagon defended.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))


class Basic(Hexagone):
    def __init__(self, x, y):
        super().__init__("basic", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon basic.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))


class Defended(Hexagone):
    def __init__(self, x, y):
        super().__init__("Defended", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon defended.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))


class Sand(Hexagone):
    def __init__(self, x, y):
        super().__init__("sand", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon sand.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))


class Forest(Hexagone):
    def __init__(self, x, y):
        super().__init__("forest", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon forest.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))


class Rock(Hexagone):
    def __init__(self, x, y):
        super().__init__("rock", x, y)
        self.image = pygame.image.load(path.join("Images", "hexagon rock.png"))
        self.image = pygame.transform.scale(self.image, (60, 60))
