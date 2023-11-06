import pygame


class Troupe:
    def __init__(self, troop_type, x, y):
        self.troop_type = troop_type
        self.x = x
        self.y = y
        self.health = 100
        self.attack_power = 10
        self.status = "none"

    def move(self, destination_x, destination_y):
        delta_x = destination_x - self.x
        delta_y = destination_y - self.y
        distance = ((delta_x ** 2) + (delta_y ** 2)) ** 0.5
        speed = 2

        if distance > 0:
            move_x = (delta_x / distance) * speed
            move_y = (delta_y / distance) * speed
            self.x += move_x
            self.y += move_y

            if abs(self.x - destination_x) < move_x and abs(self.y - destination_y) < move_y:
                self.x = destination_x
                self.y = destination_y

    def attack(self, target):
        if isinstance(target, Troupe):
            damage = self.attack_power
            target.health -= damage

            if target.health <= 0:
                target.status = "dead"

    def draw(self, screen):
        color_mapping = {
            "assassin": (255, 0, 0),
            "magician": (0, 0, 255),
            "turret": (0, 255, 0)
        }

        troop_center_x = self.x
        troop_center_y = self.y
        troop_radius = 20

        pygame.draw.circle(screen, color_mapping[self.troop_type], (troop_center_x, troop_center_y), troop_radius)
