#!/usr/bin/env python

import pygame
import sys

pygame.init()

size = width, height = 640,480

screen = pygame.display.set_mode(size)
mountain = pygame.image.load("mountain.pcx")
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(mountain,(0,0))
    pygame.display.flip()
