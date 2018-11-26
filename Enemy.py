from math import sqrt

class Enemy():
    def __init__(self,pos,size=[248,196]):
        self.pos = pos
        self.size = size
        self.alive = True
        self.timer = 0
        self.radius = 10

    
    def tick(self):
        self.timer += 1

    
    def checkHitox(self,posSource,radiusSource=0):
        #"source" og damage
        #length to source
        distanceToSource = int(sqrt((posSource[0]-self.pos[0])**2+(posSource[1]-self.pos[1])**2))
        radiusToRadius = distanceToSource - radiusSource - self.radius
        if (radiusToRadius < 0):
            return True
        else:
            return False
    
    
    def die(self):
        self.alive = False

        

