from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import random
from players import Player


'''class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
        # bot_logic se réfère au type attaquant ou défenseur pour faire appel au fonctions
        # en fonction d'une logique d'attaque ou de défense
        self.bot_logic = AttackerBot() if player_type == "Attacker" else DefenderBot()

    def make_move(self, game):
        self.bot_logic.make_move(game)

    def end_ini(self):
        S = 0
        for troop in self.bot_logictroops_available:
            S += troop[1]

        if S == 0:
            return False
        else:
            return True

    def initialize_troops(self, clicked, i, game):
        self.bot_logic.initialize_troops(clicked, i, game)

    def draw_button(self, screen, height, width, col):
        self.bot_logic.draw_button(screen, height, width, col)

    def selected_button(self, clicked, i):
        return self.bot_logic.selected_button(clicked, i)
'''

class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
        self.bot_logic = None

    def set_bot_logic(self, bot_logic):
        self.bot_logic = bot_logic

    def selected_button(self, clicked_pos):
        for index, troop in enumerate(self.troops_available):
            if troop.button.collidepoint(clicked_pos):
                self.button_selected = True
                print("button selected")
                return index

        return None


class AttackerBot(Bot):
    def __init__(self):
        super().__init__("AttackerBot", "Attacker")
        self.troops_available = [["assassin", 2], ["magician", 1], ["turret", 1]]

    def initialize_bot_logic(self):
        self.set_bot_logic(self)

    def make_move(self, game):
        # Logique pour l'attaquant bot
        """if not self.selected_troop_index:
            movable_troops = [index for index, troop in enumerate(game.attacker.troops) if troop.can_move()]
            if movable_troops:
                self.selected_troop_index = random.choice(movable_troops)
        else:
            target_hexagon = random.choice(game.board.list)
            game.attacker.move_troop(self.selected_troop_index, target_hexagon)"""
        pass

    def initialize_troops(self, game):
        # placing the troops a bit far from the defended hexagon
        entiers = list(range(0, 79))
        entiers_aleatoires = random.shuffle(entiers)
        for troop in game.attacker.troops_available:
            # choice of the hexagon to place the troop, now randomly on the map
            d = 0
            j = 0
            while d == 0:
                # flake8: noqa
                if (
                    not game.board.list[entiers_aleatoires[i]].occupied
                    and game.board.list[entiers_aleatoires[i]].accessible
                    and game.board.list[entiers_aleatoires[i]]
                    not in game.defender.defended_hexagon.larger_neighbors
                ):
                    game.board.list[entiers_aleatoires[i]].occupied = True

                    i += 1
                    d += 1

                    if self.troops_available[j][0] == "assassin":
                        troop = Assassin(self.defended_hexagon)

                    elif self.troops_available[j][0] == "turret":
                        troop = Turret(self.defended_hexagon)

                    elif self.troops_available[j][0] == "magician":
                        troop = Magician(self.defended_hexagon)

                    self.add_troop(troop)
                    print("troop placed")
                    self.troops_available[j][1] -= 1
                    j += 1

                else:
                    i += 1

    # Les autres méthodes spécifiques à l'attaquant peuvent être ajoutées ici


class DefenderBot(Bot):
    def __init__(self):
        super().__init__("DefenderBot", "Defender")
        self.troops_available = [["archer", 1], ["archer", 1], ["shield", 1], ["engineer", 1]]
        self.defended_hexagon = None

    def initialize_bot_logic(self):
        self.set_bot_logic(self)

    def make_move(self, game):
        # Logique pour le défenseur bot
        """if not self.selected_troop_index:
            attackable_troops = [index for index, troop in enumerate(game.defender.troops) if troop.can_attack()]
            if attackable_troops:
                self.selected_troop_index = random.choice(attackable_troops)
        else:
            target_troop = random.choice(game.attacker.troops)
            game.defender.attack_enemy(self.selected_troop_index, target_troop)"""
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
        d = 0
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
                        new_troop = Archer(game.board.larger_list_neighbors(self.defended_hexagon)[entiers_aleatoires[i]])

                    elif troop_type == "engineer":
                        new_troop = Engineer(game.board.larger_list_neighbors(self.defended_hexagon)[entiers_aleatoires[i]])

                    elif troop_type == "shield":
                        new_troop = Shield(game.board.larger_list_neighbors(self.defended_hexagon)[entiers_aleatoires[i]])

                    self.add_troop(new_troop)
                    print(f"{troop_type} placed")
                    break
                i += 1
        """for troop_type, troop_count in self.troops_available:
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
                        new_troop = Archer(self.defended_hexagon)

                    elif troop_type == "engineer":
                        new_troop = Engineer(self.defended_hexagon)

                    elif troop_type == "shield":
                        new_troop = Shield(self.defended_hexagon)

                    self.add_troop(new_troop)
                    print(f"{troop_type} placed")
                    break  # Sortez de la boucle une fois que la troupe a été placée
                else:
                    i += 1"""
        """for troop in game.defender.troops_available:
            # choice of the hexagon to place the troop, now randomly on the map
            d = 0
            j = 0
            while d == 0 and i < 18:
                # flake8: noqa
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

                    i += 1
                    d += 1

                    if self.troops_available[j][0] == "archer":
                        troop = Archer(self.defended_hexagon)

                    elif self.troops_available[j][0] == "engineer":
                        troop = Engineer(self.defended_hexagon)

                    elif self.troops_available[j][0] == "shield":
                        troop = Shield(self.defended_hexagon)

                    self.add_troop(troop)
                    print("troop placed")
                    self.troops_available[j][1] -= 1
                    j += 1

                else:
                    i += 1
"""
    # Les autres méthodes spécifiques au défenseur peuvent être ajoutées ici
