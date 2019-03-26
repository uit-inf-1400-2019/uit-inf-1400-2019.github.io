#!/usr/bin/env python

# The main problem with the previous version is sharing state with the
# handler. Using global variables is possible, but maybe not the best
# option.
# 
# An alternative is to create event handlers that can receive state when
# created. 
# 
#
# one option:
# 
#  def foo_handler_creator(event, state):
#      def handler(event, state=state):
#          pass # whatever is done inside the handler
#      return handler
#
# Second option:
#
# class handler(EventHandler):
#     def __init__(self, state....)
#        ....
#     def handle(self, event):
#        pass # handling the event
#
# The problem with that system is that the event dispatcher
# must either be changed to check for EventHandler objects
# and call hander.handle(event) on the given event, or we will have
# problems with combining function event handlers with object event handlers.
# 
# A better option might be to do the following:
# class handler(EventHandler): 
#     def __init__(self, state....)
#        ....
#     def __call___(self, event):
#        pass # handling the event
# 
# An object with a __call__ method can be used as a function:
# 
# f = handler(state...)
# 
# f(event)
#
# This way, the same event dispatcher can be used to handle both event
# handler functions and objects, and state can be kept in the objects. 
#


import pygame
import time
import math
from pygame.locals import *
import random


pygame.init()

screen_res_x = 640
screen_res_y = 480

screen = pygame.display.set_mode((screen_res_x, screen_res_y), 0, 32)

# ------------------------------------------------------------
# 
# Some objects to display
# 
# ------------------------------------------------------------

bgimage = pygame.image.load("Chapter03/sushiplate.jpg")
background = bgimage.convert()
fish = pygame.image.load("Chapter03/fugu.png").convert_alpha()

class Ball:
    def __init__(self):
        self.img = pygame.image.load("ball.png").convert_alpha()
        self.x = random.random() * 640
        self.y = random.random() * 480

        self.dir_x = 1
        self.dir_y = 1
        self.speed = 120  # hvor mange pixels per sekund

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
        self.speed = 50 + random.random() * 120
        self.img = pygame.image.load("spider.png").convert_alpha()

    def change_speed(self, new_speed):
        self.speed = new_speed
        self.speed = min(50, self.speed)
        self.speed = max(500, self.speed)
        

    def move(self, time_passed_seconds):
        #self.change_speed(random.random() * 500)
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
        # NB: This simple code assumes only a single handler 
        # for each type
        self.__handlers[etype] = handler
    def dispatch(self, event):
        if event.type in self.__handlers:
            self.__handlers[event.type](event)
        else:
            print("Unknown event type", event.type, pygame.event.event_name(event.type), event)
            
def mouse_motion_handler(event):
    print("Moving mouse", event.pos, event.rel, event)
    pass

def timer_event_handler(event):
    print("Timer ping", event)

dispatcher = Dispatcher()
dispatcher.register_handler(MOUSEMOTION, mouse_motion_handler)
dispatcher.register_handler(USEREVENT+1, timer_event_handler)

# her deler vi state med handler
class FooHandler:
    def __init__(self):
        self.var = 42
    def handler(self, event):
        print("foohandler - var =", self.var, "event=", event)

foohandler = FooHandler()
dispatcher.register_handler(USEREVENT+1, foohandler.handler)

pygame.time.set_timer(USEREVENT+1, 2000)

# Make the program quit after 10 seconds by having a timer post a QUIT event
# after 10 seconds. 
# pygame.time.set_timer(QUIT, 10000)


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
        if event.type == QUIT:
            finished = True
        else:
            dispatcher.dispatch(event)

    time_passed = clock.tick(1000)
    time_passed_seconds = time_passed / 1000.0

    for obj in objects:
        obj.move(time_passed_seconds)

    screen.blit(background, (0,0))

    for obj in objects:
        obj.draw()

    x,y = pygame.mouse.get_pos() 
    fish_x = x - fish.get_width() / 2
    fish_y = y - fish.get_height() / 2
    
    screen.blit(fish, (fish_x, fish_y))
    
    pygame.display.update()

pygame.quit()
