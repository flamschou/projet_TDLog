from hexagon import Hexagone, Rock
import pygame
from os import path


def test___init__():
    hexagon = Hexagone("None", 10, 15)

    assert hexagon.hex_type == "None"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None


def test___init__Basic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()
    image = pygame.image.load(path.join("Images", "hexagon basic.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "basic"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test___init__Sand():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSand()
    image = pygame.image.load(path.join("Images", "hexagon sand.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "sand"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test___init__Forest():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toForest()
    image = pygame.image.load(path.join("Images", "hexagon forest.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "forest"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test___init__Rock():
    hexagon = Rock(10, 15)
    image = pygame.image.load(path.join("Images", "hexagon rock.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "rock"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test___init__Defended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()
    image = pygame.image.load(path.join("Images", "hexagon defended.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "defended"
    assert hexagon.x == 10
    assert hexagon.y == 15
    assert not hexagon.occupied
    assert hexagon.index is None
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test_toBasic():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toBasic()
    image = pygame.image.load(path.join("Images", "hexagon basic.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "basic"
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test_toSand():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toSand()
    image = pygame.image.load(path.join("Images", "hexagon sand.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "sand"
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')


def test_toDefended():
    hexagon = Hexagone("None", 10, 15)
    hexagon.toDefended()
    image = pygame.image.load(path.join("Images", "hexagon defended.png"))
    image = pygame.transform.scale(image, (60, 60))

    assert hexagon.hex_type == "defended"
    assert pygame.image.tostring(hexagon.image, 'RGBA') == pygame.image.tostring(image, 'RGBA')
