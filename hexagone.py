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



class basicHex(hexagon):
    """
    The basic hexagon is the one that is the most common on the board.
    It is the one that will be used to create the board.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "basic"


class emptyHex(hexagon):
    """
    The empty hexagon is the one that is the most common on the board.
    You can build on this hexagon.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "empty"


class swampHex(hexagon):
    """
    The swamp hexagon is an hexagon that is not accessible.
    You can't build on this hexagon.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "swamp"
        self._accessibility = False
        self.constructible = False


class forestHex(emptyHex):
    """
    The forest hexagon is an hexagon that is not accessible by vehicles.
    Zadists fight better in this type of hexagon.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "forest"
