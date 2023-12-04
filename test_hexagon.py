from hexagon import Hexagone, Rock
import pygame
from os import path


def test___init__():
    hexagon = Rock(10, 15)
    assert hexagon.hex_type == "rock"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert hexagon.image == pygame.transform.scale(
        pygame.image.load(path.join("Images", "hexagon rock.png"), (60, 60))
    )


def test_toBasic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()
    assert hexagon.hex_type == "basic"
    assert hexagon.image == pygame.transform.scale(
        pygame.image.load(path.join("Images", "hexagon basic.png"), (60, 60))
    )


def test_toSand():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSand()
    assert hexagon.hex_type == "sand"
    assert hexagon.image == pygame.transform.scale(
        pygame.image.load(path.join("Images", "hexagon sand.png"), (60, 60))
    )


def test_toDefended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()
    assert hexagon.hex_type == "defended"
    assert hexagon.image == pygame.transform.scale(
        pygame.image.load(path.join("Images", "hexagon defended.png"), (60, 60))
    )
