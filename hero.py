class hero:
    def __init__(self):
        self.pos = 16
    

    def movement(self, pos):
        
        print("Quel déplacement voulez-vous effectuer ?")
        move = input()
        if move == "z":
            if level[pos - 15] == "x":
                print("Un mur vous fait face")
            elif level[pos - 15] == "p":
                pos = pos - 15
        if move == "s":
            if level[pos + 15] == "x":
                print("Un mur vous fait face")
            elif level[pos + 15] == "p":
                pos = pos + 15
        if move == "q":
            if level[pos - 1] == "x":
                print("Un mur vous fait face")
            elif level[pos - 1] == "p":
                pos = pos - 1
        if move == "d":
            if level[pos + 1] == "x":
                print("Un mur vous fait face")
            elif level[pos + 1] == "p":
                pos = pos + 1