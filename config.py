class Config:
    def __init__(self):
        """Initialise la largeur et la hauteur de la fenêtre ainsi que des sprites
        """

        self.window_width = 750
        self.window_height = 750
        self.window = (self.window_width, self.window_height)
        #self.font_pos = 
        self.sprite_width = int(self.window_width/15)
        self.sprite_height = int(self.window_height/15)
        self.inventory_sprite = int(self.sprite_height/2)
        self.inventory_font = 220
        self.inventory_one = 222
        self.inventory_two = 223
        self.inventory_three = 224
        self.instruction_one = 91
        self.instruction_two = 106
        self.instruction_three = 121
        self.final = 108

        self.run = True
        self.win = False

    def loading_stage(self, filename):
        """Parcours un fichier txt pour le convertir en dico 
        """

        with open(filename, "r") as stage:
            k = 0
            structure = {}
            for i in range(15):
                line = stage.readline()

                for j in range(15):

                    lettre = line[j]
                    structure[k] = lettre

                    k += 1
        return structure
