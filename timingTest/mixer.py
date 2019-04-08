#mixer.py
#Program Purpose: to use the mixer function to make accurate playback

#import files
import pygame
pygame.init()

#input
chan = 1 #number of sounds
bpm = int(input("Input a BPM: "))

#create the mixer
pygame.mixer.init(frequency= 22050, size= 16, channels = 2, buffer = 4096)

#logic for finding how many seconds between beats
secs = 60 / bpm

#we'll probably have to put this in a for loop
#play
pygame.mixer.Channel.play('kick.wav', -1, secs, 0)

