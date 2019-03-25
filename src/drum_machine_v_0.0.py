#######################################################################
# Drum Machine                                                        #
#                                                                     #
# CREATORS:                                                           #
### Ashley Babjac                                                     #
### Zoe Babyar                                                        #
#                                                                     #
# PROGRAM DESCRIPTION:                                                #
### Simple Drum-Machine game that allows user to choose sounds and    #
### place them in measure to create a beat                            #
#######################################################################

import pygame
pygame.init()

#screen size constants
display_width = 800
display_height = 600

#color constants
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
red2 = (199,26,7)
blue = (0,0,255)
blue2 = (52,7,199)
green = (0,255,0)
green2 = (19,199,7)
yellow = (255,230,0)
yellow2 = (179,191,22)
purple = (178,49,188)
purple2 = (81,0,115)
pink = (255,0,205)
pink2 = (196,26,134)
orange = (255, 137,0)
orange2 = (166,67,0)
teal = (0,255,255)
teal2 = (0,142,100)
gray = (190,205,210)

#initialize FPS(frames per second) clock
clock = pygame.time.Clock()

#helper function for display_message
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

#prints a message to the game screen
def message_display(text, font, size, location_w, location_h, color):
	Text = pygame.font.SysFont(font, size)
	TextSurf, TextRect = text_objects(text, Text, color)
	TextRect.center = ((location_w, location_h))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

#general button pressing function
def button(msg,x,y,w,h,ic,ac,font_size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        #if click[0] == 1:
            #depends on the click

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",font_size)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#sets up the game display for the user
def set_up_display():
    button("start", display_width/2+50, display_height/15, 50, 50, green, green2, 20)
    button("stop", display_width/2+120, display_height/15, 50, 50, red, red2, 20)

#runs the game
def game_loop():
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			#otherwise do something

		set_up_display()
		pygame.display.update()

		clock.tick(60)

#set up window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('UTK Drum Machine')
gameDisplay.fill(gray)
message_display("Drum Machine", "Helvetica", 60, display_width/4, display_height/10, black)

game_loop()
pygame.quit()
quit()
