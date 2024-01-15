# this file defines the class Player and its subclasses Attacker and Defender
# the class player contains important methods such as the initialization of the troops and the movements of the troops

from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import utils
import scale
import pygame

S = scale.scale


class Player:
    def __init__(self, name):
        self.name = name
        self.troops = []
        self.dices = []
        self.troops_available = []
        self.button_selected = False
        self.playing = False

    # adds a troop to the list of troops
    def add_troop(self, troop):
        self.troops.append(troop)

    # select a troop by clicking on it
    def selection_troop(self, clicked):
        clicked_pos = clicked
        for troop in self.troops:
            for troop in self.troops:
                if troop.speed == 0:
                    troop.selected = False
                    print("no speed left ; you can't move anymore")

                elif troop.rect.collidepoint(clicked_pos):
                    troop.selected = True
                    text = troop.troop_type + " selected"
                    print(text)

    # the troop selected makes an action to the hexagon clicked
    def action_troop(self, clicked, game):
        clicked_pos = clicked

        for hexagon in game.board.list:
            if hexagon.rect.collidepoint(clicked_pos) and any(
                troop.selected for troop in self.troops
            ):
                for troop in self.troops:
                    if troop.selected and troop.hex != hexagon and hexagon.accessible:
                        troop.action(hexagon, game)
                        troop.selected = False

    # make a move by using the two previous methods
    def make_move(self, clicked, game):
        self.selection_troop(clicked)
        self.action_troop(clicked, game)

    # this method defines the button selected during the initialization phase
    def selected_button(self, clicked):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        for troop in self.troops_available:
            if troop[2].collidepoint(clicked_pos) and troop[1] > 0:
                self.button_selected = True
                troop[3] = True
                print("button selected")

    # this method initializes the troops during the initialization phase
    # it is a bit messy, but it works
    def initialize_troops(self, clicked, game):
        # beginning of the game, the defender starts by placing his troops

        clicked_pos = clicked

        self.selected_button(clicked_pos)

        print("clicked at", clicked_pos)

        if self.name == "Defender" and not self.placed:
            for hexagon in game.board.list:
                if hexagon.rect.collidepoint(clicked_pos):
                    if not hexagon.occupied:
                        hexagon.toDefended()
                        print("hexagon defended")
                        self.placed = True
        for troops in self.troops_available:
            if troops[3]:
                print("troop selected")
        else:
            for hexagon in game.board.list:
                if hexagon.rect.collidepoint(clicked_pos) and self.button_selected:
                    for troop in self.troops_available:
                        if not hexagon.occupied and hexagon.accessible and troop[3]:
                            if troop[0] == "assassin":
                                troop1 = Assassin(hexagon)

                            elif troop[0] == "magician":
                                troop1 = Magician(hexagon)

                            elif troop[0] == "turret":
                                troop1 = Turret(hexagon)

                            elif troop[0] == "archer":
                                troop1 = Archer(hexagon)

                            elif troop[0] == "engineer":
                                troop1 = Engineer(hexagon)

                            elif troop[0] == "shield":
                                troop1 = Shield(hexagon)

                            self.add_troop(troop1)
                            print("troop placed")
                            troop[1] -= 1
                            print(troop[1])
                            if troop[1] == 0:
                                self.button_selected = False
                                troop[3] = False

    # this method displays the buttons of selection of the troops during the initialization phase
    def draw_button(self, screen, height, width, col):
        pos_y = height - 150  # Position verticale initiale des boutons
        i = 0
        for troop in self.troops_available:
            utils.drawButton_troop(
                troop[0], screen, troop[1], width, pos_y, col, self.troops_available[i]
            )
            i += 1

            pos_y -= 30 * S  # Ajustement vertical pour chaque bouton

    # this method ends the initialization phase
    def end_ini(self):
        S = 0
        for troop in self.troops_available:
            S += troop[1]

        if S == 0:
            return False
        else:
            return True

    # this method regenate the speed of the troops after the end of the turn
    def regenerate_speed(self):
        for troop in self.troops:
            troop.speed = troop.default_speed
            troop.attack_power = troop.default_attack_power
            troop.attack_capacity = troop.default_attack_capacity

    # this method initializes the parameter of the troops available during the initialization phase
    def ini_troops_available(self, width, height):
        pos_y = height - 150  # Position verticale initiale des boutons
        button_size = (100 * S, 20 * S)

        for troop in self.troops_available:
            button_pos = (width - 150 * S, pos_y)
            troop[2] = pygame.Rect(button_pos, button_size)

            pos_y -= 30 * S  # Ajustement vertical pour chaque bouton


class Attacker(Player):
    def __init__(self):
        super().__init__("Attacker")
        self.troops_available = [
            ["assassin", 2, None, False],
            ["magician", 1, None, False],
            ["turret", 1, None, False],
        ]
        # for i in range(4):
        # creates the four dices of the attacker
        # self.dices.append(Dice("archeer", "engineer", "shield", "stepback", "missed")) later..


class Defender(Player):
    def __init__(self):
        super().__init__("Defender")
        self.placed = False
        self.troops_available = [
            ["archer", 2, None, False],
            ["engineer", 1, None, False],
            ["shield", 1, None, False],
        ]
        # for i in range(4):
        #   creates the four dices of the attacker
        #   self.dices.append(
        #       Dice("magician", "assassin", "turret", "stepback", "missed")
        #   )
