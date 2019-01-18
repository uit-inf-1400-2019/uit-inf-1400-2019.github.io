#!/usr/bin/env python3

import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME="Chapter03/sushiplate.jpg"
MOUSE_FNAME="Chapter03/fugu.png"

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        print("Fikk quit-event") 
        exit()

    #lst= pygame.mouse.get_pos()
    #x = lst[0]
    #y = lst[1]
    # enklere: 
    x,y = pygame.mouse.get_pos()
    mx = x - mouse_size_x / 2
    my = y - mouse_size_y / 2

    screen.blit(background, (0,0))
    screen.blit(mouse_img, (mx,my))
    
    pygame.display.update()
    
        
