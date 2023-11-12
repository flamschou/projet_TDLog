# file to define the dices and there methods, because the game use special dices
import random

class Dice:
    def __init__(self, attr1, attr2, attr3, attr4, attr5):
        # initialisation with 5 attributes on the 5 first faces
        self.faces = [attr1, attr2, attr3, attr4, attr5, None]
        # the sixth face has a random attribute chose between the 5 first
        self.faces[-1] = random.choice([attr1, attr2, attr3, attr4, attr5])

    def get_faces(self):
        # returns the the faces of the dice
        return self.faces

    def roll(self):
        # throws the dice and returns a random face
        rolled_face = random.choice(self.faces)
        return rolled_face
