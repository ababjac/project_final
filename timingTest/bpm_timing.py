#bpm_timing.py
#Program Purpose: plays a sound at the bpm interval that the user inputs

#import files
import pygame
import time
pygame.init()

#create the sound
sound = pygame.mixer.Sound('kick.wav')

#ask user for input
bpm = int(input("Input a BPM: "))
bars = int(input("Play sound for ____ bars: "))

#logic for finding how many seconds between beats
secs = 60 / bpm
signature = 4

#play the sound for the given input at every 1/4 note
b = 0
while(b < bars):
	b = b + 1
	s = 0
	while(s < signature):
		pygame.time.wait(int(1000*secs))
		sound.play()
		s = s + 1
	#end of bar

#done with user-input number of bars
	

