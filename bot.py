from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import random
from players import Player


class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
        # bot_logic se réfère au type attaquant ou défenseur pour faire appel au fonctions
        # en fonction d'une logique d'attaque ou de défense
        self.bot_logic = AttackerBot() if player_type == "Attacker" else DefenderBot()

    def make_move(self, game):
        self.bot_logic.make_move(game)

    def end_ini(self):
        return self.bot_logic.end_ini()

    def initialize_troops(self, clicked, i, game):
        self.bot_logic.initialize_troops(clicked, i, game)

    def draw_button(self, screen, height, width, col):
        self.bot_logic.draw_button(screen, height, width, col)

    def selected_button(self, clicked, i):
        return self.bot_logic.selected_button(clicked, i)


class AttackerBot(Bot):
    def __init__(self):
        super().__init__("AttackerBot", "Attacker")

    def make_move(self, game):
        # Logique pour l'attaquant bot
        if not self.selected_troop_index:
            movable_troops = [index for index, troop in enumerate(game.attacker.troops) if troop.can_move()]
            if movable_troops:
                self.selected_troop_index = random.choice(movable_troops)
        else:
            target_hexagon = random.choice(game.board.list)
            game.attacker.move_troop(self.selected_troop_index, target_hexagon)

    def initialize_troops(self, game):
        # placing the troops randomly with a distance defined from the defended hexagon
        # define a method in hexagon.py to get the neighbors of a hexagon with a given distance
        i = 3
        for troop in game.defender.troops:
            # choice of the hexagon to place the troop, now randomly on the map
            for hexagon in game.board.list:
                if not hexagon.occupied and hexagon.accessible:
                    hexagon.occupied = True
                    if self.troops_available[i][0] == "assassin":
                        troop = Assassin(hexagon)

                    elif self.troops_available[i][0] == "magician":
                        troop = Magician(hexagon)

                    elif self.troops_available[i][0] == "turret":
                        troop = Turret(hexagon)

                    elif self.troops_available[i][0] == "archer":
                        troop = Archer(hexagon)

                    elif self.troops_available[i][0] == "engineer":
                        troop = Engineer(hexagon)

                    elif self.troops_available[i][0] == "shield":
                        troop = Shield(hexagon)

                self.add_troop(troop)
                print("troop placed")
                self.troops_available[i][1] -= 1
                print(self.troops_available[i][1])
                if self.troops_available[i][1] == 0:
                    self.button_selected = False

                elif hexagon.occupied:
                    print("this hexagon is already occupied")
                else:
                    print("this hexagon is not accessible")

    # Les autres méthodes spécifiques à l'attaquant peuvent être ajoutées ici


class DefenderBot(Bot):
    def __init__(self):
        super().__init__("DefenderBot", "Defender")

    def make_move(self, game):
        # Logique pour le défenseur bot
        if not self.selected_troop_index:
            attackable_troops = [index for index, troop in enumerate(game.defender.troops) if troop.can_attack()]
            if attackable_troops:
                self.selected_troop_index = random.choice(attackable_troops)
        else:
            target_troop = random.choice(game.attacker.troops)
            game.defender.attack_enemy(self.selected_troop_index, target_troop)

    def initialize_troops(self, game):
        # choice of the hexagon to defend, now randomly on the map
        i = random.randint(0, len(game.board.list))
        defended_hexagon = game.board.list[i]
        defended_hexagon.occupied = True
        # defended_hexagon.defended = True not defined yet in hexagon.py

        # placing the troops around the defended hexagon
        # define a method in hexagon.py to get the neighbors of a hexagon with a given distance
        for troop in game.defender.troops:
            # choice of the hexagon to place the troop, now randomly on the map
            for hexagon in game.board.list:
                if not hexagon.occupied and hexagon.accessible:
                    hexagon.occupied = True
                    if self.troops_available[i][0] == "assassin":
                        troop = Assassin(hexagon)

                    elif self.troops_available[i][0] == "magician":
                        troop = Magician(hexagon)

                    elif self.troops_available[i][0] == "turret":
                        troop = Turret(hexagon)

                    elif self.troops_available[i][0] == "archer":
                        troop = Archer(hexagon)

                    elif self.troops_available[i][0] == "engineer":
                        troop = Engineer(hexagon)

                    elif self.troops_available[i][0] == "shield":
                        troop = Shield(hexagon)

                self.add_troop(troop)
                print("troop placed")
                self.troops_available[i][1] -= 1
                print(self.troops_available[i][1])
                if self.troops_available[i][1] == 0:
                    self.button_selected = False

                elif hexagon.occupied:
                    print("this hexagon is already occupied")
                else:
                    print("this hexagon is not accessible")

    # Les autres méthodes spécifiques au défenseur peuvent être ajoutées ici