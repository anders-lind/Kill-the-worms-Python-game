import pygame as pygame


class Game():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((400,300))

        self.state = 0
        self.started = False
        self.running = True

        self.movingUp = False
        self.movingRight = False
        self.movingDown = False
        self.movingLeft = False

        self.startKnapHover = False
        self.leftClick = False
        self.rightClick = False
        self.middleClick = False

        
        self.sheetTerrain = pygame.image.load("grass-1-1.png").convert()
        self.sheetPlayerIdle = pygame.image.load("hr-level1_idle.png").convert()
        self.sheetPlayerRunning = pygame.image.load("hr-level1_running.png").convert()
        #Up = (88*0,132*0,88,132) Right = (88*0,132*2,88,132) Down = (88*0,132*4,88,132) Left = (88*0,132*6,88,132)
        rects = ((88*0,132*0,88,132),(88*0,132*2,88,132),(88*0,132*4,88,132),(88*0,132*6,88,132))

        self.sprites = []
        for r in rects:
            image = pygame.Surface(pygame.Rect(r).size).convert()
            image.blit(self.sheetPlayerRunning, (0, 0), pygame.Rect(r))
            self.sprites.append(image)


        self.test = False
        self.test2 = False
        self.testTal = 0




    def input(self,pygameEvents):
        #musepositionen
        mouseX,mouseY = pygame.mouse.get_pos()
        #print(mouseX,mouseY)

        #trykkede knapper
        pygame.event.get()
        leftClick,middleClick,rightClick = pygame.mouse.get_pressed()
        if leftClick or rightClick or middleClick:
            print(leftClick,rightClick,middleClick)

        keys=pygame.key.get_pressed()

        a = 0
        for key in range (0,len(keys)):
            a += 1
            if key == 1:
                pass
                #print("key", a)
        #if self.test:
            #print("True")


        if self.state == 0:
            if (100 < mouseX < 100+200 and 75 < mouseY < 75+50):
                self.startKnapHover = True
                self.testTal += 10
                print("startknap hover")
            else:
                self.startKnapHover = False

            if self.startKnapHover and self.testTal > 500:
                self.state = 1
                print("starter spillet")
        

        if self.state == 1:
            pass
            #print("State 1")


    
    def lavKnapper(self):
        self.knapper = []
        '''
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        myFont = pygame.font.SysFont('Comic Sans MS', 30)

        #knap ((R,G,B),(CornerX,cornerY,height,width))

        startKnap = ((200,200,200),(100,75,200,50))
        self.knapper.append(startKnap)
        '''



            




