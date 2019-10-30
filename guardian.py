class Guardian:
    
    def __init__(self, level):
        for i in range(15*15):
            if level[i] == "e":
                self.pos = i

    def is_there_anyone_here(self, pos, end, run):
        if pos == end:
            run = False
        else:
            pass
        return run
