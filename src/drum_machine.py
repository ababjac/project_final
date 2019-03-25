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

#set up window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('UTK Drum Machine')
gameDisplay.fill(gray)

#initialize FPS(frames per second) clock
clock = pygame.time.Clock()

pygame.quit()
quit()
