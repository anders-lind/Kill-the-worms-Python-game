from Bomb import Bomb

class Game():
    def __init__(self, pygame):
        #pygame.init()
        #screen = pygame.display.set_mode((1,1))
        
        #Game status variables
        self.started = False
        self.done = False
        self.state = 0

        #mus
        self.mouseX,self.mouseY = 0,0

        #Keyboard input variables
        self.w = False
        self.d = False
        self.s = False
        self.a = False
        self.k = False
        self.leftClick = False
        self.rightClick = False
        self.middleClick = False

        #Knapper
        self.startKnapHover = False

        #Player variables
        self.lastMovement = "None"
        self.pX = 0
        self.pY = 0
        self.playerPos = [self.pX,self.pY]
        self.pVX = 0
        self.pVY = 0
        self.playerVel = [self.pVX,self.pVY]

        #bombs
        self.bombs = []

        #Sprites
        self.playerSprites = []
        self.explosionSprites = []

        #animations
        self.animations = []

    def tick(self,pygame,events,pressed):
        self.input(pygame,events,pressed)
        self.physics()
        
        

    def createBomb(self):
        print("create bomb")
        bomb = Bomb(self.playerPos[0],self.playerPos[1],self.mouseX,self.mouseY)
        self.bombs.append(bomb)


    def input(self,pygame,events,pressed):
        #mus:  positionen og klik
        self.mouseX,self.mouseY = pygame.mouse.get_pos()
        self.leftClick,self.middleClick,self.rightClick = pygame.mouse.get_pressed()

        #keyboard keys
        for event in events:
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                #print(event.key)
                if event.key == 97:
                    self.a = True
                elif event.key == 100:
                    self.d = True
                elif event.key == 107:
                    self.k = True
                elif event.key == 115:
                    self.s = True
                elif event.key == 119:
                    self.w = True

            if event.type == pygame.KEYUP:
                print("key lifted")
                #print(event.key)
                if event.key == 97:
                    self.a = False
                elif event.key == 100:
                    self.d = False
                elif event.key == 107:
                    self.k = False
                elif event.key == 115:
                    self.s = False
                elif event.key == 119:
                    self.w = False
                
        if self.state == 0:
            #Startknap
            if (100 < self.mouseX < 100+200 and 75 < self.mouseY < 75+50):
                self.startKnapHover = True
                if self.leftClick == 1:
                    self.state = 1
            else:
                self.startKnapHover = False

        if self.state == 1:
            if self.k:
                self.createBomb()


    def physics(self):
        if self.state == 1:


            #player x-movement
            if self.d:
                self.pVX = 10
                self.lastMovement = "RIGHT"
            elif self.a:
                self.pVX = -10
                self.lastMovement = "LEFT"
            else:
                self.pVX *= 0.5

            #player y-movement
            if self.w:
                self.pVY = -10
                self.lastMovement = "UP"
            elif self.s:
                self.pVY = 10
                self.lastMovement = "DOWN"
            else:
                self.pVY *= 0.5

            #player diagonal movement
            if self.d and self.w:
                self.lastMovement = "UP_RIGHT"
            if self.a and self.w:
                self.lastMovement = "UP_LEFT"
            if self.d and self.s:
                self.lastMovement = "DOWN_RIGHT"
            if self.a and self.s:
                self.lastMovement = "DOWN_LEFT"
           
            self.pX += self.pVX
            self.pY += self.pVY

            self.playerPos = [self.pX,self.pY]
            self.playerVel = [self.pVX,self.pVY]

            #bomb physics
            n = -1
            for b in self.bombs:
                n += 1
                b.move()
                if b.clock() >= 100:
                    explosion = b.explode()
                    self.animations.append(explosion)
                    del self.bombs[n]


    def sprites(self,pygame):
        #single sprites
        self.spriteDynamite = pygame.image.load("cliff-explosives.png").convert()

        #sprite sheets
        self.sheetTerrain = pygame.image.load("grass-1-1.png").convert()
        self.sheetPlayerIdle = pygame.image.load("hr-level1_idle.png").convert()
        self.sheetPlayerRunning = pygame.image.load("hr-level1_running.png").convert()
        self.sheetExplosion = pygame.image.load("explosion-1.png").convert()

        #player sprites
        #Up = (88*0,132*0,88,132) Up+Right = (88*0,132*1,88,132) Right = (88*0,132*2,88,132) Right+down = (88*0,132*0,88,132) Down = (88*0,132*4,88,132) Left = (88*0,132*6,88,132)
        playerRects = ((88*0,132*0,88,132),(88*0,132*1,88,132),(88*0,132*2,88,132),(88*0,132*3,88,132),(88*0,132*4,88,132),(88*0,132*5,88,132),(88*0,132*6,88,132),(88*0,132*7,88,132))
        for r in playerRects:
            image = pygame.Surface(pygame.Rect(r).size).convert()
            image.blit(self.sheetPlayerRunning, (0, 0), pygame.Rect(r))
            self.playerSprites.append(image)        
   

        #explosion sprites
        explosionRects = ((64*0,0,64,59),(64*1,0,64,59),(64*1,0,64,59),(64*2,0,64,59),(64*2,0,64,59),(64*3,0,64,59),(64*4,0,64,59),(64*5,0,64,59),(64*6,0,64,59),(64*7,0,64,59),(64*8,0,64,59),(64*9,0,64,59),(64*10,0,64,59),(64*11,0,64,59),(64*12,0,64,59),(64*13,0,64,59))
        for r in explosionRects:
            image = pygame.Surface(pygame.Rect(r).size).convert()
            image.blit(self.sheetExplosion, (0, 0), pygame.Rect(r))
            self.explosionSprites.append(image)

        


    '''
    def lavKnapper(self,pygame):
        self.knapper = []
        
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        myFont = pygame.font.SysFont('Comic Sans MS', 30)

        #knap ((R,G,B),(CornerX,cornerY,height,width))

        startKnap = ((200,200,200),(100,75,200,50))
        self.knapper.append(startKnap)
    '''



            




