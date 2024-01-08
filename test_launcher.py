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
        test.board.list[i].accessible = True

    test.defender.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)
    test.attacker.ini_troops_available(SCREEN_WIDTH, SCREEN_HEIGHT)

    test.time = 3

    # initialisation de l'hexagon à défendre
    test.current_player.initialize_troops((106, 100), test)

    # initialisation des troupes du défenseur
    while not test.current_player.troops_available[0][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150 * S), test
        )

    test.current_player.initialize_troops((106, 100), test)
    test.current_player.initialize_troops((164, 100), test)

    while not test.current_player.troops_available[1][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180 * S), test
        )
    test.current_player.initialize_troops((136, 146), test)

    while not test.current_player.troops_available[2][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 210 * S), test
        )
    test.current_player.initialize_troops((194, 146), test)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    print("attacker turn")

    # initialisation des troupes de l'attaquant

    while not test.current_player.troops_available[0][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 150), test
        )
    test.current_player.initialize_troops((222, 196), test)
    test.current_player.initialize_troops((280, 196), test)

    while not test.current_player.troops_available[1][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 180 * S), test
        )
    test.current_player.initialize_troops((252, 246), test)

    while not test.current_player.troops_available[2][3]:
        test.current_player.initialize_troops(
            (SCREEN_WIDTH - 150 * S, SCREEN_HEIGHT - 210 * S), test
        )
    test.current_player.initialize_troops((308, 246), test)

    for troop in test.current_player.troops:
        print(troop.hex.index, troop.troop_type)

    print("fin init")

    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    print("defender turn")

    # on fait bouger et attaquer les troupes du défenseur

    test.current_player.make_move((164, 100), test)
    test.current_player.make_move((222, 100), test)
    test.current_player.make_move((222, 100), test)
    test.current_player.make_move((280, 196), test)
    test.current_player.make_move((222, 100), test)
    test.current_player.make_move((280, 100), test)

    test.current_player.make_move((106, 100), test)
    test.current_player.make_move((164, 100), test)
    test.current_player.make_move((222, 100), test)
    test.current_player.make_move((222, 196), test)
    test.current_player.make_move((252, 146), test)
    test.current_player.make_move((308, 146), test)

    test.current_player.make_move((136, 146), test)
    test.current_player.make_move((106, 100), test)

    test.current_player.make_move((194, 146), test)
    test.current_player.make_move((222, 196), test)

    test.eliminations()

    test.current_player.make_move((194, 146), test)
    test.current_player.make_move((164, 196), test)

    # on change de joueur

    test.current_player.regenerate_speed()
    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    test.current_player.make_move((296, 210), test)
    test.current_player.make_move((235, 210), test)

    test.current_player.make_move((235, 210), test)
    test.current_player.make_move((174, 210), test)

    test.current_player.make_move((235, 210), test)
    test.current_player.make_move((205, 156), test)

    test.current_player.make_move((205, 156), test)
    test.current_player.make_move((266, 156), test)

    test.current_player.make_move((266, 156), test)
    test.current_player.make_move((296, 103), test)

    test.current_player.make_move((266, 261), test)
    test.current_player.make_move((174, 210), test)

    test.current_player.make_move((327, 261), test)
    test.current_player.make_move((296, 210), test)

    test.current_player.make_move((296, 210), test)
    test.current_player.make_move((174, 210), test)

    test.current_player.regenerate_speed()
    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    test.current_player.regenerate_speed()
    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    test.current_player.make_move((296, 210), test)
    test.current_player.make_move((174, 210), test)

    test.current_player.make_move((266, 261), test)
    test.current_player.make_move((174, 210), test)

    test.current_player.regenerate_speed()
    test.change_player()

    if test.deck[test.event_counter - 1].event_type == "Rescue":
        test.time += 1

    test.winner = test.defender

    assert test.time == 0
    assert test.winner == test.defender


test_scenario()
