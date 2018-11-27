from Bomb import Bomb
from Enemy import Enemy
from Animations import AnimePlayer, AnimeExplosions
from random import randint

class Game():
    def __init__(self, pygame):        
        #Game status variables
        self.started = False
        self.done = False
        self.state = 0
        self.time = 0
        self.state1Started = False
        self.gameWon = False
        self.devMode = True

        #mus
        self.mouseX,self.mouseY = 0,0

        #Keyboard input variables
        self.w = False
        self.d = False
        self.s = False
        self.a = False
        self.k = False
        self.e = False
        self.p = False
        self.leftClick = False
        self.rightClick = False
        self.middleClick = False

        #Knapper
        self.startKnapHover = False

        #points
        self.points = 0

        #Player variables
        playerScale = 0.5
        self.playerSize = [int(88*playerScale),int(132*playerScale)]
        self.lastMovement = "None"
        self.playerSpeed = 5
        self.pX = 0
        self.pY = 0
        self.playerPos = [self.pX,self.pY]
        self.pVX = 0
        self.pVY = 0
        self.playerVel = [self.pVX,self.pVY]

        #bombs
        self.bombs = []
        bombScale = 0.5
        self.bombSize = [int(64*bombScale),int(59*bombScale)]
        self.bombThrowable = True

        #enemy
        self.enemies = []
        self.deadEnemies = []
        enemiyScale = 0.5
        self.enemySize = [int(248*enemiyScale),int(170*enemiyScale)]

        #Sprites
        self.playerSprites = []
        self.explosionSprites = []
        self.wormReadySprites = []
        self.wormAttack1Sprites = []
        self.wormDieSprites = []

        #test
        self.animePlayer = AnimePlayer(pygame)

        #animations
        self.animations = []


    def tick(self,pygame,events,pressed):
        self.gameConfig()
        self.input(pygame,events,pressed)
        self.physics()


    def createBomb(self):
        print("create bomb")
        bomb = Bomb(self.playerPos[0],self.playerPos[1],self.mouseX,self.mouseY)
        self.bombs.append(bomb)
    
    def createEnemy(self,pos,size):
        print("create enemy")
        enemy = Enemy(pos,size)
        self.enemies.append(enemy)
    
    def earnPoints(self,points):
        self.points += points
        print("You have earned ",self.points, " point!")

    def map(self):
        print("creating map")
        for i in range (0,10):
            #x = 1200  y = 700
            x = randint(100,1100)
            y = randint(100,600)
            pos = [x,y]
            self.createEnemy(pos,self.enemySize)

    def wonGame(self):
        self.gameWon = True
        self.state = 2


    def gameConfig(self):
        if self.state == 1:
            self.time += 1
            if not self.state1Started:
                self.state1Started = True
                self.map()
            if len(self.enemies) == 0:
                self.wonGame()
        else:
            pass


    def input(self,pygame,events,pressed):
        #mus:  positionen og klik
        self.mouseX,self.mouseY = pygame.mouse.get_pos()
        self.leftClick,self.middleClick,self.rightClick = pygame.mouse.get_pressed()

        #keyboard keys
        for event in events:
            if event.type == pygame.KEYDOWN:
                #print("key pressed")
                if event.key == 97:
                    self.a = True
                elif event.key == 100:
                    self.d = True
                elif event.key == 101:
                    self.e = True
                elif event.key == 107:
                    self.k = True
                elif event.key == 112:
                    self.p = True
                elif event.key == 115:
                    self.s = True
                elif event.key == 119:
                    self.w = True

            if event.type == pygame.KEYUP:
                #print("key lifted")
                if event.key == 97:
                    self.a = False
                elif event.key == 100:
                    self.d = False
                elif event.key == 101:
                    self.e = False
                elif event.key == 107:
                    self.k = False
                elif event.key == 112:
                    self.p = False
                elif event.key == 115:
                    self.s = False
                elif event.key == 119:
                    self.w = False
            
        #menu
        if self.state == 0:
            #Startknap
            if (100 < self.mouseX < 100+200 and 75 < self.mouseY < 75+50):
                self.startKnapHover = True
                if self.leftClick == 1:
                    self.state = 1
            else:
                self.startKnapHover = False

        #ingame
        if self.state == 1:
            if self.k and self.bombThrowable:
                self.createBomb()
                self.bombThrowable = False
            if not self.k:
                self.bombThrowable = True
            if self.e and self.enemyCreatable:
                pos = [self.mouseX,self.mouseY]
                self.createEnemy(pos,self.enemySize)
                self.enemyCreatable = False
            if not self.e:
                self.enemyCreatable = True
            if self.p:
                if self.devMode:
                    for e in self.enemies:
                        e.die()
                        self.deadEnemies.append(e)
                    self.enemies = []


    def physics(self):
        if self.state == 1:
            #player x-movement
            if self.d:
                self.pVX = self.playerSpeed
                self.lastMovement = "RIGHT"
            elif self.a:
                self.pVX = -self.playerSpeed
                self.lastMovement = "LEFT"
            else:
                self.pVX *= 0.5

            #player y-movement
            if self.w:
                self.pVY = -self.playerSpeed
                self.lastMovement = "UP"
            elif self.s:
                self.pVY = self.playerSpeed
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
            bN = -1
            for b in self.bombs:
                bN += 1
                b.move()
                if b.clock() >= b.counter:
                    explosion = b.explode()
                    self.animations.append(explosion)

                    #enemy hitbox
                    eL = []
                    eN = -1
                    for e in self.enemies:
                        eN += 1
                        if not e.alive:
                            continue
                        if e.checkHitox(b.pos,b.radius):
                            print("Enemy killed! ", len(self.enemies)-1, " enemies left!")
                            self.earnPoints(100)
                            e.die()
                            self.deadEnemies.append(e)
                            del self.enemies[eN]

                    del self.bombs[bN]


    def getSprite(self,type,info):
        if type == 1:
            action,direction = info
            sprite = self.animePlayer.chooseSprite(action,direction)
            return sprite
        else:
            print("Du valgte ikke player-animation")


    def sprites(self,pygame):
        #sprite sheets
        self.sheetTerrain = pygame.image.load("grass-1-1.png").convert_alpha()
        self.sheetPlayerIdle = pygame.image.load("hr-level1_idle.png").convert_alpha()
        self.sheetPlayerRunning = pygame.image.load("hr-level1_running.png").convert_alpha()
        self.sheetExplosion = pygame.image.load("explosion-1.png").convert_alpha()
        self.sheetWormReady = pygame.image.load("worm-prepared.png").convert_alpha()
        self.sheetWormAttack1 = pygame.image.load("worm-attack-01.png").convert_alpha()
        self.sheetWormDie = pygame.image.load("worm-die.png").convert_alpha()


        #single sprites
        spriteDynamite = pygame.image.load("cliff-explosives.png").convert_alpha()
        self.spriteDynamite = pygame.transform.scale(spriteDynamite,(self.bombSize[0],self.bombSize[1]))

        
        #player sprites
        playerRects = ((88*0,132*0,88,132),(88*0,132*1,88,132),(88*0,132*2,88,132),(88*0,132*3,88,132),(88*0,132*4,88,132),(88*0,132*5,88,132),(88*0,132*6,88,132),(88*0,132*7,88,132))
        for r in playerRects:
            image = pygame.Surface(pygame.Rect(r).size,pygame.SRCALPHA,32).convert_alpha()
            image.blit(self.sheetPlayerRunning, (0, 0), pygame.Rect(r))
            sprite = pygame.transform.scale(image,(self.playerSize[0],self.playerSize[1]))
            self.playerSprites.append(sprite)        
   

        #explosion sprites
        explosionRects = ((64*0,0,64,59),(64*1,0,64,59),(64*1,0,64,59),(64*2,0,64,59),(64*2,0,64,59),(64*3,0,64,59),(64*4,0,64,59),(64*5,0,64,59),(64*6,0,64,59),(64*7,0,64,59),(64*8,0,64,59),(64*9,0,64,59),(64*10,0,64,59),(64*11,0,64,59),(64*12,0,64,59),(64*13,0,64,59))
        for r in explosionRects:
            image = pygame.Surface(pygame.Rect(r).size,pygame.SRCALPHA,32).convert_alpha()
            image.blit(self.sheetExplosion, (0, 0), pygame.Rect(r))
            sprite = pygame.transform.scale(image,(int(64*1),int(59*1)))
            self.explosionSprites.append(image)
        
        #enemy ready
        wormReadyRects = []
        for i in range (0,10):
            wormReadyRects.append((190*i,156*0,190,156))
        for w in wormReadyRects:
            image = pygame.Surface(pygame.Rect(w).size,pygame.SRCALPHA,32).convert_alpha()
            image.blit(self.sheetWormReady, (0, 0), pygame.Rect(w))
            sprite = pygame.transform.scale(image,(100,100))
            self.wormReadySprites.append(sprite)
        
        #enemy attack
        wormAttack1Rects = []
        for i in range (0,8):
            rect = (248*i+25,196*6+19,248,170)
            wormAttack1Rects.append(rect)
        for w in wormAttack1Rects:
            image = pygame.Surface(pygame.Rect(w).size,pygame.SRCALPHA,32).convert_alpha()
            image.blit(self.sheetWormAttack1, (0, 0), pygame.Rect(w))
            sprite = pygame.transform.scale(image,(self.enemySize[0],self.enemySize[1]))
            self.wormAttack1Sprites.append(sprite)

        #enemy die
        wormDieRects = []
        for x in range (0,5):
            for y in range (0,3):
                rect = (1188/6*x, 684/4*y, 1188/6, 684/4)
                wormDieRects.append(rect)
        for w in wormDieRects:
            image = pygame.Surface(pygame.Rect(w).size,pygame.SRCALPHA,32).convert_alpha()
            image.blit(self.sheetWormDie, (0, 0), pygame.Rect(w))
            sprite = pygame.transform.scale(image,(self.enemySize[0],self.enemySize[1]))
            self.wormDieSprites.append(sprite)


        


            




