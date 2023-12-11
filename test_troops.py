from troop import Troop, Archer, Assassin, Magician, Turret, Engineer, Shield
from hexagon import Hexagone
from game import Game
import pygame


def test___init__():
    hex = Hexagone("None", 10, 15)
    troop = Troop("None", hex)
    assert troop.troop_type == "None"
    assert troop.hex == hex
    assert troop.hex.occupied
    assert troop.health == 0
    assert troop.attack_capacity == 0
    assert troop.attack_power == 0
    assert troop.status == "none"
    assert troop.default_speed == 0
    assert troop.speed == 0
    assert troop.color == (0, 0, 0)
    assert troop.attack_range == 0
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected


def test___init__Archer():
    hex = Hexagone("None", 10, 15)
    troop = Archer(hex)
    assert troop.troop_type == "archer"
    assert troop.hex == hex
    assert troop.health == 100
    assert troop.attack_capacity == 1
    assert troop.attack_power == 20
    assert troop.status == "none"
    assert troop.default_speed == 5
    assert troop.speed == 5
    assert troop.color == (0, 255, 0)
    assert troop.attack_range == 2
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "defender"


def test___init__Assassin():
    hex = Hexagone("None", 10, 15)
    troop = Assassin(hex)
    assert troop.troop_type == "assassin"
    assert troop.hex == hex
    assert troop.health == 100
    assert troop.attack_capacity == 1
    assert troop.attack_power == 20
    assert troop.status == "none"
    assert troop.default_speed == 5
    assert troop.speed == 5
    assert troop.color == (255, 0, 0)
    assert troop.attack_range == 1
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "attacker"


def test___init__Magician():
    hex = Hexagone("None", 10, 15)
    troop = Magician(hex)
    assert troop.troop_type == "magician"
    assert troop.hex == hex
    assert troop.health == 200
    assert troop.attack_capacity == 1
    assert troop.attack_power == 50
    assert troop.status == "none"
    assert troop.default_speed == 3
    assert troop.speed == 3
    assert troop.color == (255, 0, 0)
    assert troop.attack_range == 2
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "attacker"


def test___init__Turret():
    hex = Hexagone("None", 10, 15)
    troop = Turret(hex)
    assert troop.troop_type == "turret"
    assert troop.hex == hex
    assert troop.health == 500
    assert troop.attack_capacity == 1
    assert troop.attack_power == 100
    assert troop.status == "none"
    assert troop.default_speed == 1
    assert troop.speed == 1
    assert troop.color == (255, 0, 0)
    assert troop.attack_range == 3
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "attacker"


def test___init__Engineer():
    hex = Hexagone("None", 10, 15)
    troop = Engineer(hex)
    assert troop.troop_type == "engineer"
    assert troop.hex == hex
    assert troop.health == 200
    assert troop.attack_capacity == 1
    assert troop.attack_power == 50
    assert troop.status == "none"
    assert troop.default_speed == 3
    assert troop.speed == 3
    assert troop.color == (0, 255, 0)
    assert troop.attack_range == 1
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "defender"


def test___init__Shield():
    hex = Hexagone("None", 10, 15)
    troop = Shield(hex)
    assert troop.troop_type == "shield"
    assert troop.hex == hex
    assert troop.health == 500
    assert troop.attack_capacity == 1
    assert troop.attack_power == 100
    assert troop.status == "none"
    assert troop.default_speed == 1
    assert troop.speed == 1
    assert troop.color == (0, 255, 0)
    assert troop.attack_range == 1
    assert troop.rect == pygame.Rect(troop.hex.x - 10, troop.hex.y - 10, 20, 20)
    assert not troop.selected
    assert troop.player == "defender"


def test_move():
    game = Game(2, 2)
    game.generate()
    game.board.list[0].accessible = True
    game.board.list[1].accessible = True
    hex1 = game.board.list[0]
    hex2 = game.board.list[1]
    troop = Troop("None", hex1)
    troop.speed = 5
    troop.move(hex2, game)

    assert troop.hex == hex2
    assert troop.speed < 5
    assert troop.hex.occupied
    assert not hex1.occupied

    hex1.occupied = True
    speed_aux = troop.speed
    troop.move(hex1, game)

    assert troop.hex == hex2
    assert troop.speed == speed_aux
    assert troop.hex.occupied

    hex1.occupied = False
    troop.speed = 0
    troop.move(hex1, game)

    assert troop.hex == hex2
    assert troop.speed == 0
    assert troop.hex.occupied
    assert not hex1.occupied

    troop.speed = 5
    hex2.toSand()
    troop.move(hex1, game)

    assert troop.hex == hex1
    assert troop.speed == 3
    assert troop.hex.occupied
    assert not hex2.occupied

    troop.speed = 1
    hex1.toSand()
    troop.move(hex2, game)

    assert troop.hex == hex1
    assert troop.speed == 1
    assert troop.hex.occupied
    assert not hex2.occupied


def test_attack():
    game = Game(2, 2)
    game.generate()
    hex1 = game.board.list[0]
    hex2 = game.board.list[1]
    game.board.list[0].accessible = True
    game.board.list[1].accessible = True
    troop1 = Archer(hex1)
    troop2 = Assassin(hex2)
    troop1.attack(troop2, 1, game)

    assert troop2.health == 80
    assert troop1.attack_capacity == 0

    troop1.attack(troop2, 4, game)

    assert troop2.status == "dead"


def test_is_troop_allowed_to_strike():
    game = Game(3, 3)
    game.generate()
    troop2 = Archer(game.board.list[0])
    troop1 = Assassin(game.board.list[1])
    troop3 = Magician(game.board.list[8])

    assert troop1.is_troop_allowed_to_strike(troop2, game)
    assert not troop1.is_troop_allowed_to_strike(troop3, game)

    troop1.attack_capacity = 0

    assert not troop1.is_troop_allowed_to_strike(troop2, game)
