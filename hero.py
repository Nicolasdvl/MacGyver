class Hero:
    def __init__(self, level):

        """ Parcours le dico level pour trouver la pos de héro et initialise un inventaire
        """

        for pos, element in level.items():
            if element == "s":
                self.pos = pos
        self.inventory = []

    def move(self, level):

        """ Permet le déplacement de héro
        """

        pos = self.pos
        move = input()
        if move == "z":

            if level[pos - 15] == "x":
                self.pos = pos
            
            else:
                pos = pos - 15
                self.pos = pos
                
        elif move == "s":

            if level[pos + 15] == "x":
                self.pos = pos
            
            else:
                pos = pos + 15
                self.pos = pos
                
        elif move == "q":

            if level[pos - 1] == "x":
                self.pos = pos
            
            else:
                pos = pos - 1
                self.pos = pos
                
        elif move == "d":

            if level[pos + 1] == "x":
                self.pos = pos
            
            else:
                pos = pos + 1
                self.pos = pos
                
        else:
            print("Saisie non compris, utilisez les touches zqsd")

    
    def pick(self, item):

        """ Ajoute un objet à l'inventaire de héro si celui-ci se trouve sur la même position
        """

        if item.pos == self.pos:
            self.inventory.append(item.name)
            self.inventory.sort()
            item.pos = 0
    
    def craft(self):

        """ Vérifie si le héro a ramassé tous les objets
        """
        
        if self.inventory == ['ether', 'tube', 'needle']:
            self.inventory = ['syringe']


