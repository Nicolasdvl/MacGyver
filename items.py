from random import randint

class Items:
    def __init__(self, name, level):

        """ Fais apparaître aléatoirement les objets sur la position d'un passage
        """

        self.name = name
        x = randint(0, 225)
        while level[x] != "p":
            x = randint(0, 225)
        self.pos = x
        

   
