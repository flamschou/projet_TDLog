import pygame


class Troop:
    def __init__(self, troop_type, hex):
        self.troop_type = troop_type
        self.hex = hex
        self.health = 0
        self.attack_power = 0
        self.status = "none"
        self.speed = 0
        self.color = (0, 0, 0)

    def move(self, destination_h, adrenaline):
        if destination_h.troupe is None:
            speed = self.speed*adrenaline

            if self.hexagone.voisin(destination_h):

                if speed > 0 & self.hex.hex_type != "swamp":
                    self.hex = destination_h
                    speed -= 1

                if speed > 1 & self.hex.hex_type == "swamp":
                    speed -= 2

    def attack(self, target, adrenaline):
        if isinstance(target, Troop):
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


class Magician(Troop):
    def __init__(self, hex):
        super().__init__("magician", hex)
        self.health = 200
        self.attack_power = 50
        self.speed = 3
        self.color = (0, 0, 255)


class Turret(Troop):
    def __init__(self, hex):
        super().__init__("turret", hex)
        self.health = 500
        self.attack_power = 100
        self.speed = 1
        self.color = (0, 255, 0)
