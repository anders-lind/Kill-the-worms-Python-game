import pygame as pygame
from Game import *

game = Game(pygame)
clock = pygame.time.Clock() 	


def main():
	if not game.started:
		#åbner et vindue, Køres kun en gang
		pygame.init()
		logo = pygame.image.load("logo.png")
		pygame.display.set_icon(logo)
		pygame.display.set_caption("Python-Spil")
		screen = pygame.display.set_mode((1200,700))
		game.started = True
		game.sprites(pygame)
		print("game started")

	while not game.done:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				game.done = True
		
		pressed = pygame.key.get_pressed()

		game.tick(pygame,events,pressed)
		render(screen)

		clock.tick(60)
		
		
def render(screen):
	if (game.started):
		#things on the screen is rendered here
		font1 = pygame.font.SysFont('Comic Sans MS', 30)
		
		#state 0 = Start menu
		if game.state == 0:
			#StartKnap
			if game.startKnapHover:
				pygame.draw.rect(screen,(220,220,220),(100,75,200,50))
				textSurface = font1.render('Start', True, (100, 100, 100))
				screen.blit(textSurface,(100+60,75))

			else:
				pygame.draw.rect(screen,(180,180,180),(100,75,200,50))
				textSurface = font1.render('Start', True, (100, 100, 100))
				screen.blit(textSurface,(100+60,75))

		#state 1 = in-game				
		if game.state == 1 or game.state == 2:
			#background
			screen.blit(game.sheetTerrain,(-128*2,128*0))
			screen.blit(game.sheetTerrain,(-128*4,128*1))
			screen.blit(game.sheetTerrain,(-128*3,128*2))
			screen.blit(game.sheetTerrain,(-128*1,128*3))
			screen.blit(game.sheetTerrain,(-128*4,128*4))
			screen.blit(game.sheetTerrain,(-128*3,128*5))


			#Player
			#diagonal movement
			posX = game.playerPos[0] - game.playerSize[0]/2
			posY = game.playerPos[1] - game.playerSize[1]/2
			playerSpritePos = [posX,posY]

			#hitbox
			if game.devMode:
				pos = [int(game.playerPos[0]),int(game.playerPos[1])]
				pygame.draw.circle(screen,[255,0,0],pos,int(game.playerSize[1]/2),1)

			if game.w and game.d:
				screen.blit(game.playerSprites[1],playerSpritePos)
			elif game.s and game.d:
				screen.blit(game.playerSprites[3],playerSpritePos)
			elif game.s and game.a:
				screen.blit(game.playerSprites[5],playerSpritePos)
			elif game.w and game.a:
				screen.blit(game.playerSprites[7],playerSpritePos)
			#straightMovemt
			elif game.w:
				screen.blit(game.playerSprites[0],playerSpritePos)
			elif game.d:
				screen.blit(game.playerSprites[2],playerSpritePos)
			elif game.s:
				screen.blit(game.playerSprites[4],playerSpritePos)
			elif game.a:
				screen.blit(game.playerSprites[6],playerSpritePos)
			#Idle
			elif game.lastMovement == "None":
				screen.blit(game.playerSprites[4],playerSpritePos)
			elif game.lastMovement == "UP":
				screen.blit(game.playerSprites[0],playerSpritePos)
			elif game.lastMovement == "UP_RIGHT":
				screen.blit(game.playerSprites[1],playerSpritePos)
			elif game.lastMovement == "UP_LEFT":
				screen.blit(game.playerSprites[7],playerSpritePos)
			elif game.lastMovement == "DOWN":
				screen.blit(game.playerSprites[4],playerSpritePos)
			elif game.lastMovement == "DOWN_RIGHT":
				screen.blit(game.playerSprites[3],playerSpritePos)
			elif game.lastMovement == "DOWN_LEFT":
				screen.blit(game.playerSprites[5],playerSpritePos)
			elif game.lastMovement == "RIGHT":
				screen.blit(game.playerSprites[2],playerSpritePos)
			elif game.lastMovement == "LEFT":
				screen.blit(game.playerSprites[6],playerSpritePos)


			#enemies alive
			for e in game.enemies:
				e.tick()
				if e.timer+1 > len(game.wormAttack1Sprites):
					e.timer = 0
				sprite = game.wormAttack1Sprites[e.timer]
				pos = [e.pos[0] - e.size[0]/2,e.pos[1] - e.size[1]/2]
				screen.blit(sprite,pos)

				#hitbox
				if game.devMode:
					pygame.draw.circle(screen,[255,0,0],e.pos,int(game.enemySize[1]/2),1)
					pygame.draw.rect(screen,[255,0,0],(pos[0],pos[1],e.size[0],e.size[1]),1)
				
			#enemies dead
			for e in game.deadEnemies:
				e.tick()
				if e.timer+1 > len(game.wormDieSprites):
					sprite = game.wormDieSprites[len(game.wormDieSprites)-1]
				else:
					sprite = game.wormDieSprites[e.timer]
				pos = [e.pos[0] - e.size[0]/2,e.pos[1] - e.size[1]/2]
				screen.blit(sprite,pos)
				#hitbox
				if game.devMode:
					pygame.draw.circle(screen,[255,0,0],e.pos,int(game.enemySize[1]/2),1)
					pygame.draw.rect(screen,[255,0,0],(pos[0],pos[1],e.size[0],e.size[1]),1)


			#bombs
			for b in game.bombs:
				screen.blit(game.spriteDynamite,b.pos)
				#hitbox
				if game.devMode:
					pos = [int(b.pos[0]),int(b.pos[1])]
					pygame.draw.circle(screen,[255,0,0],pos,int(game.bombSize[1]/2),1)


			#animations
			n = -1
			for a in game.animations:
				n += 1
				if a.type == 2:
					a.tick()
					if not a.time > len(game.explosionSprites):
						sprite = game.explosionSprites[a.time-1]
						pos = a.pos
						screen.blit(sprite,pos)
					else:
						del game.animations[n]
			
			#HUD
			#timer
			pygame.draw.rect(screen,(0,0,0),(770,10,200,50))
			text = str("Time: " + str(int(game.time/60)))
			textSurface = font1.render(text, True, (255, 255, 255))
			screen.blit(textSurface,(780,10))

			#points
			pygame.draw.rect(screen,(0,0,0),(990,10,200,50))
			text = str("Points: " + str(game.points))
			textSurface = font1.render(text, True, (255, 255, 255))
			screen.blit(textSurface,(1000,10))

			#win screen
			if game.state == 2:
				s = pygame.Surface((550,160),pygame.SRCALPHA)
				s.fill((50,50,50,200))
				text1 = str("You killed all enemies!")
				text2 = str("It only took " + str(int(game.time/60)) + " seconds")
				text3 = str("You earned  a score of " + str(int(game.points*100 / (int((game.time/60)+1)))))
				font1 = pygame.font.SysFont('Comic Sans MS', 40)
				textSurface1 = font1.render(text1, True, (255, 255, 255))
				textSurface2 = font1.render(text2, True, (255, 255, 255))
				textSurface3 = font1.render(text3, True, (255, 255, 255))
				s.blit(textSurface1,(10,10))
				s.blit(textSurface2,(10,10+40))
				s.blit(textSurface3,(10,10+80))
				screen.blit(s,(350,250))


					
		pygame.display.flip()


main()
