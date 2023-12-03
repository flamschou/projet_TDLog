from players import Player, Attacker, Defender
from troop import Troop
from hexagon import Hexagone
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
    assert attacker.troops_available == [["assassin", 2], ["magician", 1], ["turret", 1]]


def test___init__Defender():
    defender = Defender()

    assert defender.name == "Defender"
    assert defender.troops_available == [["archer", 2], ["engineer", 1], ["shield", 1]]


def test_add_troop():
    player = Player("test")
    hex = Hexagone("None", 10, 15)
    troop = Troop("None", hex)
    player.add_troop(troop)

    assert player.troops == ["troop"]


def test_make_move():
    player = Player("test")
    game = Game(2, 2)
    game.generate()
    game.board.list[0].accessible = True
    game.board.list[1].accessible = True
    troop = Troop("None", game.board.list[0])
    player.add_troop(troop)

    player.make_move((115, 105), game)

    assert not troop.selected
    assert troop.hex == game.board.list[0]

    troop.speed = 1
    player.make_move((115, 105), game)

    assert troop.selected
    assert troop.hex == game.board.list[0]

    player.make_move((173, 105), game)

    assert not troop.selected
    assert troop.hex == game.board.list[1]
    assert troop.speed == 0

    troop.speed = 1
    game.board.list[0].accessible = False
    player.make_move((115, 105), game)

    assert troop.selected
    assert troop.hex == game.board.list[1]
    assert troop.speed == 1
