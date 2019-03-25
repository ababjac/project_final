#timing.py
#Program Purpose: print a character at a time interval
#import files
import pygame
import time
pygame.init()

#print
x = 1
while(x < 7):
	pygame.time.wait(1000)
	print("hello world")
	x = x + 1

print("finished")
