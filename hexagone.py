# create the class hexagone for the board

class hexagon:
    """
    Each hexagon will constitute the board, and the edifferent subclasses will
    constitute the different type of squares of the game.

    The hexagons will have different properties depending on their type.

    The first one is the accessibility : all of the hexagon can switch from accessible
    to not accessible during the game, knowing that at the beginning the configuration
    is precisely defined.

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
        self._type = None
        self._accessibility = True
        self._players = []

    @property
    def index(self):
        return self._index

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def type(self):
        return self._type

    @property
    def accessibility(self):
        return self._accessibility

class basicHex(hexagon):
    """
    The basic hexagon is the one that is the most common on the board.
    It is the one that will be used to create the board.
    """
    def __init__(self, index, x, y):
        super().__init__(index, x, y)
        self._type = "basic"
