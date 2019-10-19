class setup:
    def __init__(self):
        window_width = 750
        window_height = 750
        self.window = (window_width, window_height)
        self.sprite_width = window_width/15
        self.sprite_height = window_height/15
        self.position = {}

    def loading_stage(filename):

        with open(filename, "r") as stage:
            k = 0  
            for i in range(15):
                line = stage.readline()

                for j in range(15):
                
                    lettre = line [j]
                    setup.position[k] = lettre
                    
                    k += 1
        return setup.position

setup.__init__(setup)
setup.loading_stage("level.txt")

print (setup.window)
for i in range(15*15):
    print(setup.position[i])