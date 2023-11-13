import pygame
import board
#  import pytest


class Troop:
    def __init__(self, troop_type, hex):
        self.troop_type = troop_type
        self.hex = hex
        self.health = 0
        self.attack_power = 0
        self.status = "none"
        self.speed = 0
        self.color = (0, 0, 0)
        self.attack_range = 0
        self.rect = pygame.Rect(self.hex.x-10, self.hex.y-10, 20, 20)
        self.selected = False

    def move(self, destination_h, game):
        if not destination_h.occupied:
            self.speed = self.speed*game.adrenalin
            if game.board.neighbors(self.hex, destination_h):

                print("moving")

                if self.speed > 0 and self.hex.hex_type != "swamp":
                    self.hex = destination_h
                    self.speed -= 1
                    print("moved to "+str(destination_h.index)+" hexagon")
                    print("speed left: "+str(self.speed))

                if self.speed > 1 and self.hex.hex_type == "swamp":
                    self.speed -= 2

        self.rect = pygame.Rect(self.hex.x-10, self.hex.y-10, 20, 20)

    def test_move(self, destination_h, adrenaline):
        self.move(self, destination_h, adrenaline)
        assert self.hex == destination_h

    def attack(self, target, adrenaline):
        if isinstance(target, Troop) and board.isdistance(self.hex, target.hex, self.attack_range):
            damage = self.attack_power*adrenaline
            target.health -= damage

            if target.health <= 0:
                target.status = "dead"

    def draw(self, screen):
        troop_center_x = self.hex.x
        troop_center_y = self.hex.y
        troop_radius = 15
        pygame.draw.circle(screen, self.color, (troop_center_x, troop_center_y), troop_radius)


class Assassin(Troop):
    def __init__(self, hex):
        super().__init__("assassin", hex)
        self.color = (255, 0, 0)
        self.health = 100
        self.attack_power = 20
        self.speed = 5
        self.attack_range = 1


class Magician(Troop):
    def __init__(self, hex):
        super().__init__("magician", hex)
        self.health = 200
        self.attack_power = 50
        self.speed = 3
        self.color = (0, 0, 255)
        self.attack_range = 2


class Turret(Troop):
    def __init__(self, hex):
        super().__init__("turret", hex)
        self.health = 500
        self.attack_power = 100
        self.speed = 1
        self.color = (0, 255, 0)
        self.attack_range = 3


class Archer(Troop):
    def __init__(self, x, y):
        super().__init__("archer", x, y)
        self.health = 100
        self.attack_power = 20
        self.speed = 5
        self.color = (255, 255, 0)
        self.attack_range = 2


class Engineer(Troop):
    def __init__(self, x, y):
        super().__init__("engineer", x, y)
        self.health = 200
        self.attack_power = 50
        self.speed = 3
        self.color = (0, 255, 255)
        self.attack_range = 1


class Shield(Troop):
    def __init__(self, x, y):
        super().__init__("shield", x, y)
        self.health = 500
        self.attack_power = 100
        self.speed = 1
        self.color = (255, 0, 255)
        self.attack_range = 1
