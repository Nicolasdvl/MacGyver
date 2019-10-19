class hero:
    def __init__(self, level):
        for i in range(15*15):
            if level[i] == "s":
                self.pos = i
        self.inventory = []

    def movement(self, pos, level):
        
        print("Quel déplacement voulez-vous effectuer ?")
        move = input()
        if move == "z":

            if level[pos - 15] == "x":
                print("Un mur vous fait face")
                return int(pos)
            
            else:
                pos = pos - 15
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "s":

            if level[pos + 15] == "x":
                print("Un mur vous fait face")
                return int(pos)
            
            else:
                pos = pos + 15
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "q":

            if level[pos - 1] == "x":
                print("Un mur vous fait face")
                return int(pos)
            
            else:
                pos = pos - 1
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        elif move == "d":

            if level[pos + 1] == "x":
                print("Un mur vous fait face")
                return int(pos)
            
            else:
                pos = pos + 1
                print("Vous vous trouvez sur la case :" + str(pos))
                return int(pos)
                
        else:
            print("Saisie non compris, utilisez les touches zqsd")

    
    def pick(self, inventory, pos_item, name_item, pos_hero):
        if pos_item == pos_hero:
            print("Vous ramasser un objet !")
            inventory.append(name_item)
            pos_item = 0

            return pos_item, inventory
        else :
            pass

