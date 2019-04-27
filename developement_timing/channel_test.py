import pygame
import time

pygame.init()

bpm = int(input("Input a BPM: "))

clock = pygame.time.Clock()
last = pygame.time.get_ticks()
secs = int((60 / bpm) * 1000)

sound1 = pygame.mixer.Sound('../sounds2/Clap-1.wav')
sound2 = pygame.mixer.Sound('../sounds2/Hip-Hop-Snare-1.wav')

while(True):
    now = pygame.time.get_ticks()
    if(now - last == secs):
        print("playing 1\n")
        pygame.mixer.find_channel(True).play(sound1)
        pygame.time.wait(secs)

        print("playing 2\n")
        pygame.mixer.find_channel(True).play(sound2)
        last = pygame.time.get_ticks()
