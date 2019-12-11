class Hero:
    def __init__(self, level):
        """ Parcours le dico level pour trouver la pos de héro et initialise un inventaire
        """

        for pos, element in level.items():
            if element == "s":
                self.pos = pos
        self.inventory = []
        self.visibility = 1

    def move(self, level, move):
        """ Permet le déplacement de héro
        """

        pos = self.pos
        if move == "up":

            if level[pos - 15] == "x":
                self.pos = pos

            else:
                pos = pos - 15
                self.pos = pos

        elif move == "down":

            if level[pos + 15] == "x":
                self.pos = pos

            else:
                pos = pos + 15
                self.pos = pos

        elif move == "left":

            if level[pos - 1] == "x":
                self.pos = pos

            else:
                pos = pos - 1
                self.pos = pos

        elif move == "right":

            if level[pos + 1] == "x":
                self.pos = pos

            else:
                pos = pos + 1
                self.pos = pos

    def pick(self, item):
        """ Ajoute un objet à l'inventaire de héro si celui-ci se trouve sur la même position
        """

        if item.pos == self.pos and item.visibility == 1:
            self.inventory.append(item.name)
            item.visibility = 0

    def craft(self):
        """ Vérifie si le héro a ramassé tous les objets
        """
        
        if 'ether' in self.inventory and 'tube' in self.inventory and 'needle' in self.inventory:
            self.inventory = ['syringe']
