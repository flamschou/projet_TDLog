from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import random
from players import Player
import pygame


class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
        self.bot_logic = None
        self.position = (0, 0)

    def simuler_clic(self):
        # créé un évènement de clic à la position du bot
        pygame.event.post(
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": self.position})
        )

    def set_bot_logic(self, bot_logic):
        self.bot_logic = bot_logic

    def selected_button(self, clicked_pos):
        for index, troop in enumerate(self.troops_available):
            if troop.button.collidepoint(clicked_pos):
                self.button_selected = True
                print("button selected")
                return index

        return None


# ATTAQUANT BOT
# notons ici que on a privilégié le dévelopmment du défenseur, donc dabord tester le défenseur bot
class AttackerBot(Bot):
    def __init__(self):
        super().__init__("AttackerBot", "Attacker")
        self.troops_available = [
            ["assassin", 1],
            ["assassin", 1],
            ["magician", 1],
            ["turret", 1],
        ]
        self.position = (0, 0)

    def initialize_bot_logic(self):
        self.set_bot_logic(self)

    # implémentation de la logique du bot attaquant, en utilisant la génération de clicks...
    def make_move(self, game):
        # logique pour l'attaquant bot (pour l'instant identique au défenseur)
        if self.playing:
            # vérifier si une troupe est sélectionnée
            if self.selected_troop_index is not None:
                selected_troop = self.troops[self.selected_troop_index]
                self.use_selected_troop(selected_troop, game)

            else:
                # aucune troupe n'est sélectionnée, en sélectionner une
                self.select_random_troop(game)

    # sélectionne une troupe aléatoire
    def select_random_troop(self, game):
        self.selected_troop_index = self.troops.index(random.choice(self.troops))
        self.position = (
            self.troops[self.selected_troop_index].hex.x,
            self.troops[self.selected_troop_index].hex.y,
        )
        self.simuler_clic()
        print(
            "clic simule et troupe selectionnee"
            + str(self.troops[self.selected_troop_index])
        )

    # si une troupe est sélectionnée, l'utiliser
    def use_selected_troop(self, selected_troop, game):
        # vérifier si la troupe a une capacité d'attaque non nulle
        if selected_troop.attack_capacity > 0:
            # vérifier si la troupe peut attaquer une troupe ennemie
            attackable_troops = [
                troop
                for troop in game.attacker.troops
                if game.board.isdistance(
                    selected_troop.hex, troop.hex, selected_troop.attack_range
                )
            ]

            if attackable_troops:
                # attaquer une troupe ennemie si il y en a une à portée
                target_troop = random.choice(attackable_troops)
                self.position = (target_troop.hex.x, target_troop.hex.y)
                self.simuler_clic()
                print("cic simulé et troupe attaquée" + str(target_troop))
            else:
                # trouver la troupe ennemie la plus proche et se déplacer vers elle si il reste de la vitesse
                if selected_troop.speed != 0:
                    target_troop = min(
                        game.attacker.troops,
                        key=lambda troop: game.board.get_distance(
                            selected_troop.hex, troop.hex
                        ),
                    )
                    # flake8: noqa
                    if game.board.isdistance(
                        selected_troop.hex,
                        target_troop.hex,
                        selected_troop.speed + selected_troop.attack_range,
                    ):
                        # sé déplacer et attaquer si la troupe est à porté suffisante après le déplacement considérant la vitesse restante
                        while (
                            selected_troop.speed > 0
                            and selected_troop.speed + selected_troop.attack_range
                            > game.board.get_distance(
                                selected_troop.hex, target_troop.hex
                            )
                        ):
                            destination_hex = game.board.find_destination_hex(
                                selected_troop.hex, target_troop.hex
                            )
                            self.position = (destination_hex.x, destination_hex.y)
                            self.simuler_clic()
                            print("cic simulé et troupe déplacée" + str(selected_troop))
                        self.position = (target_troop.hex.x, target_troop.hex.y)
                        self.simuler_clic()
                        print("cic simulé et troupe attaquée" + str(target_troop))
                    else:
                        # se rapprocher de la troupe ennemie et s'arreter là
                        destination_hex = game.board.find_destination_hex(
                            selected_troop.hex, target_troop.hex
                        )
                        self.position = (destination_hex.x, destination_hex.y)
                        self.simuler_clic()
                        print("cic simulé et troupe déplacée" + str(selected_troop))
        else:
            # La troupe n'a pas de capacité d'attaque, ne rien faire
            pass

    def initialize_troops(self, game):
        # placing the troops a bit far from the defended hexagon
        entiers = list(range(0, 18))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        i = 0
        for troop_info in self.troops_available:
            troop_type, troop_count = troop_info
            # Choix de l'hexagone pour placer la troupe, aléatoirement sur la carte
            while i < 18:
                if (
                    not game.board.list[entiers_aleatoires[i]].occupied
                    and game.board.list[entiers_aleatoires[i]].accessible
                    and game.board.list[entiers_aleatoires[i]]
                    not in game.defender.defended_hexagon.larger_neighbors
                ):
                    game.board.larger_list_neighbors(self.defended_hexagon)[
                        entiers_aleatoires[i]
                    ].occupied = True

                    if troop_type == "assassin":
                        new_troop = Assassin(game.board.list[entiers_aleatoires[i]])

                    elif troop_type == "magician":
                        new_troop = Magician(game.board.list[entiers_aleatoires[i]])

                    elif troop_type == "turret":
                        new_troop = Turret(game.board.list[entiers_aleatoires[i]])

                    self.add_troop(new_troop)
                    print(f"{troop_type} placed")
                    break
                i += 1


