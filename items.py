from random import randint


class Items:
    def __init__(self, name, level):
        """ Fais apparaître aléatoirement les objets sur la position d'un passage
        """

        self.name = name
        x = randint(0, 224)
        while level[x] != "p":
            x = randint(0, 224)
        self.pos = x
        self.visibility = 1
