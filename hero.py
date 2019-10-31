class Hero:
    def __init__(self, level):
        for i in range(15*15):
            if level[i] == "s":
                self.pos = i
        self.inventory = []

    def movement(self, pos, level):
        
        move = input()
        if move == "z":

            if level[pos - 15] == "x":
                return int(pos)
            
            else:
                pos = pos - 15
                return int(pos)
                
        elif move == "s":

            if level[pos + 15] == "x":
                return int(pos)
            
            else:
                pos = pos + 15
                return int(pos)
                
        elif move == "q":

            if level[pos - 1] == "x":
                return int(pos)
            
            else:
                pos = pos - 1
                return int(pos)
                
        elif move == "d":

            if level[pos + 1] == "x":
                return int(pos)
            
            else:
                pos = pos + 1
                return int(pos)
                
        else:
            print("Saisie non compris, utilisez les touches zqsd")

    
    def pick(self, inventory, pos_item, name_item, pos_hero):
        if pos_item == pos_hero:
            inventory.append(name_item)
            inventory.sort()
            pos_item = 0

            return pos_item, inventory
        else :
            pass
    
    def craft(self, inventory):
        if inventory == ['ether', 'tube', 'needle']:
            inventory = ['syringe']
            return inventory
        else:
            pass


