import pygame

pygame.init()

bpm = int(input("Input a BPM: "))

clock = pygame.time.Clock()
last = pygame.time.get_ticks()
secs = int((60 / bpm) * 1000)
sound = pygame.mixer.Sound('../sounds2/Clap-1.wav')

while(True):
    now = pygame.time.get_ticks()
    if(now - last >= secs):
        pygame.mixer.find_channel(True).play(sound)
        last = now