# DEFENSEUR BOT
class DefenderBot(Bot):
    def __init__(self):
        super().__init__("DefenderBot", "Defender")
        self.troops_available = [
            ["archer", 1],
            ["archer", 1],
            ["shield", 1],
            ["engineer", 1],
        ]
        self.defended_hexagon = None
        self.position = (0, 0)
        self.selected_troop_index = None

    # inutile ?
    def initialize_bot_logic(self):
        self.set_bot_logic(self)

    # implémentation de la logique du bot défenseur, en utilisant la génération de clicks...
    def make_move(self, game):
        # logique pour le défenseur bot
        if self.playing:
            # vérifier si une troupe est sélectionnée
            if self.selected_troop_index is not None:
                selected_troop = self.troops[self.selected_troop_index]
                self.use_selected_troop(selected_troop, game)

            else:
                # aucune troupe n'est sélectionnée, en sélectionner une
                self.select_random_troop(game)

    # sélectionne une troupe aléatoire
    def select_random_troop(self, game):
        self.selected_troop_index = self.troops.index(random.choice(self.troops))
        self.position = (
            self.troops[self.selected_troop_index].hex.x,
            self.troops[self.selected_troop_index].hex.y,
        )
        self.simuler_clic()
        print(
            "clic simule et troupe selectionnee"
            + str(self.troops[self.selected_troop_index])
        )

    # si une troupe est sélectionnée, l'utiliser
    def use_selected_troop(self, selected_troop, game):
        # vérifier si la troupe a une capacité d'attaque non nulle
        if selected_troop.attack_capacity > 0:
            # vérifier si la troupe peut attaquer une troupe ennemie
            attackable_troops = [
                troop
                for troop in game.attacker.troops
                if game.board.isdistance(
                    selected_troop.hex, troop.hex, selected_troop.attack_range
                )
            ]

            if attackable_troops:
                # attaquer une troupe ennemie si il y en a une à portée
                target_troop = random.choice(attackable_troops)
                self.position = (target_troop.hex.x, target_troop.hex.y)
                self.simuler_clic()
                print("cic simulé et troupe attaquée" + str(target_troop))
            else:
                # trouver la troupe ennemie la plus proche et se déplacer vers elle si il reste de la vitesse
                if selected_troop.speed != 0:
                    target_troop = min(
                        game.attacker.troops,
                        key=lambda troop: game.board.get_distance(
                            selected_troop.hex, troop.hex
                        ),
                    )
                    # flake8: noqa
                    if game.board.isdistance(
                        selected_troop.hex,
                        target_troop.hex,
                        selected_troop.speed + selected_troop.attack_range,
                    ):
                        # sé déplacer et attaquer si la troupe est à porté suffisante après le déplacement considérant la vitesse restante
                        while (
                            selected_troop.speed > 0
                            and selected_troop.speed + selected_troop.attack_range
                            > game.board.get_distance(
                                selected_troop.hex, target_troop.hex
                            )
                        ):
                            destination_hex = game.board.find_destination_hex(
                                selected_troop.hex, target_troop.hex
                            )
                            self.position = (destination_hex.x, destination_hex.y)
                            self.simuler_clic()
                            print("cic simulé et troupe déplacée" + str(selected_troop))
                        self.position = (target_troop.hex.x, target_troop.hex.y)
                        self.simuler_clic()
                        print("cic simulé et troupe attaquée" + str(target_troop))
                    else:
                        # se rapprocher de la troupe ennemie et s'arreter là
                        destination_hex = game.board.find_destination_hex(
                            selected_troop.hex, target_troop.hex
                        )
                        self.position = (destination_hex.x, destination_hex.y)
                        self.simuler_clic()
                        print("cic simulé et troupe déplacée" + str(selected_troop))
        else:
            # La troupe n'a pas de capacité d'attaque, ne rien faire
            pass

    def initialize_troops(self, game):
        # choice of the hexagon to defend, now randomly on the map
        i = random.randint(0, len(game.board.list))
        self.defended_hexagon = game.board.list[i]
        game.board.list[i].toDefended()
        print("hexagon defended chosen")
        # defended_hexagon.defended = True not defined yet in hexagon.py

        # placing the troops around the defended hexagon
        entiers = list(range(0, 18))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        i = 0
        for troop_info in self.troops_available:
            troop_type, troop_count = troop_info
            # Choix de l'hexagone pour placer la troupe, aléatoirement sur la carte
            while i < 18:
                if (
                    not game.board.larger_list_neighbors(self.defended_hexagon)[
                        entiers_aleatoires[i]
                    ].occupied
                    and game.board.larger_list_neighbors(self.defended_hexagon)[
                        entiers_aleatoires[i]
                    ].accessible
                ):
                    game.board.larger_list_neighbors(self.defended_hexagon)[
                        entiers_aleatoires[i]
                    ].occupied = True

                    if troop_type == "archer":
                        new_troop = Archer(
                            game.board.larger_list_neighbors(self.defended_hexagon)[
                                entiers_aleatoires[i]
                            ]
                        )

                    elif troop_type == "engineer":
                        new_troop = Engineer(
                            game.board.larger_list_neighbors(self.defended_hexagon)[
                                entiers_aleatoires[i]
                            ]
                        )

                    elif troop_type == "shield":
                        new_troop = Shield(
                            game.board.larger_list_neighbors(self.defended_hexagon)[
                                entiers_aleatoires[i]
                            ]
                        )

                    self.add_troop(new_troop)
                    print(f"{troop_type} placed")
                    break
                i += 1
