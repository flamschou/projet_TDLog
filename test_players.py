from players import Player, Attacker, Defender
from troop import Troop, Archer
from hexagon import Hexagone
import pygame
import scale
from game import Game


def test___init__():
    player = Player("test")
    assert player.name == "test"
    assert player.troops == []
    assert player.dices == []
    assert player.troops_available == []
    assert not player.button_selected


def test___init__Attacker():
    attacker = Attacker()

    assert attacker.name == "Attacker"
    assert attacker.troops_available == [
        ["assassin", 2, None, False],
        ["magician", 1, None, False],
        ["turret", 1, None, False],
    ]


def test___init__Defender():
    defender = Defender()

    assert defender.name == "Defender"
    assert defender.troops_available == [
        ["archer", 2, None, False],
        ["engineer", 1, None, False],
        ["shield", 1, None, False],
    ]


def test_add_troop():
    player = Player("test")
    hex = Hexagone("None", 10, 15)
    troop = Troop("None", hex)
    player.add_troop(troop)

    assert player.troops == [troop]


def test_make_move():
    player = Player("test")
    game = Game(2, 2)
    game.generate()
    game.board.list[0].toBasic()
    game.board.list[1].toBasic()
    game.board.list[0].accessible = True
    game.board.list[1].accessible = True
    troop = Troop("None", game.board.list[0])

    player.add_troop(troop)
    player.make_move((106, 100), game)

    assert not troop.selected
    assert troop.hex == game.board.list[0]

    troop.speed = 1

    player.make_move((106, 100), game)

    assert troop.selected
    assert troop.hex == game.board.list[0]

    player.make_move((173, 105), game)

    assert not troop.selected
    assert troop.hex == game.board.list[1]
    assert troop.speed == 0

    troop.speed = 1
    troop.selected = True
    game.board.list[0].accessible = False
    player.make_move((106, 100), game)

    assert not game.board.list[0].accessible
    assert troop.selected
    assert troop.hex == game.board.list[1]
    assert troop.speed == 1


def test_selected_button():
    game = Game(2, 2)
    game.generate()
    S = scale.scale
    SCREEN_WIDTH = 900 * S
    SCREEN_HEIGHT = 600 * S

    current_player = game.defender
    current_player.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

    current_player.selected_button((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150))

    assert current_player.troops_available[0][3]
    assert current_player.button_selected
    assert not current_player.troops_available[1][3]

    game.change_player()
    current_player.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)
    current_player.selected_button((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180))

    assert current_player.troops_available[1][3]
    assert current_player.button_selected

    current_player.troops_available[1][3] = False
    current_player.button_selected = False
    current_player.troops_available[1][1] = 0
    current_player.selected_button((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180))

    assert not current_player.troops_available[1][3]
    assert not current_player.button_selected


def test_ini_troops_available():
    game = Game(2, 2)
    game.generate()
    S = scale.scale
    SCREEN_WIDTH = 900 * S
    SCREEN_HEIGHT = 600 * S
    button_size = (100 * S, 20 * S)

    current_player = game.defender
    current_player.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

    assert current_player.troops_available[0][2] == pygame.Rect(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), button_size
    )
    assert current_player.troops_available[1][2] == pygame.Rect(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180), button_size
    )
    assert current_player.troops_available[2][2] == pygame.Rect(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 210), button_size
    )


def test_initialize_troops():
    game = Game(2, 2)
    game.generate()
    S = scale.scale
    SCREEN_WIDTH = 900 * S
    SCREEN_HEIGHT = 600 * S
    game.board.list[0].toBasic()
    game.board.list[1].toBasic()
    game.board.list[0].accessible = True
    game.board.list[1].accessible = True

    current_player = game.defender
    current_player.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

    current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), game
    )

    assert current_player.troops_available[0][3]
    assert current_player.button_selected

    current_player.troops_available[0][1] = 1

    current_player.initialize_troops((106, 100), game)

    assert current_player.troops_available[0][3]
    assert current_player.button_selected
    assert game.board.list[0].hex_type == "Defended"

    current_player.initialize_troops((106, 100), game)

    assert current_player.troops[0].hex == game.board.list[0]
    assert current_player.troops[0].troop_type == current_player.troops_available[0][0]
    assert current_player.troops_available[0][1] == 0
    assert not current_player.troops_available[0][3]
    assert current_player.button_selected
    assert game.board.list[0].occupied

    current_player.button_selected = False
    current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), game
    )
    current_player.initialize_troops((173, 105), game)

    assert not game.board.list[1].occupied
    assert not current_player.troops_available[0][3]
    assert not current_player.button_selected

    current_player.troops_available[0][1] = 1
    current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), game
    )
    current_player.initialize_troops((106, 100), game)

    assert current_player.troops_available[0][1] == 1
    assert game.board.list[0].occupied
    assert current_player.troops_available[0][3]
    assert current_player.button_selected


def test_end_ini():
    game = Game(2, 2)
    game.generate()

    assert game.current_player.end_ini()

    game.current_player.troops_available[0][1] = 0
    game.current_player.troops_available[1][1] = 0
    game.current_player.troops_available[2][1] = 0

    assert not game.current_player.end_ini()


def test_regenerate_speed():
    player = Player("test")
    hex = Hexagone("None", 10, 15)

    troop = Archer(hex)

    player.add_troop(troop)

    troop.speed = 0
    troop.attack_capacity = 0
    troop.attack_power = 0

    player.regenerate_speed()

    assert troop.speed == troop.default_speed
    assert troop.attack_capacity == troop.default_attack_capacity
    assert troop.attack_power == troop.default_attack_power
