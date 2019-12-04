class Guardian:
    
    def __init__(self, level):

        """ Parcours la liste level pour déterminer la position du gardien
        """

        for pos,element in level.items():
            if element == "e":
                self.pos = pos

    def is_there_anyone_here(self, hero, setup):

        """ Vérifie les conditions de victoire
        """

        if hero.pos == self.pos and hero.inventory == ['syringe']:
            win = 1 
            setup.run = False
        elif hero.pos == self.pos and hero.inventory != ['syringe']:
            win = 0
            setup.run == False
        return win
