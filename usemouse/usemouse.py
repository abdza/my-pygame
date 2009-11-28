#!/usr/bin/env python

import pygame
import sys

pygame.init()

size = width, height = 640,480

screen = pygame.display.set_mode(size)
mountain = pygame.image.load("mountain.pcx")
crosshair = pygame.image.load("crosshair.png")
pygame.mouse.set_visible(False)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    mousex,mousey = pygame.mouse.get_pos()
    screen.blit(mountain,(0,0))
    screen.blit(crosshair,(mousex,mousey))
    pygame.display.flip()
