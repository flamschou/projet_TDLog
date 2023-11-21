from dice import Dice
from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import utils


class Player:
    def __init__(self, name):
        self.name = name
        self.troops = []
        self.dices = []
        self.troops_available = []
        self.button_selected = False

    def add_troop(self, troop):
        self.troops.append(troop)

    def make_move(self, clicked, game):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        for troop in self.troops:
            if troop.speed == 0:
                troop.selected = False
                print("no speed left ; you can't move anymore")

            elif troop.rect.collidepoint(clicked_pos):
                troop.selected = True
                print("troop selected")

        for hexagon in game.board.list:
            if hexagon.rect.collidepoint(clicked_pos) and any(
                troop.selected for troop in self.troops
            ):
                for troop in self.troops:
                    if troop.selected and troop.hex != hexagon and hexagon.accessible:
                        troop.hex.occupied = False
                        troop.move(hexagon, game)
                        hexagon.occupied = True
                        troop.selected = False

    def selected_button(self, clicked, i):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        for j in range(len(self.troops_available)):
            if self.troops_available[j][2].collidepoint(clicked_pos) and self.troops_available[j][1] > 0:
                self.button_selected = True
                return (j)

        return (i)

    def initialize_troops(self, clicked, i, game):
        clicked_pos = clicked
        print("clicked at", clicked_pos)

        for hexagon in game.board.list:
            if hexagon.rect.collidepoint(clicked_pos) and self.button_selected:
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

    def draw_button(self, screen, height, width, col):
        pos_y = height - 150  # Position verticale initiale des boutons
        i = 0
        for troop in self.troops_available:
            utils.drawButton_troop(troop[0], screen, troop[1], width, pos_y, col, self.troops_available[i])
            i += 1

            pos_y -= 30  # Ajustement vertical pour chaque bouton

    def end_ini(self):
        S = 0
        for troop in self.troops_available:
            S += troop[1]

        if S == 0:
            return False
        else:
            return True

    def regenerate_speed(self):
        for troop in self.troops:
            troop.speed = troop.default_speed


class Attacker(Player):
    def __init__(self):
        super().__init__("Attacker")
        self.troops_available = [["assassin", 2], ["magician", 1], ["turret", 1]]
        # for i in range(4):
        # creates the four dices of the attacker
        # self.dices.append(Dice("archeer", "engineer", "shield", "stepback", "missed")) later..


class Defender(Player):
    def __init__(self):
        super().__init__("Defender")
        self.troops_available = [["archer", 2], ["engineer", 1], ["shield", 1]]
        for i in range(4):
            # creates the four dices of the attacker
            self.dices.append(
                Dice("magician", "assassin", "turret", "stepback", "missed")
            )
