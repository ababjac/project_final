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
#                                                                     #
# VERSION: 0.0                                                        #
### Simple Set up of graphics with no logic components                #
#######################################################################


import pygame, time, pygameMenu
pygame.mixer.pre_init(44100, 16, 2, 4096)
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

#sound constants
#hi_hat = pygame.mixer.Sound("../sounds/hihat.wav")
#kick = pygame.mixer.Sound("../sounds/kick.wav")
#rimshot = pygame.mixer.Sound("../sounds/rimshot.wav")
#shaker = pygame.mixer.Sound("../sounds/shaker.wav")
#snare = pygame.mixer.Sound("../sounds/snare.wav")

#set up window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('UTK Drum Machine')
gameDisplay.fill(gray)

#initialize FPS(frames per second) clock
clock = pygame.time.Clock()

#helper function for display_message
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

#prints a message to the game screen
def message_display(text, font, size, location_w, location_h, color, action=None):
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
	#start and stop buttons
    button("start", display_width/2+50, display_height/15, 50, 50, green, green2, 20)
    button("stop", display_width/2+120, display_height/15, 50, 50, red, red2, 20)

	#set up sound buttons
	#thinking about changing sound buttons to drop down menu as well
    button("hi-hat", display_width/50, display_height/6, 50, 50, blue, blue2, 20)
    button("kick", display_width/50+70, display_height/6, 50, 50, blue, blue2, 20)
    button("rimshot", display_width/50+140, display_height/6, 50, 50, blue, blue2, 20)
    button("shaker", display_width/50+210, display_height/6, 50, 50, blue, blue2, 20)
    button("snare", display_width/50+280, display_height/6, 50, 50, blue, blue2, 20)

	#indentation error here?
	#generall area where we will "drag" sounds
	#pygame.draw.rect(gameDisplay, black, (0,250,800,350))
	#where I am thinking of putting the timing drop down menu
	#pygame.draw.rect(gameDisplay, teal, ())

	#set timing menu
	#having trouble getting pop-up menu for timing working
	#refer to https://github.com/ppizarror/pygame-menu for menu commands and examples
	#timer_menu = pygameMenu.Menu(gameDisplay,
	#	dopause=False,
	#	font=pygameMenu.fonts.FONT_NEVIS,
	#	menu_alpha=85,
	#	menu_color=(0, 0, 0),  # Background color
	#	menu_color_title=(0, 0, 0),
	#	menu_height=int(H_SIZE / 2),
	#	menu_width=600,
	#	onclose=PYGAME_MENU_RESET,  # If this menu closes (press ESC) back to main
	#	title='Timer Menu',
	#	title_offsety=5,  # Adds 5px to title vertical position
	#	window_height=H_SIZE,
	#	window_width=W_SIZE
	#	)


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

#title
message_display("Drum Machine", "Helvetica", 60, display_width/4, display_height/10, black)

game_loop()
pygame.quit()
quit()
