#!/usr/bin/env python

import pygame, time
import math
from pygame.locals import *
from sys import exit
from random import randint



pygame.init()
Fps = 30
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
    x = 200+ int( math.floor( 10*math.sin(0.1*(pow(t,2) + 0.2*pow(t,1)))))
    y = int(math.floor(  0.0001*(pow(t,3) + 0.5*pow(t,1))))
    if (x>0 and x < 640 and y > 0 and y<480):
        pixObj[x][y] = White
        pixObj[x][y] = Blue
   
    if (t > 480):
        t = 0
        del pixObj
        pixObj = pygame.PixelArray(screen)
	screen.fill((0,0,0))
       
   # screen.fill((0,255,255))
#  pygame.draw.circle(screen, (0,0,0) ,(circ_x,circ_y), 15)
    pygame.display.update()
    fpsClock.tick(Fps)
