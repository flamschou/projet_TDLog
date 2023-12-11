# scenario complet de partie pour tester le jeu

from game import Game  # HumanVSBotGame
import scale


def test_scenario():
    # Générer un plateau aléatoire
    num_rows = 4  # Nombre de lignes
    num_cols = 4  # Nombre de colonnes

    S = scale.scale

    # Paramètres de la fenêtre
    SCREEN_WIDTH = 900 * S
    SCREEN_HEIGHT = 600 * S

    # partie humain vs humain
    test = Game(num_rows, num_cols)
    test.generate()

    for i in range(16):
        test.board.list[i].toBasic()

    test.defender.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)
    test.attacker.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

    test.time = 3

    test.current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), test
    )
    test.current_player.initialize_troops((106, 100), test)
    test.current_player.initialize_troops((106, 100), test)
    test.current_player.initialize_troops((164, 100), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 190), test)
    test.current_player.initialize_troops((136, 146), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 170), test)
    test.current_player.initialize_troops((194, 146), test)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    test.change_player()

    print("attacker turn")

    test.current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), test
    )
    test.current_player.initialize_troops((222, 196), test)
    test.current_player.initialize_troops((280, 196), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 190), test)
    test.current_player.initialize_troops((252, 246), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 170), test)
    test.current_player.initialize_troops((308, 246), test)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    print("fin init")

test_scenario()
