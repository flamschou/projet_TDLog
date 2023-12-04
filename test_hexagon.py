from hexagon import Hexagone, Rock
import pygame
from os import path


def test___init__():
    hexagon = Rock(10, 15)
    image = pygame.image.load(path.join("Images", "hexagon rock.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "rock"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert hexagon.image == image


def test_toBasic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()
    image1 = pygame.image.load(path.join("Images", "hexagon basic.png"))
    image1 = pygame.transform.scale(image1, (60, 60))

    assert hexagon.hex_type == "basic"
    assert hexagon.image == image1


def test_toSand():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSand()
    image = pygame.image.load(path.join("Images", "hexagon sand.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "sand"
    assert hexagon.image == image


def test_toDefended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()
    image = pygame.image.load(path.join("Images", "hexagon defended.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "defended"
    assert hexagon.image == image
