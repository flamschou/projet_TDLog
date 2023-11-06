import pygame
import hexagone_1 as hex


class Troupe:
    def __init__(self, troop_type, hexagone):
        self.troop_type = troop_type
        self.hexagone = hexagone
        self.health = 0
        self.attack_power = 0
        self.status = "none"
        self.speed = 0
        self.color = (0, 0, 0)

    def move(self, destination_h):
        speed = self.speed

        if  self.hexagone.voisin(destination_h) & speed >0:
            self.hexagone = destination_h
            speed -= 1

    def attack(self, target):
        if isinstance(target, Troupe):
            damage = self.attack_power
            target.health -= damage

            if target.health <= 0:
                target.status = "dead"

    def draw(self, screen):
        troop_center_x = self.x
        troop_center_y = self.y
        troop_radius = 20

        pygame.draw.circle(screen, self.color, (troop_center_x, troop_center_y), troop_radius)


class Assassin(Troupe):
    def __init__(self, x, y):
        super().__init__("assassin", x, y)
        self.color = (255, 0, 0)
        self.health = 100
        self.attack_power = 20
        self.speed = 5


class Magician(Troupe):
    def __init__(self, x, y):
        super().__init__("magician", x, y)
        self.health = 200
        self.attack_power = 50
        self.speed = 3
        self.color = (0, 0, 255)


class Turret(Troupe):
    def __init__(self, x, y):
        super().__init__("turret", x, y)
        self.health = 500
        self.attack_power = 100
        self.speed = 1
        self.color = (0, 255, 0)