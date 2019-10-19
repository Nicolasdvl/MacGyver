class hero:
    def __init__(self, level):
        for i in range(15*15):
            if level[i] == "s":
                self.pos = i
    

    def movement(self, pos, level):
        
        print("Quel déplacement voulez-vous effectuer ?")
        move = input()
        if move == "z":

            if level[pos - 15] == "x":
                print("Un mur vous fait face")
            
            else:
                pos = pos - 15
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "s":

            if level[pos + 15] == "x":
                print("Un mur vous fait face")
            
            else:
                pos = pos + 15
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "q":

            if level[pos - 1] == "x":
                print("Un mur vous fait face")
            
            else:
                pos = pos - 1
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "d":

            if level[pos + 1] == "x":
                print("Un mur vous fait face")
            
            else:
                pos = pos + 1
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        else:
            print("Saisie non compris, utilisez les touches zqsd")