class Setup:
    def __init__(self):
        self.window_width = 750
        self.window_height = 750
        self.window = (self.window_width, self.window_height)
        self.sprite_width = self.window_width/15
        self.sprite_height = self.window_height/15
        self.run = True

    def loading_stage(self, filename):

        with open(filename, "r") as stage:
            k = 0 
            structure = {}
            for i in range(15):
                line = stage.readline()

                for j in range(15):
                
                    lettre = line [j]
                    structure[k] = lettre
                    
                    k += 1
        return structure