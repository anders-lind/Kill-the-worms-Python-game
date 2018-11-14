from math import sqrt

class Enemy():
    def __init__(self,pos,size=10):
        self.pos = pos
        self.size = size
        self.alive = True
        self.timer = 0

    
    def tick(self):
        self.timer += 1

    
    def checkHitox(self,posOfSource,radiusSource=0):
        #"source" og damage
        posSource = posOfSource
        radiusSource = radiusSource

        #length to source
        distanceToSource = int(sqrt((posSource[0]-self.pos[0])**2+(posSource[1]-self.pos[1])**2))
        distanceToRadius = distanceToSource - radiusSource
        if (distanceToRadius <= self.size):
            return True
        else:
            return False
    
    def die(self):
        self.alive = False

        

