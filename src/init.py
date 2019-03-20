#######################################################################
# Piano Game                                                          #
#                                                                     #
# CREATORS:                                                           #
### Ashley Babjac                                                     #
### Zoe Babyar                                                        #
#                                                                     #
# PROGRAM DESCRIPTION:                                                #
### Basic piano game to understand python fundamentals                #
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

#sound constants
A = pygame.mixer.Sound("../wav-piano-sound/wav/a1.wav")
B = pygame.mixer.Sound("../wav-piano-sound/wav/b1.wav")
C = pygame.mixer.Sound("../wav-piano-sound/wav/c1.wav")
C2 = pygame.mixer.Sound("../wav-piano-sound/wav/c2.wav")
D = pygame.mixer.Sound("../wav-piano-sound/wav/d1.wav")
E = pygame.mixer.Sound("../wav-piano-sound/wav/e1.wav")
F = pygame.mixer.Sound("../wav-piano-sound/wav/f1.wav")
G = pygame.mixer.Sound("../wav-piano-sound/wav/g1.wav")

#set up window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('UTK Piano Player')
gameDisplay.fill(gray)

#initialize FPS(frames per second) clock
clock = pygame.time.Clock()

#helper function for display_message
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

#prints a message to the game screen
def message_display(text):
	Text = pygame.font.Font('freesansbold.ttf', 35)
	TextSurf, TextRect = text_objects(text, Text)
	TextRect.center = ((display_width/2, display_height/4))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	#time.sleep(2)

#set up piano board
def orig_piano():
	pygame.draw.rect(gameDisplay, black, (0,250,800,350))
	pygame.draw.rect(gameDisplay, red, (10,275,85,300))
	pygame.draw.rect(gameDisplay, orange, (109,275,85,300))
	pygame.draw.rect(gameDisplay, yellow, (208,275,85,300))
	pygame.draw.rect(gameDisplay, green, (307,275,85,300))
	pygame.draw.rect(gameDisplay, teal, (406,275,85,300))
	pygame.draw.rect(gameDisplay, blue, (505,275,85,300))
	pygame.draw.rect(gameDisplay, purple, (604,275,85,300))
	pygame.draw.rect(gameDisplay, pink, (703,275,85,300))

#general button pressing function
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1:
            play_key(msg)

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#play key based on sound
def play_key(sound):
	if sound == 'A':
		pygame.mixer.Sound.play(A)
	elif sound == 'B':
		pygame.mixer.Sound.play(B)
	elif sound == 'C':
		pygame.mixer.Sound.play(C)
	elif sound == 'C2':
		pygame.mixer.Sound.play(C2)
	elif sound == 'D':
		pygame.mixer.Sound.play(D)
	elif sound == 'E':
		pygame.mixer.Sound.play(E)
	elif sound == 'F':
		pygame.mixer.Sound.play(F)
	elif sound == 'G':
		pygame.mixer.Sound.play(G)

#allows user to press piano keys
def key_logic():
	button('C',10,275,85,300,red,red2)
	button('D',109,275,85,300,orange,orange2)
	button('E',208,275,85,300,yellow,yellow2)
	button('F',307,275,85,300,green,green2)
	button('G',406,275,85,300,teal,teal2)
	button('A',505,275,85,300,blue,blue2)
	button('B',604,275,85,300,purple,purple2)
	button('C2',703,275,85,300,pink,pink2)

#function that runs game
def game_loop():
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			#otherwise do something

		message_display("Click on the Keys to Begin Playing!")
		orig_piano()
		key_logic()
		pygame.display.update()

		clock.tick(60)

#run the game and exit
game_loop()
pygame.quit()
quit()
