#mixer.py
#Program Purpose: to use the mixer function to make accurate playback

#import files
import pygame
pygame.init()

#input
chan = 1 #number of sounds
bpm = int(input("Input a BPM: "))

#create the mixer
pygame.mixer.init(frequency= 22050, size= 16, channels = 1, buffer = 1024)

#logic for finding how many seconds between beats
secs = (60 / bpm) * 1000

#number of sounds
pygame.mixer.set_num_channels(1);

#play
pygame.mixer.Channel(0).play(pygame.mixer.Sound('kick.wav'), -1, int(secs), 0)

