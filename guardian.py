class Guardian:

    def __init__(self, level):
        """ Parcours la liste level pour déterminer la position du gardien
        """

        for pos, element in level.items():
            if element == "e":
                self.pos = pos
        self.visibility = 1
        
    def is_there_anyone_here(self, hero, config):
        """ Vérifie les conditions de victoire
        """

        if hero.pos == self.pos and hero.inventory == ['syringe']:
            config.run = False
            config.win = True
        elif hero.pos == self.pos and hero.inventory != ['syringe']:
            config.run = False
            config.win = False
        else:
            config.run = True
