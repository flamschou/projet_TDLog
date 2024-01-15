from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import random
from players import Player
import pygame
import time
import scale

S = scale.scale


class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
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

    def distance_with_opponants(self, game, troop, player):
        L = []
        I = []
        for i in range(4):
            L.append(
                [
                    player.troops[i],
                    game.board.distance_on_board(troop.hex, player.troops[i].hex),
                ]
            )
            I.append(game.board.distance_on_board(troop.hex, player.troops[i].hex))
        return L, I

    def find_attackable_troop(self, game, troop, player):
        List, Index = self.distance_with_opponants(game, troop, player)
        i = Index.index(min(Index))
        return List[i]


# ATTAQUANT BOT
# notons ici que on a privilégié le dévelopmment du défenseur, donc dabord tester le défenseur bot
class AttackerBot(Bot):
    def __init__(self):
        super().__init__("AttackerBot", "Attacker")
        self.troops_available = [
            ["assassin", 2],
            ["magician", 1],
            ["turret", 1],
        ]
        self.position = (0, 0)

    # implémentation de la logique du bot attaquant, en utilisant la génération de clicks...
    """def make_move(self, game):
        # logique pour l'attaquant bot (pour l'instant identique au défenseur)
        for selected_troop in self.troops:
            self.use_selected_troop(selected_troop, game)

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
    
    def win_for_attack(self, game):
        pass
"""

    # bie nimplémentée pour le défenseur mais faire de même pour l'attaquant
    def initialize_troops(self, game):
        # placing the troops a bit far from the defended hexagon
        entiers = list(range(0, 18))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        i = 0
        central_hex = game.board.select_far_hex(game.defended_hex)
        possibilities = game.board.larger_list_neighbors(central_hex)
        for troop_info in self.troops_available:
            troop_type, troop_count = troop_info
            # Choix de l'hexagone pour placer la troupe, aléatoirement sur la carte
            while i < 18:
                if (
                    not possibilities[entiers_aleatoires[i]].occupied
                    and possibilities[entiers_aleatoires[i]].accessible
                    and possibilities[entiers_aleatoires[i]]
                ):
                    possibilities[entiers_aleatoires[i]].occupied = True

                    if troop_type == "assassin":
                        new_troop = Assassin(possibilities[entiers_aleatoires[i]])

                    elif troop_type == "magician":
                        new_troop = Magician(possibilities[entiers_aleatoires[i]])

                    elif troop_type == "turret":
                        new_troop = Turret(possibilities[entiers_aleatoires[i]])

                    self.add_troop(new_troop)
                    print(f"{troop_type} placed")
                    break
                i += 1


# DEFENSEUR BOT
class DefenderBot(Bot):
    def __init__(self):
        super().__init__("DefenderBot", "Defender")
        self.troops_available = [
            ["archer", 2, None, False],
            ["shield", 1, None, False],
            ["engineer", 1, None, False],
        ]
        self.defended_hexagon = None
        self.position = (0, 0)
        self.selected_troop_index = None

    # implémentation de la logique du bot défenseur, en utilisant la génération de clicks...
    def make_move_bot(self, game, screen):
        # logique pour le défenseur bot
        player = game.attacker
        for selected_troop in self.troops:
            print(self.distance_with_opponants(game, selected_troop, player))
            self.use_selected_troop(selected_troop, game, player)
            game.screen_update_bot(screen)
            pygame.time.delay(1500)

    # si une troupe est sélectionnée, l'utiliser
    def use_selected_troop(self, selected_troop, game, player):
        print(self.find_attackable_troop(game, selected_troop, player))
        target_troop = self.find_attackable_troop(game, selected_troop, player)[0]
        d_target = self.find_attackable_troop(game, selected_troop, player)[1]
        # vérifier si la troupe a une capacité d'attaque non nulle
        if selected_troop.attack_capacity > 0:
            # vérifier si la troupe peut attaquer une troupe ennemie
            if d_target <= selected_troop.attack_range:
                # attaquer une troupe ennemie si il y en a une à portée
                selected_troop.move(target_troop.hex, game)
                pygame.time.delay(500)

            else:
                # trouver la troupe ennemie la plus proche et se déplacer vers elle si il reste de la vitesse
                if selected_troop.speed != 0:
                    # flake8: noqa
                    if d_target <= selected_troop.attack_range + selected_troop.speed:
                        # sé déplacer et attaquer si la troupe est à porté suffisante après le déplacement considérant la vitesse restante
                        while (
                            selected_troop.speed > 0
                            and selected_troop.speed + selected_troop.attack_range
                            > d_target
                        ):
                            destination_hex = game.board.find_destination_hex(
                                selected_troop.hex, target_troop.hex
                            )
                            selected_troop.move(destination_hex, game)
                            pygame.time.delay(500)
                            print("troupe déplacée : " + str(selected_troop))
                            pygame.time.delay(500)
                    else:
                        # se rapprocher de la troupe ennemie et s'arreter là
                        destination_hex = game.board.find_destination_hex(
                            selected_troop.hex, target_troop.hex
                        )
                        selected_troop.move(destination_hex, game)
                        pygame.time.delay(500)
                        print("troupe déplacée : " + str(selected_troop))
                        pygame.time.delay(500)
        else:
            # La troupe n'a pas de capacité d'attaque, ne rien faire
            pass

    def step_back(self, troop, board):
        pass

    def initialize_bot(self, game, screen):
        # select a random hexagon to defend
        i = random.randint(0, len(game.board.list))
        self.defended_hexagon = game.board.list[i]
        game.board.list[i].toDefended()
        pygame.time.delay(1000)
        print("hexagon defended chosen")
        game.screen_update_bot(screen)

        # choisit la stratégie de placer par défaut un archer sur l'hexagone à défendre
        archer = Archer(game.board.list[i])
        self.troops_available[0][1] -= 1
        self.add_troop(archer)
        pygame.time.delay(1000)
        game.screen_update_bot(screen)

        defense = game.board.larger_list_neighbors(self.defended_hexagon)
        print(defense)

        for troop in self.troops_available:
            if troop[1] != 0:
                troop[3] = True
                j = 0
                while troop[1] != 0 and j < len(defense):
                    if not defense[j].occupied and defense[j].accessible:
                        if troop[0] == "shield":
                            troop1 = Shield(defense[j])

                        elif troop[0] == "engineer":
                            troop1 = Engineer(defense[j])

                        elif troop[0] == "archer":
                            troop1 = Archer(defense[j])
                        self.add_troop(troop1)
                        pygame.time.delay(1000)
                        game.screen_update_bot(screen)
                        print(str(troop[0]) + " place")
                        pygame.time.delay(1000)
                        game.board.larger_list_neighbors(self.defended_hexagon)[
                            j
                        ].occupied = True
                        troop[1] -= 1
                    j += 1
                troop[3] = False
