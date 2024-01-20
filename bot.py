from troop import Assassin, Magician, Turret, Engineer, Archer, Shield
import random
from players import Player
import pygame
import time
import scale

S = scale.scale
num_cols = 10

class Bot(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.bot_type = player_type
        self.position = (0, 0)

    def set_bot_logic(self, bot_logic):
        self.bot_logic = bot_logic

    def selected_button(self, clicked_pos):
        for index, troop in enumerate(self.troops_available):
            if troop.button.collidepoint(clicked_pos):
                self.button_selected = True
                print("button selected")
                return index

        return None

    def distance_with_opponants(self, game, troop, player):
        L = []
        I = []
        for opponent_troop in player.troops : 
            if opponent_troop.health > 0: 
                L.append(
                    [
                        opponent_troop,
                        game.board.distance_between_hexagons(troop.hex.index, opponent_troop.hex.index, num_cols),
                    ]
                )
                I.append(game.board.distance_between_hexagons(troop.hex.index, opponent_troop.hex.index, num_cols))
        return L, I
    
    def reachable_allies(self, game, troop):
        L = []
        for ally_troop in self.troops:
            if ally_troop.health > 0 and ally_troop != troop:
                if game.board.distance_between_hexagons(troop.hex.index, ally_troop.hex.index, num_cols) < troop.attack_range:
                    L.append(ally_troop)  
        return L
    
    def ally_to_heal(self, game, troop):
        L = self.reachable_allies(game, troop)
        I = []
        if L != []:
            for ally in L:
                n = ally.default_health - ally.health
                I.append(n)
            i = I.index(min(I))
            return L[i]
        else : 
            return None  

    def find_attackable_troop(self, game, troop, player):
        List, Index = self.distance_with_opponants(game, troop, player)
        i = Index.index(min(Index))
        return List[i]
    
    def heal(self, game, troop, screen):
        ally_to_heal = self.ally_to_heal(game, troop)
        if ally_to_heal != None:
            troop.action(ally_to_heal.hex, game)
            pygame.time.delay(500)
            game.screen_update_bot(screen)
            pygame.time.delay(500)
    
    # going towards the defended hexagon
    def go_towards_defended_hexagon(self, game, troop, screen):
        avant = troop.hex
        if  game.board.distance_between_hexagons(troop.hex.index, game.defended_hex.index, num_cols) > 1:
            while troop.speed > 0 and game.board.distance_between_hexagons(troop.hex.index, game.defended_hex.index, num_cols) > 1:
                hex = game.board.find_destination_hex(troop.hex, game.defended_hex)
                if hex != None:
                    troop.action(hex, game)
                if troop.hex == avant:
                    break
                avant = troop.hex
        else : 
            troop.action(game.defended_hex, game)
        game.screen_update_bot(screen)
        pygame.time.delay(500)
    


# ATTAQUANT BOT
# notons ici que on a privilégié le dévelopmment du défenseur, donc dabord tester le défenseur bot
class AttackerBot(Bot):
    def __init__(self):
        super().__init__("AttackerBot", "Attacker")
        self.troops_available = [
            ["assassin", 2, None, False],
            ["magician", 1, None, False],
            ["turret", 1, None, False],
        ]
        self.position = (0, 0)

    # implémentation de la logique du bot attaquant, en utilisant la génération de clicks...
    # implémentation de la logique du bot défenseur, en utilisant la génération de clicks...
    def make_move_bot(self, game, screen):
        # logique pour le défenseur bot
        player = game.defender
        for selected_troop in self.troops:
                if game.winner == None:
                    if selected_troop.health > 0:
                        selected_troop.selected = True
                        game.screen_update_bot(screen)
                        pygame.time.delay(500)
                        print(self.distance_with_opponants(game, selected_troop, player))
                        self.use_selected_troop(selected_troop, game, player, screen)
                        game.screen_update_bot(screen)
                        pygame.time.delay(1500)
                        selected_troop.selected = False
                    print("action terminée du bot !")
        game.change_player()
        game.current_player.regenerate_speed()
        if game.current_player.name == "Defender":
            game.display_Event(screen)

    # si une troupe est sélectionnée, l'utiliser
    def use_selected_troop(self, selected_troop, game, player, screen):

        # start with searching attackable troops
        print(self.find_attackable_troop(game, selected_troop, player))
        target_troop = self.find_attackable_troop(game, selected_troop, player)[0]
        d_target = self.find_attackable_troop(game, selected_troop, player)[1]
        print("target troop : " + str(target_troop))
        # test if the attacker is able to win directly
        if game.board.distance_between_hexagons(selected_troop.hex.index, game.defended_hex.index, num_cols) == 1 and game.defended_hex.occupied == False:
                selected_troop.action(game.defended_hex, game)
                pygame.time.delay(500)
                game.screen_update_bot(screen)
                pygame.time.delay(500)
                print("troupe déplacée : " + str(selected_troop))
                game.winner = game.attacker

        elif selected_troop.attack_capacity > 0:
            # vérifier si la troupe peut attaquer une troupe ennemie
            print ("attacke chosen")
            pygame.time.delay(50)
            if d_target <= selected_troop.attack_range:
                # attaquer une troupe ennemie si il y en a une à portée
                if selected_troop.is_troop_allowed_to_strike(target_troop, game):
                    selected_troop.action(target_troop.hex, game)
                    pygame.time.delay(500)

            else:
                # trouver la troupe ennemie la plus proche et se déplacer vers elle si il reste de la vitesse
                if selected_troop.speed != 0:
                    # flake8: noqa
                    if d_target <= selected_troop.attack_range + selected_troop.speed:
                        print
                        # sé déplacer et attaquer si la troupe est à porté suffisante après le déplacement considérant la vitesse restante
                        while (selected_troop.speed > 0 and selected_troop.attack_range < d_target):
                            destination_hex = game.board.find_destination_hex(
                                selected_troop.hex, target_troop.hex)
                            pygame.time.delay(50)
                            self.action_towards_defender(game, destination_hex, selected_troop, screen)
                            d_target -= 1
                        # attack after moving
                        if selected_troop.is_troop_allowed_to_strike(target_troop, game):
                            selected_troop.action(target_troop.hex, game)
                            pygame.time.delay(10)
                            

                        
                    else:
                        # tries to heal
                        self.heal(game, selected_troop, screen)
                        # se rapprocher de la troupe ennemie et s'arreter là
                        destination_hex = game.board.find_destination_hex(
                            selected_troop.hex, target_troop.hex
                        )
                        pygame.time.delay(50)
                        self.action_towards_defender(game, destination_hex, selected_troop, screen)
                        # tries to heal again
                        self.heal(game, selected_troop, screen)
                        self.go_towards_defended_hexagon(game, selected_troop, screen)
                        self.heal(game, selected_troop, screen)
            self.go_towards_defended_hexagon(game, selected_troop, screen)


        else:
            # no attack capacity, move towards the defend hexagon
            self.go_towards_defended_hexagon(game, selected_troop, screen)

    

    # makes the move for a troop
    def action_towards_defender(self, game, destination_hex, troop, screen):
        if destination_hex != None and destination_hex.occupied == False:
                                troop.action(destination_hex, game)
                                pygame.time.delay(500)
                                game.screen_update_bot(screen)
                                pygame.time.delay(500)
                                print("troupe déplacée : " + str(troop))

    def step_back(self, troop, board):
        pass


    # bie nimplémentée pour le défenseur mais faire de même pour l'attaquant
    def initialize_bot(self, game, screen):
        # placing the troops a bit far from the defended hexagon
        pygame.time.delay(1000)
        game.screen_update_bot(screen)
        print(game.defended_hex)
        central_hex = game.board.select_far_hex(game.defended_hex)
        possibilities = game.board.larger_list_neighbors(central_hex)
        entiers = list(range(0, len(possibilities)))
        entiers_aleatoires = random.sample(entiers, len(entiers))
        i = 0
        print(possibilities)
        for troop in self.troops_available:
            # Choix de l'hexagone pour placer la troupe, aléatoirement sur la carte
            while i < len(possibilities) and troop[1] != 0:
                if (
                    not possibilities[entiers_aleatoires[i]].occupied
                    and possibilities[entiers_aleatoires[i]].accessible):

                    possibilities[entiers_aleatoires[i]].occupied = True
                    if troop[0] == "assassin":
                        new_troop = Assassin(possibilities[entiers_aleatoires[i]])

                    elif troop[0]  == "magician":
                        new_troop = Magician(possibilities[entiers_aleatoires[i]])

                    elif troop[0]  == "turret":
                        new_troop = Turret(possibilities[entiers_aleatoires[i]])

                    self.add_troop(new_troop)
                    pygame.time.delay(1000)
                    game.screen_update_bot(screen)
                    print(str(troop[0]) + " place")
                    pygame.time.delay(1000)
                    possibilities[entiers_aleatoires[i]].occupied = True
                    troop[1] -= 1
                i += 1


# DEFENSEUR BOT
class DefenderBot(Bot):
    def __init__(self):
        super().__init__("DefenderBot", "Defender")
        self.troops_available = [
            ["archer", 2, None, False],
            ["shield", 1, None, False],
            ["engineer", 1, None, False],
        ]
        self.defended_hexagon = None
        self.position = (0, 0)
        self.selected_troop_index = None

    # implémentation de la logique du bot défenseur, en utilisant la génération de clicks...
    def make_move_bot(self, game, screen):
        # logique pour le défenseur bot
        player = game.attacker
        for selected_troop in self.troops:
            if selected_troop.health > 0:
                    selected_troop.selected = True
                    game.screen_update_bot(screen)
                    pygame.time.delay(500)
                    print(self.distance_with_opponants(game, selected_troop, player))
                    self.use_selected_troop(selected_troop, game, player, screen)
                    game.screen_update_bot(screen)
                    pygame.time.delay(1500)
                    selected_troop.selected = False
        print("action terminée du bot !")
        game.change_player()
        game.current_player.regenerate_speed()
        if game.current_player.name == "Defender":
            game.display_Event(screen)

    # si une troupe est sélectionnée, l'utiliser
    def use_selected_troop(self, selected_troop, game, player, screen):

        # start with searching attackable troops
        print(self.find_attackable_troop(game, selected_troop, player))
        target_troop = self.find_attackable_troop(game, selected_troop, player)[0]
        d_target = self.find_attackable_troop(game, selected_troop, player)[1]
        print("target troop : " + str(target_troop))
        # vérifier si la troupe a une capacité d'attaque non nulle
        if selected_troop.attack_capacity > 0:
            # vérifier si la troupe peut attaquer une troupe ennemie
            print ("attacke chosen")
            pygame.time.delay(50)
            if d_target <= selected_troop.attack_range:
                # attaquer une troupe ennemie si il y en a une à portée
                if selected_troop.is_troop_allowed_to_strike(target_troop, game):
                    selected_troop.action(target_troop.hex, game)
                    pygame.time.delay(500)

            else:
                # trouver la troupe ennemie la plus proche et se déplacer vers elle si il reste de la vitesse
                if selected_troop.speed != 0:
                    # flake8: noqa
                    if d_target <= selected_troop.attack_range + selected_troop.speed:
                        print
                        # sé déplacer et attaquer si la troupe est à porté suffisante après le déplacement considérant la vitesse restante
                        while (selected_troop.speed > 0 and selected_troop.attack_range < d_target):
                            destination_hex = game.board.find_destination_hex(
                                selected_troop.hex, target_troop.hex)
                            pygame.time.delay(50)
                            self.action_towards_attacker(game, destination_hex, selected_troop, screen)
                            d_target -= 1
                        # attack after moving
                        if selected_troop.is_troop_allowed_to_strike(target_troop, game):
                            selected_troop.action(target_troop.hex, game)
                            pygame.time.delay(10)
                        self.go_towards_defended_hexagon(game, selected_troop, screen)

                        
                    else:
                        # tries to heal
                        self.heal(game, selected_troop, screen)
                        # se rapprocher de la troupe ennemie et s'arreter là
                        destination_hex = game.board.find_destination_hex(
                            selected_troop.hex, target_troop.hex
                        )
                        pygame.time.delay(50)
                        self.action_towards_attacker(game, destination_hex, selected_troop, screen)
                        # tries to heal again
                        self.heal(game, selected_troop, screen)
                        self.go_towards_defended_hexagon(game, selected_troop, screen)
                        self.heal(game, selected_troop, screen)


        else:
            # no attack capacity, move towards the defend hexagon
            self.go_towards_defended_hexagon(game, selected_troop, screen)


    # makes the move for a troop
    def action_towards_attacker(self, game, destination_hex, troop, screen):
        if destination_hex != None and destination_hex.occupied == False:
                                troop.action(destination_hex, game)
                                pygame.time.delay(500)
                                game.screen_update_bot(screen)
                                pygame.time.delay(500)
                                print("troupe déplacée : " + str(troop))

    def step_back(self, troop, board):
        pass

    def initialize_bot(self, game, screen):
        # select a random hexagon to defend
        i = random.randint(0, len(game.board.list))
        self.defended_hexagon = game.board.list[i]
        game.board.list[i].toDefended()
        game.defended_hex = game.board.list[i]
        pygame.time.delay(1000)
        print("hexagon defended chosen")
        game.screen_update_bot(screen)

        # choisit la stratégie de placer par défaut un archer sur l'hexagone à défendre
        archer = Archer(game.board.list[i])
        self.troops_available[0][1] -= 1
        self.add_troop(archer)
        pygame.time.delay(1000)
        game.screen_update_bot(screen)

        defense = game.board.larger_list_neighbors(self.defended_hexagon)
        print(defense)

        for troop in self.troops_available:
            if troop[1] != 0:
                troop[3] = True
                j = 0
                while troop[1] != 0 and j < len(defense):
                    if not defense[j].occupied and defense[j].accessible:
                        if troop[0] == "shield":
                            troop1 = Shield(defense[j])

                        elif troop[0] == "engineer":
                            troop1 = Engineer(defense[j])

                        elif troop[0] == "archer":
                            troop1 = Archer(defense[j])
                        self.add_troop(troop1)
                        pygame.time.delay(1000)
                        game.screen_update_bot(screen)
                        print(str(troop[0]) + " place")
                        pygame.time.delay(1000)
                        game.board.larger_list_neighbors(self.defended_hexagon)[
                            j
                        ].occupied = True
                        troop[1] -= 1
                    j += 1
                troop[3] = False
