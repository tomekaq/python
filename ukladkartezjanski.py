#!/usr/bin/env python

import pygame, time
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
Fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480),0,24)

White = (255,255,255)
Blue = (255,0,0)

pixObj = pygame.PixelArray(screen)

#del pixObj
t = 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    t += 1
    pixObj[200][t] = White
    pixObj[300][t] = Blue
   
    while (t > 480):
        t = 0
        del pixObj
        pixObj = pygame.PixelArray(screen)
	screen.fill((0,0,0))
       
   # screen.fill((0,255,255))
#  pygame.draw.circle(screen, (0,0,0) ,(circ_x,circ_y), 15)
    pygame.display.update()
    fpsClock.tick(Fps)
