class setup:
    def __init__(self):
        window_width = 750
        window_height = 750
        self.window = (window_width, window_height)
        self.sprite_width = window_width/15
        self.sprite_height = window_height/15
        self.run = True

    def loading_stage(self, filename):

        with open(filename, "r") as stage:
            k = 0 
            self = {}
            for i in range(15):
                line = stage.readline()

                for j in range(15):
                
                    lettre = line [j]
                    self[k] = lettre
                    
                    k += 1
        return self