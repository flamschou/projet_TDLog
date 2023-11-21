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
                        troop.move(hexagon, game)
                        troop.selected = False

    def make_attack(self, clicked, game):
        clicked_pos = clicked
        print("clicked at", clicked_pos)
        attacker = None
        defender = None

        for troop in self.troops:
            if troop.selected:
                attacker = troop

            if troop.rect.collidepoint(clicked_pos) and not troop.selected:
                defender = troop

        if attacker is not None and defender is not None:
            attacker.attack(defender, game.adrenalin)
        else:
            print("No attacker or defender selected.")

    def initialize_troops(self, clicked, game, troop):
        # beginning of the game, the attacker starts by placing his troops

        clicked_pos = clicked
        print("clicked at", clicked_pos)

        for hexagon in game.board.list:
            if hexagon.rect.collidepoint(clicked_pos):
                if not hexagon.occupied and hexagon.accessible:
                    hexagon.occupied = True
                    troop.hex = hexagon
                    self.troops.append(troop)
                    print("troop placed")
                elif hexagon.occupied:
                    print("this hexagon is already occupied")
                else:
                    print("this hexagon is not accessible")


class Attacker(Player):
    def __init__(self):
        super().__init__("Attacker")
        # for i in range(4):
        # creates the four dices of the attacker
        # self.dices.append(Dice("archeer", "engineer", "shield", "stepback", "missed")) later..


class Defender(Player):
    def __init__(self):
        super().__init__("Defender")
        for i in range(4):
            # creates the four dices of the attacker
            self.dices.append(
                Dice("magician", "assassin", "turret", "stepback", "missed")
            )

    def make_move(self):
        # Implement defender's move logic
        pass  # Placeholder, implement your logic
