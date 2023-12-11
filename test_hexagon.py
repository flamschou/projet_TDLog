from hexagon import Hexagone, Rock, Basic, Sand, Forest, Defended


def test___init__():
    hexagon = Hexagone("None", 10, 15)

    assert hexagon.hex_type == "None"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Basic():
    hexagon = Basic(10, 15)

    assert hexagon.hex_type == "basic"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Sand():
    hexagon = Sand(10, 15)

    assert hexagon.hex_type == "sand"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Forest():
    hexagon = Forest(10, 15)

    assert hexagon.hex_type == "forest"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Rock():
    hexagon = Rock(10, 15)

    assert hexagon.hex_type == "rock"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Defended():
    hexagon = Defended(10, 15)

    assert hexagon.hex_type == "Defended"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test_toBasic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()

    assert hexagon.hex_type == "basic"


def test_toSand():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSand()

    assert hexagon.hex_type == "sand"


def test_toDefended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()

    assert hexagon.hex_type == "Defended"
