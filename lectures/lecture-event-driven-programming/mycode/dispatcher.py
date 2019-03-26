#!/usr/bin/env python

"""Dispatcher example. 

* Demonstrates how to make a simple event dispatcher and how to use it.

* Shows some alternatives for creating event handlers that can be registered with the
  dispatcher.

* Shows how the dispatcher can be used with PyGame events and how to add new event types
  to PyGame.

"""

import pygame
import time
import math
from pygame.locals import *
import random

pygame.init()

SCREEN_RES_X = 640
SCREEN_RES_Y = 480
screen = pygame.display.set_mode((SCREEN_RES_X, SCREEN_RES_Y), 0, 32)


# ------------------------------------------------------------
# 
# Some objects to display
# 
# ------------------------------------------------------------

bgimage = pygame.image.load("Chapter03/sushiplate.jpg")
background = bgimage.convert()
fish = pygame.image.load("Chapter03/fugu.png").convert_alpha()

class Ball:
    BASE_BALL_SPEED = 120 # hvor mange pixels per sekund
    
    def __init__(self):
        self.img = pygame.image.load("ball.png").convert_alpha()
        self.x = random.random() * SCREEN_RES_X
        self.y = random.random() * SCREEN_RES_Y

        self.dir_x = 1
        self.dir_y = 1
        self.speed = self.BASE_BALL_SPEED

    def move(self, time_passed_seconds):
        dist = time_passed_seconds * self.speed

        self.x = self.x + dist * self.dir_x
        self.y = self.y + dist * self.dir_y

        if self.x < 0:
            self.dir_x = 1
        if self.y < 0:
            self.dir_y = 1
        if self.x > screen.get_width():
            self.dir_x = -1
        if self.y > screen.get_height():
            self.dir_y = -1 

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

class SuperBall(Ball):
    def __init__(self):
        Ball.__init__(self)
        self.speed = 50 + random.random() * self.BASE_BALL_SPEED
        self.img = pygame.image.load("spider.png").convert_alpha()

    def change_speed(self, new_speed):
        self.speed = new_speed
        self.speed = min(50, self.speed)
        self.speed = max(500, self.speed)

    def move(self, time_passed_seconds):
        self.change_speed(math.sin(time.time()) * 500)
        Ball.move(self, time_passed_seconds)


# ------------------------------------------------------------
# 
# Dispatch/event handler  code
# 
# ------------------------------------------------------------

class Dispatcher:
    def __init__(self):
        self.__handlers = {}

    def register_handler(self, etype, handler):
        """Register a callable object (function, method or object with __call__ method) that
        will be called for 'etype' events. 
        The event handler will receive the event as a parameter. 
        NB: This simple code assumes only a single handler 
        for each type. 
        """
        self.__handlers[etype] = handler
    def dispatch(self, event):
        if event.type in self.__handlers:
            self.__handlers[event.type](event)
        else:
            print("Unknown event type", event.type, pygame.event.event_name(event.type), event)
            
def mouse_motion_handler(event):
    print("Mouse move:", event.pos, event.rel, event)
    pass

def timer_event_handler(event):
    print("Timer ping", event)

def quit_handler(event):
    global finished
    print("Finished")
    finished = True

FOOEVENT = USEREVENT+1
dispatcher = Dispatcher()
dispatcher.register_handler(MOUSEMOTION, mouse_motion_handler)
dispatcher.register_handler(FOOEVENT, timer_event_handler)
dispatcher.register_handler(QUIT, quit_handler)

# every other second, we let a timer fire a FOOEVENT
pygame.time.set_timer(FOOEVENT, 2000)

# Make the program quit after 10 seconds by having a timer post a QUIT event
# after 10 seconds. 
# pygame.time.set_timer(QUIT, 10000)


class FooHandler:
    """
    Example handler object that can hold state.
    There are two ways of calling this handler from the dispatcher:
      1) pass the object itself and the dispatcher will invoke the
         __call__ method when trying to use the object as a function.
      2) pass the handler method from the object to the dispatcher.
         Python will keep the binding between the method and the object(self),
         so the dispatcher can call the method as if it was a function.
    """
    def __init__(self, var = 42):
        self.var = var
        
    def handler(self, event):
        """Event handler option 1.
        Pass this method to the dispatcher when registering the event type.""" 
        print("foohandler option 1 - var =", self.var, "event=", event)

    def __call__(self, event):
        """Event handler option 2.
        Pass the object itself to the dispatcher when registering the event type.
        """
        print("foohandler option 2 - var =", self.var, "event=", event)

foohandler = FooHandler()
#dispatcher.register_handler(FOOEVENT, foohandler.handler)
dispatcher.register_handler(FOOEVENT, foohandler)



# ------------------------------------------------------------
#
# Main loop
# 
# ------------------------------------------------------------

clock = pygame.time.Clock()

objects = [
    Ball(),
    Ball(),
    SuperBall()
    ]

finished = False
while not finished:
    foohandler.var += 1
    for event in pygame.event.get():
        dispatcher.dispatch(event)

    time_passed = clock.tick(1000)
    time_passed_seconds = time_passed / 1000.0

    for obj in objects:
        obj.move(time_passed_seconds)

    screen.blit(background, (0,0))

    for obj in objects:
        obj.draw()

    # draw "cursor" object
    x,y = pygame.mouse.get_pos() 
    fish_x = x - fish.get_width() / 2
    fish_y = y - fish.get_height() / 2
    screen.blit(fish, (fish_x, fish_y))
    
    pygame.display.update()

pygame.quit()
