import pygame


class Troop:
    def __init__(self, troop_type, hex):
        self.troop_type = troop_type
        self.hex = hex
        self.health = 0
        self.attack_capacity = 0
        self.attack_power = 0
        self.status = "none"
        self.default_speed = 0
        self.speed = 0
        self.color = (0, 0, 0)
        self.attack_range = 0
        self.rect = pygame.Rect(self.hex.x - 10, self.hex.y - 10, 20, 20)
        self.selected = False

    def move(self, destination_h, game):
        if not destination_h.occupied:
            self.speed = self.speed * game.adrenalin

            if game.board.neighbors(self.hex, destination_h) and destination_h.accessible:

                if self.speed == 0:
                    print("no speed left ; you can't move anymore")

                else:
                    print("moving")

                    if self.speed > 0 and self.hex.hex_type != "swamp":
                        self.hex.occupied = False
                        self.hex = destination_h
                        self.hex.occupied = True
                        self.speed -= 1
                        print("moved to " + str(destination_h.index) + " hexagon")
                        print("speed left: " + str(self.speed))

                    if self.speed > 1 and self.hex.hex_type == "swamp":
                        self.hex.occupied = False
                        self.hex = destination_h
                        self.hex.occupied = True
                        self.speed -= 2
            self.rect = pygame.Rect(self.hex.x - 10, self.hex.y - 10, 20, 20)
        else:
            for current_player in [game.attacker, game.defender]:
                for troop in current_player.troops:
                    if troop.hex == destination_h:
                        if self.is_troop_allowed_to_strike(troop, game):
                            self.attack(troop, game.adrenalin)

    def test_move(self, destination_h, adrenaline):
        self.move(self, destination_h, adrenaline)
        assert self.hex == destination_h

    def attack(self, target, adrenaline):
        damage = self.attack_power * adrenaline
        target.health -= damage
        print("attacked " + target.troop_type + " for " + str(damage) + " damage")
        self.attack_capacity -= 1

        if target.health <= 0:
            target.status = "dead"
            print(target.troop_type + " is dead")

    def is_troop_allowed_to_strike(self, target, game):
        if self.attack_capacity == 0:
            print(self.troop_type + " has no attack power")
            return False
        else:
            if game.board.isdistance(self.hex, target.hex, self.attack_range):
                return True
            else:
                print(self.troop_type + " has not enough attack range")
                return False

    def draw(self, screen):
        troop_center_x = self.hex.x
        troop_center_y = self.hex.y
        image_rect = self.image.get_rect(center=(troop_center_x, troop_center_y))
        if self.selected:
            screen.blit(self.imageSelected, image_rect)
        screen.blit(self.image, image_rect)

    def info(self, screen):
        font = pygame.font.Font(None, 25)
        text = "Health = "+str(self.health)
        health_text = font.render(text, True, (0, 0, 0))
        text_rect = health_text.get_rect(center=(90, 30))
        screen.blit(health_text, text_rect)

    def isHovered(self, mousePos):
        return self.rect.collidepoint(mousePos)


class Assassin(Troop):
    def __init__(self, hex):
        super().__init__("assassin", hex)
        self.color = (255, 0, 0)
        self.health = 100
        self.attack_power = 20
        self.attack_capacity = 1
        self.speed = 5
        self.default_speed = self.speed
        self.attack_range = 1
        self.player = "attacker"
        self.image = pygame.image.load("Images\\assassin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\assassinSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))


class Magician(Troop):
    def __init__(self, hex):
        super().__init__("magician", hex)
        self.health = 200
        self.attack_power = 50
        self.attack_capacity = 1
        self.speed = 3
        self.default_speed = self.speed
        self.color = (255, 0, 0)
        self.attack_range = 2
        self.player = "attacker"
        self.image = pygame.image.load("Images\\magician.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\magicianSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))


class Turret(Troop):
    def __init__(self, hex):
        super().__init__("turret", hex)
        self.health = 500
        self.attack_power = 100
        self.attack_capacity = 1
        self.speed = 1
        self.default_speed = self.speed
        self.color = (255, 0, 0)
        self.attack_range = 3
        self.player = "attacker"
        self.image = pygame.image.load("Images\\turret.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\turretSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))


class Archer(Troop):
    def __init__(self, hex):
        super().__init__("archer", hex)
        self.health = 100
        self.attack_power = 20
        self.attack_capacity = 1
        self.speed = 5
        self.default_speed = self.speed
        self.color = (0, 255, 0)
        self.attack_range = 2
        self.player = "defender"
        self.image = pygame.image.load("Images\\archer.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\archerSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))


class Engineer(Troop):
    def __init__(self, hex):
        super().__init__("engineer", hex)
        self.health = 200
        self.attack_power = 50
        self.attack_capacity = 1
        self.speed = 3
        self.default_speed = self.speed
        self.color = (0, 255, 0)
        self.attack_range = 1
        self.player = "defender"
        self.image = pygame.image.load("Images\\engineer.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\engineerSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))


class Shield(Troop):
    def __init__(self, hex):
        super().__init__("shield", hex)
        self.health = 500
        self.attack_power = 100
        self.attack_capacity = 1
        self.speed = 1
        self.default_speed = self.speed
        self.color = (0, 255, 0)
        self.attack_range = 1
        self.player = "defender"
        self.image = pygame.image.load("Images\\shield.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.imageSelected = pygame.image.load("Images\\shieldSelected.png")
        self.imageSelected = pygame.transform.scale(self.imageSelected, (30, 30))
