from game import Game
from troop import Assassin, Archer
import scale

S = scale.scale


def test___init__():
    num_rows = 5
    num_cols = 5
    game = Game(num_rows, num_cols)
    assert game.num_rows == num_rows
    assert game.num_cols == num_cols
    assert game.board is not None
    assert game.attacker is not None
    assert game.defender is not None
    assert game.current_player == game.defender
    assert game.deck == []
    assert game.time == 3
    assert game.adrenalin == 1
    assert game.event_counter == 0
    assert game.attack is None
    assert game.winner is None


def test_create_deck():
    num_rows = 5
    num_cols = 5
    game = Game(num_rows, num_cols)
    game.create_deck()

    assert len(game.deck) == 54
    for i in range(54):
        assert game.deck[i].event_type in [
            "rain",
            "fire",
            "rescue",
            "betrayal",
            "adrenalin",
            "expansion",
        ]


"""
def test_get_hexagon_at():
    num_rows = 2
    num_cols = 2
    game = Game(num_rows, num_cols)
    game.generate()

    assert game.get_hexagon_at(110, 100) == game.board.list[0]
    assert game.get_hexagon_at(170, 100) == game.board.list[1]
    assert game.get_hexagon_at(110, 152) == game.board.list[2]
    assert game.get_hexagon_at(170, 152) == game.board.list[3]
    assert game.get_hexagon_at(100, 100) is None
"""


def test_apply_events():
    num_rows = 2
    num_cols = 2
    game = Game(num_rows, num_cols)
    game.create_deck()

    game.apply_events()
    assert game.event_counter == 1

    game.apply_events()
    assert game.event_counter == 2

    game.event_counter = 52
    game.apply_events()
    assert game.event_counter == 53


def test_change_player():
    num_rows = 2
    num_cols = 2
    game = Game(num_rows, num_cols)
    game.create_deck()

    game.change_player()
    assert game.current_player == game.attacker
    assert game.event_counter == 1

    game.change_player()
    assert game.current_player == game.defender
    assert game.event_counter == 1


def test_eliminations():
    num_rows = 4
    num_cols = 4
    game = Game(num_rows, num_cols)
    game.generate()

    game.attacker.troops.append(Assassin(game.board.list[0]))
    game.attacker.troops.append(Assassin(game.board.list[1]))

    game.defender.troops.append(Archer(game.board.list[2]))
    game.defender.troops.append(Archer(game.board.list[3]))

    game.attacker.troops[0].status = "dead"
    game.eliminations()

    assert len(game.attacker.troops) == 1
    assert len(game.defender.troops) == 2

    game.defender.troops[0].status = "dead"
    game.eliminations()

    assert len(game.attacker.troops) == 1
    assert len(game.defender.troops) == 1

    game.defender.troops[0].status = "dead"
    game.eliminations()

    assert len(game.attacker.troops) == 1
    assert len(game.defender.troops) == 0
    assert game.winner == game.attacker
