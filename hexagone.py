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

<<<<<<< HEAD
        hex_center_x = self.x
        hex_center_y = self.y
        hex_radius = 30
=======
    The second one is the position, depending on the couple (x, y), knowing that the one
    at the center has the position (0, 0).
    """
    def __init__(self, index, x, y):
        assert index >= 0, "invalid index"
        assert x >= 0, "invalid x"
        assert y >= 0, "invalid y"
        self._index = index
        self._x = x
        self._y = y
        self._name = None
        self._accessibility = True
        self._players = []
        self._color = None
>>>>>>> 589758e027ca153a7c731eb36b651be2a67b1260

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

<<<<<<< HEAD
=======
    @property
    def y(self):
        return self._y

    @property
    def name(self):
        return self._name

    @property
    def accessibility(self):
        return self._accessibility
>>>>>>> 589758e027ca153a7c731eb36b651be2a67b1260

    @property
    def color(self):
        return self._color


class basicHex(hexagon):
    """
    The basic hexagon is the one that is the most common on the board.
    It is the one that will be used to create the board.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
<<<<<<< HEAD
        self._type = "basic"


class emptyHex(hexagon):
    """
    The empty hexagon is the one that is the most common on the board.
    You can build on this hexagon.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "empty"
=======
        self._name = "basic"
        self._color = "black"
>>>>>>> 589758e027ca153a7c731eb36b651be2a67b1260


class swampHex(hexagon):
    """
<<<<<<< HEAD
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
=======
    The swamp hexagon is the one that will slow down the troops.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._name = "swamp"
        self._color = "orange"


class forestHex(hexagon):
    """
    The forest hexagon is the one that will reduce range of attacks of troops.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._name = "forest"
        self._color = "green"
>>>>>>> 589758e027ca153a7c731eb36b651be2a67b1260
