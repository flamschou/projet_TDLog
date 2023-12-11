# scenario complet de partie pour tester le jeu

from game import Game  # HumanVSBotGame
import scale


def test_scenario():
    # Générer un plateau aléatoire
    num_rows = 4  # Nombre de lignes
    num_cols = 4  # Nombre de colonnes

    S = scale.scale

    S = 1

    print(S)

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

    # initialisation de l'hexagon à défendre
    test.current_player.initialize_troops((106, 100), test)

    # initialisation des troupes du défenseur
    test.current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150*S), test
    )
    test.current_player.initialize_troops((106, 100), test)
    test.current_player.initialize_troops((106, 100), test)
    test.current_player.initialize_troops((164, 100), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180*S), test)
    test.current_player.initialize_troops((136, 146), test)

    for troop in test.current_player.troops_available:
        if troop[3]:
            print(troop[0], troop[1])

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 210*S), test)
    test.current_player.initialize_troops((194, 146), test)

    print(test.board.list[5].x, test.board.list[5].y)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    test.change_player()

    print("attacker turn")

    test.current_player.initialize_troops(
        (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), test
    )
    test.current_player.initialize_troops((222, 196), test)
    test.current_player.initialize_troops((280, 196), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 170*S), test)
    test.current_player.initialize_troops((252, 246), test)

    test.current_player.initialize_troops((SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 190*S), test)
    test.current_player.initialize_troops((308, 246), test)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    print("fin init")

    test.change_player()

    print("defender turn")


test_scenario()
