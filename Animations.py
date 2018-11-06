
class AnimeExplosions():
    def __init__(self,pos,type,repeat=0):
        self.repeat = repeat
        self.type = type
        
        self.pos = pos
        self.time = -1

    
    def tick(self):
        self.time += 1


