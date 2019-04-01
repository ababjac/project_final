#better_bpm.py
#Program Purpose: plays a sound at the bpm interval that the user inputs

#import files
import pygame
import time
pygame.init()

#create the clock
clock = pygame.time.Clock()
clock.tick(60)

#create the sound
sound = pygame.mixer.Sound('kick.wav')

#ask user for input
bpm = int(input("Input a BPM: "))
bars = int(input("Play sound for ____ bars: "))

#logic for finding how many seconds between beats
secs = 60 / bpm
signature = 4

#loop
b = 0
n = 0
clock.tick(60)
#until enough bars have passed
while(b < (bars*signature)):
	#for every (timePassed % secs), play the sound
	#wait for the amount of time to pass
	clock.tick(60)
	while(pygame.time.Clock.get_time() % secs != 0):
		#do nothing
		n = n + 1		
	#once % is 0, play the sound
	sound.play()
	b = b + 1
	
