#!/usr/bin/env python3

import pygame
import random

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
        self.y = 50
        self.img = ball_img
        self.speed = [50 + random.random() * 60,
                      50 + random.random() * 60]

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x > SCREEN_X:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y:
            self.speed[1] = -abs(self.speed[1])
        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

class Circle:
    def __init__(self):
        self.x = 500
        self.y = 300
        self.speed = [50 + random.random() * 160,
                      50 + random.random() * 160]
        self.col = (255, 255, 0)
        self.size = 40 # diameter

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x > SCREEN_X:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y:
            self.speed[1] = -abs(self.speed[1])
        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)),
                           round(self.size / 2))

        
objs = [
    Ball(), 
    Ball(), 
    Ball(), 
    Ball(),
    Circle(), 
    ]

clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events: 
        if event.type == pygame.QUIT:
            print("Fikk quit-event") 
            exit()

    time_passed = clock.tick(30) / 1000.0

    #lst= pygame.mouse.get_pos()
    #x = lst[0]
    #y = lst[1]
    # enklere: 
    x,y = pygame.mouse.get_pos()
    mx = x - mouse_size_x / 2
    my = y - mouse_size_y / 2

    for o in objs: 
        o.move(time_passed)

    screen.blit(background, (0,0))
    for o in objs: 
        o.draw()
    screen.blit(mouse_img, (mx,my))
    
    pygame.display.update()
    
        
