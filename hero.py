class Hero:
    def __init__(self, level):
        for pos,element in enumerate(level):
            if element == "s":
                self.pos = pos
        self.inventory = []

    def move(self, level):
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
        if item.pos == self.pos:
            self.inventory.append(item.name)
            self.inventory.sort()
            item.pos = 0
    
    def craft(self):
        if self.inventory == ['ether', 'tube', 'needle']:
            self.inventory = ['syringe']


