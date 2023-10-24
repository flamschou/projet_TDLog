def min_opt(curr, new):
    """
    Returns the minimum between an optional value and a value,
    `None` being considered as above all values.
    """
    return new if curr is None or new < curr else curr


class Screen:
    """
    A screen is basically a two-dimensional array of characters.

    It redefines the indexing operators so that it is possible to
    access the elements using the `[x, y]` notation (both to read
    and to write elements).
    """

    def __init__(self, width, height):
        assert width >= 0, "invalid width"
        assert height >= 0, "invalid height"
        self._width = width
        self._height = height
        self._lines = [[None] * width for _ in range(height)]

    @staticmethod
    def char_of_optional(opt):
        if opt is None:
            return " "
        else:
            return opt

    def __getitem__(self, key):
        x, y = key
        return Screen.char_of_optional(self._lines[y][x])

    def __setitem__(self, key, value):
        x, y = key
        self._lines[y][x] = value

    def __str__(self):
        return "\n".join(
            ["".join(map(Screen.char_of_optional, line)) for line in self._lines]
        )

    def place_string(self, x, y, string):
        for idx, char in enumerate(string):
            assert self._lines[y][x + idx] is None, "overlapping"
            self._lines[y][x + idx] = char

    def place_strings(self, x, y, strings):
        for idx, string in enumerate(strings):
            self.place_string(x, y + idx, string)
