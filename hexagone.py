import pygame


class Hexagone:
    def __init__(self, hex_type, x, y):
        self.hex_type = hex_type
        self.x = x
        self.y = y
        self.color = None

    def draw(self, screen):
        hex_center_x = self.x
        hex_center_y = self.y
        hex_radius = 30

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

    def handle_event(self, event):
        pass


class Basic(Hexagone):
    def __init__(self, x, y):
        super().__init__("basic", x, y)
        self.color = (200, 200, 200)


class Swamp(Hexagone):
    def __init__(self, x, y):
        super().__init__("swamp", x, y)
        self.color = (0, 128, 0)


class Forest(Hexagone):
    def __init__(self, x, y):
        super().__init__("forest", x, y)
        self.color = (0, 100, 0)
