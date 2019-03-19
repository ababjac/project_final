#######################################################################
# Drum Machine                                                        # 
#                                                                     #
# CREATORS:                                                           #
### Ashley Babjac                                                     #
### Zoe Babyar                                                        #
#                                                                     #
# PROGRAM DESCRIPTION:                                                #
### ?                                                                 #
#######################################################################

import pygame
pygame.init()

#screen size constants
display_width = 1200
display_height = 800

#color constants
black = (0,0,0)
white = (255, 255, 255)

#set up window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('UTK Drum Machine')

#initialize FPS(frames per second) clock
clock = pygame.time.Clock()

#helper function for display_message
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

#prints a message to the game screen
def message_display(text):
	Text = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, Text)
	TextRect.center = ((display_width/2, display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)

#function that runs game
def game_loop():
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			#otherwise do something

	pygame.display.update()
	clock.tick(60)

#run the game and exit
game_loop()
pygame.quit()
quit()
