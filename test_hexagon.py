from hexagon import Hexagone


def test___init__():
    hexagon = Hexagone("rock", 10, 15)
    assert hexagon.hex_type == "rock"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.color == (128, 128, 128)
    assert hexagon.index is None


def test_toBasic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()
    assert hexagon.hex_type == "basic"
    assert hexagon.color == (205, 133, 63)


def test_toSwamp():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSwamp()
    assert hexagon.hex_type == "swamp"
    assert hexagon.color == (139, 69, 19)


def test_toDefended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()
    assert hexagon.hex_type == "defended"
    assert hexagon.color == (255, 20, 147)
