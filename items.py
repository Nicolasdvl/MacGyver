from random import *

class Items:
    def __init__(self, name, level):
        self.name = name
        x = randint(0, 225)
        while level[x] != "p":
            x = randint(0, 225)
        self.pos = x
        

   
