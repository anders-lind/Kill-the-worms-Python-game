class AnimeExplosions():
    def __init__(self,pos,type=2,repeat=False):
        self.type = type
        self.repeat = repeat        
        self.pos = pos
        self.time = -1


    def tick(self):
        self.time += 1



#bruges ikke
class AnimePlayer():
    def __init__(self,repeat=True):
        #pygame.init()
        #pygame.display.set_mode((1,1))

        self.repeat = repeat        
        self.time = -1
        self.ready = False


    def tick(self):
        if not self.ready:
            self.setup()
        self.time += 1
