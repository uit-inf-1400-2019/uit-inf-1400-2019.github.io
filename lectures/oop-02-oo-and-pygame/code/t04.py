#!/usr/bin/env python3

import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME="Chapter03/sushiplate.jpg"
MOUSE_FNAME="Chapter03/fugu.png"
BALL_FNAME="ball.png"

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()

class Ball:
    def __init__(self):
        self.x = 42
        self.y = 300
        self.img = ball_img

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


b1 = Ball()
b2 = Ball()

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
    b1.draw()
    screen.blit(mouse_img, (mx,my))
    b2.draw()
    
    pygame.display.update()
    
        
