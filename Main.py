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
		screen = pygame.display.set_mode((800,600))
		game.started = True
		game.sprites(pygame)
		print("game starting")

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
		#state 1 = in-game

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
				

		if game.state == 1:

			#background
			screen.blit(game.sheetTerrain,(-128*2,0))
			screen.blit(game.sheetTerrain,(-128*6,128))
			screen.blit(game.sheetTerrain,(-256*4,256))

			#Player
			#diagonal movement
			if game.w and game.d:
				screen.blit(game.playerSprites[1],game.playerPos)
			elif game.s and game.d:
				screen.blit(game.playerSprites[3],game.playerPos)
			elif game.s and game.a:
				screen.blit(game.playerSprites[5],game.playerPos)
			elif game.w and game.a:
				screen.blit(game.playerSprites[7],game.playerPos)
			#straightMovemt
			elif game.w:
				screen.blit(game.playerSprites[0],game.playerPos)
			elif game.d:
				screen.blit(game.playerSprites[2],game.playerPos)
			elif game.s:
				screen.blit(game.playerSprites[4],game.playerPos)
			elif game.a:
				screen.blit(game.playerSprites[6],game.playerPos)
			#Idle
			elif game.lastMovement == "None":
				screen.blit(game.playerSprites[4],game.playerPos)
			elif game.lastMovement == "UP":
				screen.blit(game.playerSprites[0],game.playerPos)
			elif game.lastMovement == "UP_RIGHT":
				screen.blit(game.playerSprites[1],game.playerPos)
			elif game.lastMovement == "UP_LEFT":
				screen.blit(game.playerSprites[7],game.playerPos)
			elif game.lastMovement == "DOWN":
				screen.blit(game.playerSprites[4],game.playerPos)
			elif game.lastMovement == "DOWN_RIGHT":
				screen.blit(game.playerSprites[3],game.playerPos)
			elif game.lastMovement == "DOWN_LEFT":
				screen.blit(game.playerSprites[5],game.playerPos)
			elif game.lastMovement == "RIGHT":
				screen.blit(game.playerSprites[2],game.playerPos)
			elif game.lastMovement == "LEFT":
				screen.blit(game.playerSprites[6],game.playerPos)

			#bombs
			for b in game.bombs:
				screen.blit(game.spriteDynamite,b.pos)
			
			#animations
			n = -1
			for a in game.animations:
				n += 1
				a.tick()
				if a.type == 2:
					if not a.time > len(game.explosionSprites):
						orgSprite = game.explosionSprites[a.time-1]
						sprite = pygame.transform.scale(orgSprite,(100,100))
						pos = a.pos
						screen.blit(sprite,pos)
					else:
						del game.animations[n]
					

			
		pygame.display.flip()





main()
