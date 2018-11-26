import math as math
from Animations import AnimeExplosions

class Bomb():
    def __init__(self,x1,y1,x2,y2,counter=100,vel=2):
        self.counter = counter
        self.endPos = [x2,y2]
        self.pos = [x1,y1]
        self.vel = vel
        self.timer = 0
        self.exploded = False
        self.radius = 5
        self.size = [128,128]

        self.direction = self.findDirection(self.pos,self.endPos)


    def move(self):
        self.pos[0] += self.direction[0] * self.vel
        self.pos[1] += self.direction[1] * self.vel
    
    def clock(self): 
        self.timer += 1
        return self.timer


    def explode(self):
        self.exploded = True
        explosion = AnimeExplosions(self.pos)
        print("EXPLOSION!")
        return(explosion)

    
    def findDirection(self,startPos,endPos):
        #(endPos - startPos) / lenght * vel

        dirX = endPos[0] - startPos[0]
        dirY = endPos[1] - startPos[1]

        lenght = math.sqrt(dirX**2 + dirY**2)

        directionX = dirX/lenght
        directionY = dirY/lenght

        direction = (directionX,directionY)
        return direction


