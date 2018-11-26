
#type: 2 = explosions
#type: 1 = player
#import pygame as pygame


class AnimeExplosions():
    def __init__(self,pos,type=2,repeat=False):
        self.type = type
        self.repeat = repeat        
        self.pos = pos
        self.time = -1


    def tick(self):
        self.time += 1




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

'''
    def setup(self,pygame):
        self.pygame = pygame
        self.sheetPlayerRunning = self.pygame.image.load("hr-level1_running.png").convert()
        
        sheet = self.sheetPlayerRunning
        line = 0
        amount = 22
        size = [88,132]
        self.RunningUp = self.createSprites(pygame,sheet,line,amount,size)


    def chooseSprite(self,pygame,action,direction):
        self.tick()
        if action == "RUNNING":
            if direction == "UP":
                sprites = self.RunningUp
                #n = self.time % len(sprites)
                return sprites[1]

    
    def createSprites(self,pygame,sheet,line,amount,size):
        #sheet = pygame.image.load("hr-level1_running.png").convert()
        #size = [88,132]
        #line = 0
        #amount = 22
        sprites = []
        for i in range (0,amount):
            spriteSize = (size[0]*i,line,size[0],size[1])
            image = pygame.Surface(pygame.Rect(spriteSize).size).convert()
            image.blit(self.sheetPlayerRunning,(0, 0),pygame.Rect(spriteSize))
            sprites.append(image)
            return sprites
'''
