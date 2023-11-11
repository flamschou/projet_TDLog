import pygame
import board


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

    def move(self, destination_h, adrenaline):
        if destination_h.troupe is None:
            speed = self.speed*adrenaline

            if board.neighbors(self.hex, destination_h):

                if speed > 0 & self.hex.hex_type != "swamp":
                    self.hex = destination_h
                    speed -= 1

                if speed > 1 & self.hex.hex_type == "swamp":
                    speed -= 2

    def attack(self, target, adrenaline):
        if isinstance(target, Troop) & board.isdistance(self.hex, target.hex, self.attack_range):
            damage = self.attack_power*adrenaline
            target.health -= damage

            if target.health <= 0:
                target.status = "dead"

    def draw(self, screen):
        troop_center_x = self.x
        troop_center_y = self.y
        troop_radius = 20

        pygame.draw.circle(screen, self.color, (troop_center_x, troop_center_y), troop_radius)


class Assassin(Troop):
    def __init__(self, x, y):
        super().__init__("assassin", x, y)
        self.color = (255, 0, 0)
        self.health = 100
        self.attack_power = 20
        self.speed = 5
        self.attack_range = 1


class Magician(Troop):
    def __init__(self, x, y):
        super().__init__("magician", x, y)
        self.health = 200
        self.attack_power = 50
        self.speed = 3
        self.color = (0, 0, 255)
        self.attack_range = 2


class Turret(Troop):
    def __init__(self, x, y):
        super().__init__("turret", x, y)
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
