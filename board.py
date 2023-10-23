# load and create a board

import enum
import hexagone


class RelativePosition(enum.Enum):
    """
    The possible relative positions of a hexagon, with respect to the previous
    square.
    """

    TOP = "top"
    TOP_LEFT = "top-left"
    TOP_RIGHT = "top-right"
    BOTTOM = "bottom"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_RIGHT = "bottom-right"


# The dictionary from names (strings) to instances for all relative positions
RELATIVE_POSITIONS = {
    relative_position.value: relative_position for relative_position in RelativePosition
}


class HexagonKind(enum.Enum):
    """
    The possible kinds of hexagons.
    """

    BASIC = "basic"


# The dictionary from names (strings) to instances for all square kinds
HEXAGON_KINDS = {kind.value: kind for kind in HexagonKind}


class InvalidData(Exception):
    """
    The parent class for the exceptions which can be raised if the contents of a
    file specifying a board is invalid.
    """

    def __init__(self, message):
        super().__init__()
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self._message


class InvalidLine(InvalidData):
    """
    The exception to be raised when a line is not a valid specification for a square.
    """

    def __init__(self, line_num, message):
        super().__init__(message)
        self._line_num = line_num

    @property
    def line_num(self):
        return self._line_num


class InvalidBoard(InvalidData):
    """
    The exception to be raised when constraints over the board do not hold.
    """

    def __init__(self, message: str):
        super().__init__(message)


def decode_line(
    line: str,
    line_num: int,
):
    """
    Decodes a line from the board description file, returning a tuple with:
    - the hexagone kind;
    - the list of additional parameters;
    - the (optional) relative position with respect to the previous square.

    Raises `InvalidLine` if the passed string is invalid.

    Returns `None` if the passed string is empty (ignoring whitespace).
    """
    assert line_num > 0, "invalid line_num"
    stripped = line.strip()
    if stripped:
        parts = stripped.split(sep=" ")
        if parts[0] not in HEXAGON_KINDS:
            raise InvalidLine(line_num, f"invalid kind {parts[0]!r}")
        kind = HEXAGON_KINDS[parts[0]]
        if len(parts) > 1:
            if parts[-1] not in RELATIVE_POSITIONS:
                raise InvalidLine(line_num, f"invalid relative position {parts[-1]!r}")
            relative_position = RELATIVE_POSITIONS[parts[-1]]
        else:
            relative_position = None
        parameters = filter(lambda s: len(s) > 0, parts[1:-1])
        return (kind, list(parameters), relative_position)
    else:
        return None


def check_hexagons(hexagons):
    """
    Checks whether the passed list is a valid board, raising `InvalidBoard` if it is
    not.

    Each element of the list is a tuple with the following components:
    - the x coordinate of the square (`int`);
    - the y coordinate of the square (`int`);
    - the kind of the square (`SquareKind`);
    - the parameters for the construction of the square (`str` list);
    - the relative position of the square (optional `RelativePosition`).
    """

    REL_POS_IDX = 4
    if len(hexagons) < 10:
        raise InvalidBoard("a board must have at least 10 hexagons")
    if hexagons[0][REL_POS_IDX] is not None:
        raise InvalidBoard("a board must have a first square with no relative position")
    if hexagons[-1][REL_POS_IDX] is None:
        raise InvalidBoard("a board must have a relative position for the last square")
    for hexagon in hexagons[1:-1]:
        if hexagon[REL_POS_IDX] is None:
            raise InvalidBoard(
                "a board must have a relative position for all squares in the middle"
            )
