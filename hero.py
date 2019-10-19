class hero:
    def __init__(self):
        self.pos = 16
    

    def movement(self, pos, level):
        
        print("Quel déplacement voulez-vous effectuer ?")
        move = input()
        if move == "z":
            if level[pos - 15] == "x":
                print("Un mur vous fait face")
            #elif level[pos - 15] == "p":
            else:
                pos = pos - 15
                return pos
        if move == "s":
            if level[pos + 15] == "x":
                print("Un mur vous fait face")
            #elif level[pos + 15] == "p":
            else:
                pos = pos + 15
                return pos
        if move == "q":
            if level[pos - 1] == "x":
                print("Un mur vous fait face")
            #elif level[pos - 1] == "p":
            else:
                pos = pos - 1
                return pos
        if move == "d":
            if level[pos + 1] == "x":
                print("Un mur vous fait face")
            #elif level[pos + 1] == "p":
            else:
                pos = pos + 1
                return pos
        else:
            print("Saisie non compris, utilisez les touches zqsd")