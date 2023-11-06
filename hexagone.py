import pygame


class Hexagone:
    def __init__(self, hex_type, x, y):
        self.hex_type = hex_type
        self.x = x
        self.y = y

    def draw(self, screen):
        color_mapping = {
            "basic": (200, 200, 200),
            "swamp": (0, 128, 0),
            "forest": (0, 100, 0),
        }

        hex_center_x = self.x
        hex_center_y = self.y
        hex_radius = 30

        pygame.draw.polygon(screen, color_mapping[self.hex_type], [
            (hex_center_x, hex_center_y - hex_radius),
            (hex_center_x + int(hex_radius * 0.866), hex_center_y - int(hex_radius / 2)),
            (hex_center_x + int(hex_radius * 0.866), hex_center_y + int(hex_radius / 2)),
            (hex_center_x, hex_center_y + hex_radius),
            (hex_center_x - int(hex_radius * 0.866), hex_center_y + int(hex_radius / 2)),
            (hex_center_x - int(hex_radius * 0.866), hex_center_y - int(hex_radius / 2))
        ])

    def handle_event(self, event):
        pass


    @property
    def color(self):
        return self._color