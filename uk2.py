#!/usr/bin/env python

import pygame, time
import math
from pygame.locals import *
from sys import exit
from random import randint



def toScreen(x,y):
    return (320 - x,240 - y)

def Draw(x,y,a=0):
    if (a == 1):
        (y,x) = toScreen(x+ int(math.floor(-math.sin(t))),y*int(math.floor( t )))
    (x,y) = toScreen(x+ int(math.floor(-math.sin(t))),y*int(math.floor( t )))
    
    if (x>0 and x < 640 and y > 0 and y<480):
        pixObj[x][y] = Blue
      #  pixObj[x][y] = Red

pygame.init()
Fps = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480),0,24)

White = (255,255,255)
Red = (255,0,0)
Blue = (0,255,255)
pixObj = pygame.PixelArray(screen)

#del pixObj
t = 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    t += 1
    (c,v) = toScreen(0,0)
    pixObj[c][v] = White


    for i in range (-320+1,320):
        (j,k) = toScreen(i,0)
        pixObj[j][k] = White

    for i in range (-240+1,240):
        (j,k) = toScreen(0,i)
        pixObj[j][k] = White

    for i in range(-80,80):
        Draw(i*10,1)
        Draw(i*10,-1)
        Draw(i*10,1,1)
        Draw(i*10,-1,1)
    if (t > 480):
        t = 0
        del pixObj
        pixObj = pygame.PixelArray(screen)
	screen.fill((0,0,0))
       
   # screen.fill((0,255,255))
#  pygame.draw.circle(screen, (0,0,0) ,(circ_x,circ_y), 15)
    pygame.display.update()
    fpsClock.tick(Fps)
