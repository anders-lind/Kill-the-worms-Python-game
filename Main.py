import pygame as pygame
from Game import *

game = Game(pygame)
clock = pygame.time.Clock()


def main():
	screen = pygame.display.set_mode((400,300))

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
		#state 2 = in-game pause

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
			screen.blit(game.sheetTerrain,(-128*2,0))
			screen.blit(game.sheetTerrain,(-128*6,128))
			screen.blit(game.sheetTerrain,(-256*4,256))

			if game.movingUp:
				screen.blit(game.sprites[0],(100,50))
			if game.movingRight:
				screen.blit(game.sprites[1],(100,50))
			if game.movingDown:
				screen.blit(game.sprites[2],(100,50))
			if game.movingLeft:
				screen.blit(game.sprites[3],(100,50))
			
		pygame.display.flip()

	else:
		#åbner et vindue, Køres kun en gang
		#pygame.init()
		logo = pygame.image.load("32.png")
		pygame.display.set_icon(logo)
		pygame.display.set_caption("minimal program")

		screen = pygame.display.set_mode((400,300))

		game.started = True
		print("game starting")



main()
