from random import randint


class Items:

    positions = []

    def __init__(self, name, level):
        """ Fais apparaître aléatoirement les objets sur la position d'un passage
        """

        self.name = name
        x = randint(0, 224)
        while level[x] != "p" and x not in self.positions:
            x = randint(0, 224)
        self.pos = x
        self.visibility = True
        self.positions.append(self.pos)
