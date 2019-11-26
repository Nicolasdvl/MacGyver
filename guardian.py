class Guardian:
    
    def __init__(self, level):
        for pos,element in enumerate(level):
            if element == "e":
                self.pos = pos

    def is_there_anyone_here(self, hero, setup):
        if hero.pos == self.pos and hero.inventory == ['syringe']:
            win = 1 
            setup.run = False
        elif hero.pos == self.pos and hero.inventory != ['syringe']:
            win = 0
            setup.run == False
        return win
