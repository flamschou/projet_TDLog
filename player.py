# create the class player and his heritance

import enum
import random


class Player:
    """
    A player has attributes:
    - a name;
    - a number of medals;
    - a list of occupied hexagons;
    - a list of cards to use;

    All subclasses must define a description property.
    """

    def __init__(
        self,
        name,
        num_medals,
        list_of_hexagons,
        cards_to_use,
    ):
        self._name = name
        self._num_medals = num_medals
        self._list_of_hexagons = list_of_hexagons
        self._cards_to_use = cards_to_use

    @property
    def name(self):
        return self._name
   
    @property
    def num_medals(self):
        return self._num_medals

    @property
    def list_of_hexagons(self):
        return self._list_of_hexagons

    @list_of_hexagons.setter
    def list_of_hexagons(self, list_of_hexagons):
        self._list_of_hexagons = list_of_hexagons

    @property
    def cards_to_use(self):
        return self._cards_to_use
   
    @cards_to_use.setter
    def cards_to_use(self, cards_to_use):
        self._cards_to_use = cards_to_use



class HumanPlayer(Player):
    """
    A human player has one extra attribute, their name.

    They will choose their moves using the keyboard.
    """

    def __init__(
        self,
        name,
        num_medals,
        list_of_hexagons,
        cards_to_use,
    ):
        assert name.strip() != "", "invalid name"
        super().__init__(name, num_medals, list_of_hexagons, cards_to_use,)

        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return "(human)"

    



class RandomPlayer(Player):
    """
    A random player will randomly choose a move amongst all the legal ones.
    """

    def __init__(
        self,
        name,
        num_medals,
        list_of_hexagons,
        cards_to_use,
    ):
        super().__init__(name, num_medals, list_of_hexagons, cards_to_use,)
    
    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return "(random)"
    

""" peut être voir à changer name en status puisque ce qui compte c'est pas le nom mais
le statut d'attaque ou de défense, de toute facon très incomplet pour le moment, voir 
comment former les listes de cases et de cartes etc... """
