#input_timing.py
#Program Purpose: plays a sound at the interval that the user inputs

#import files
import pygame
import time
pygame.init()

#create the sound
sound = pygame.mixer.Sound('kick.wav')

#ask user for input
secs  = int(input("Play sound every _____ seconds: "))
times = int(input("Play sound ____ times: "))

#play the sound for given input
x = 0
while(x < (times+1)):
	pygame.time.wait(1000*secs)
	sound.play()
	x = x + 1

print("finished");
