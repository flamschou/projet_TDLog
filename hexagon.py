import pygame
from event import Event


class Hexagone:
    def __init__(self, hex_type, x, y):
        self.hex_type = hex_type
        self.x = x
        self.y = y
        self.color = None
        self.accessible = True
        self.index = None
        self.occupied = False

    def draw(self, screen):
        hex_center_x = self.x
        hex_center_y = self.y
        hex_radius = 30
        if self.accessible:
            pygame.draw.polygon(screen, self.color, [
                (hex_center_x, hex_center_y - hex_radius),
                (hex_center_x + int(hex_radius * 0.866),
                 hex_center_y - int(hex_radius / 2)),
                (hex_center_x + int(hex_radius * 0.866),
                 hex_center_y + int(hex_radius / 2)),
                (hex_center_x, hex_center_y + hex_radius),
                (hex_center_x - int(hex_radius * 0.866),
                 hex_center_y + int(hex_radius / 2)),
                (hex_center_x - int(hex_radius * 0.866),
                 hex_center_y - int(hex_radius / 2))
            ])
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.index), True, (0, 0, 0))
        text_rect = text.get_rect(center=[hex_center_x, hex_center_y+hex_radius*0.6])
        screen.blit(text, text_rect)


    def toBasic(self):
        self.hex_type = "basic"
        self.color = (200, 200, 200)

    def toSwamp(self):
        self.hex_type = "swamp"
        self.color = (0, 128, 0)


class Basic(Hexagone):
    def __init__(self, x, y):
        super().__init__("basic", x, y)
        self.color = (205, 133, 63)


class Swamp(Hexagone):
    def __init__(self, x, y):
        super().__init__("swamp", x, y)
        self.color = (139, 69, 19)


class Forest(Hexagone):
    def __init__(self, x, y):
        super().__init__("forest", x, y)
        self.color = (0, 100, 0)


class Rock(Hexagone):
    def __init__(self, x, y):
        super().__init__("rock", x, y)
        self.color = (128, 128, 128)
