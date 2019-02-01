import pygame as pg
from pygame import Vector2
import cng

class Ball():
    def __init__(self, screen, color, x, y, radius, speed):

        # Screen is the same screen the manager uses. 
        self.screen = screen

        # We set a color for the ball.
        self.color = color

        # Since tuples are mutable objects (we can't change their values),
        # We instead create a vector-object.
        self.start_pos = Vector2(x, y)

        # We set a radius to determine it's size.
        self.radius = radius

        # The speed determines how many pixels the object will move between each frame.
        self.speed = speed
        
    def draw(self):
        # This method calls Pygames draw.circle()-method and uses the attributes from the init.
        pg.draw.circle(self.screen, self.color, (int(self.start_pos.x), int(self.start_pos.y)), self.radius)

        # Note that the position-vector coordinates are casted to integers to avoid a type-error, as they are 
        # casted to floating point numbers in the vector2-class.
    
    def move(self):
        # This method changes the positional coordinates of the ball. 
        # Here, you can try to experiment for yourself if you want to,
        # and try to make the ball move in different directions.
        self.start_pos.x += self.speed
        self.start_pos.y += self.speed 
        


class Game():
    def __init__(self):

        # When working with Pygame, we have to initialize it before working with it.
        pg.init()

        # We set the display, and chose a resolution
        self.screen = pg.display.set_mode(cng.SCREEN_RES)

        # Then we create a clock-object. 
        # This is usually done to keep the framerate cosistent, but will be used later.
        self.clock = pg.time.Clock()

        # We create the objects that we want to use in the loop.
        self.player1 = Ball(self.screen, cng.PLAYER_1_COLOR, cng.PLAYER_1_POS_X, cng.PLAYER_1_POS_Y, cng.PLAYER_1_RADIUS, cng.PLAYER_1_SPEED)
        self.player2 = Ball(self.screen, cng.PLAYER_2_COLOR, cng.PLAYER_2_POS_X, cng.PLAYER_2_POS_Y, cng.PLAYER_2_RADIUS, cng.PLAYER_2_SPEED)

        # Lastly, we call the gameloop.
        self.gameloop()

    def gameloop(self):
        """ Main loop of the game """

        # What you see above (""" some text """) is called a docstring.
        # It explains the purpose of the method/function.
        # There should generally be one for every function.


        # Below is the main loop
        while True: 
            # One cycle in the loop is equivalent to one frame.

            self.event()

            self.draw_objects()
            self.move_objects()

            self.update_display()
    
    def update_display(self):
        """ Refreshes the screen, and keeps the framerate stable """

        # The display.update() Updates the screen, making the new frame replace the old one. 
        pg.display.update()
        
        # clock.tick sets a framerate for the game.
        # This is to make the game run at a stable fps 
        self.clock.tick(cng.FRAMERATE) 
    
    def draw_objects(self):
        """ Draws all objects """

        # Here we simply draw all the objects which the game-class want to draw.
        self.player1.draw()
        self.player2.draw()

        # In cases where there are many objects, it is generally better to place then
        # in a list, and iterate over it, calling draw on every object. 
        # This would make the code short and consise.
    
    def move_objects(self):
        """ Moves all objects """

        # This function has the same general purpose as draw_objects, only
        # That the goal is to move the objects instead.
        self.player1.move()
        self.player2.move()

        # Again, using a list is better in cases with many objects.
        
    def event(self):

        # Here, we use screen.fill to chose our background color
        self.screen.fill(cng.BACKGROUND_COLOR)
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                exit()

