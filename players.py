from dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.troops = []
        self.dices = []

    def make_move(self, clicked, game):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        for troop in self.troops:
            if troop.rect.collidepoint(clicked_pos):
                troop.selected = True
                print("troop selected")

        for hexagon in game.board.list:
            if hexagon.rect.collidepoint(clicked_pos) and any(troop.selected for troop in self.troops):
                for troop in self.troops:
                    if troop.selected and troop.hex != hexagon:
                        troop.move(hexagon, game)
                        troop.selected = False


class Attacker(Player):
    def __init__(self):
        super().__init__("Attacker")
        for i in range(4):
            # creates the four dices of the attacker
            self.dices.append(Dice("archeer", "engineer", "shield", "stepback", "missed"))


class Defender(Player):
    def __init__(self):
        super().__init__("Defender")
        for i in range(4):
            # creates the four dices of the attacker
            self.dices.append(Dice("magician", "assassin", "turret", "stepback", "missed"))
