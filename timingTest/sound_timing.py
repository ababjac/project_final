#sound_timing.py
#Program Purpose: plays a sound at an interval
#import files
import pygame
import time
pygame.init()

#create the sound
sound = pygame.mixer.Sound('kick.wav')

#play the sound every second for 5 seconds
x = 1
while(x < 7):
	pygame.time.wait(1000)
	sound.play()
	x = x + 1
