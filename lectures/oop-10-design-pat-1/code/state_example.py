#!/usr/bin/env python3

"""Simplified state pattern example. 

This is a _very_ simplified implementation of a player or ball moving right and left on a screen. 
We are not implementing any graphics to keep the code short. 

The example is too short to show the real strength of this pattern:
when you have a complicated set of rules and states, it can be simpler
than large functions encoding all possible combinations of rules.

"""
import time

class Moving:
    def __init__(self, player):
        self.player = player
    def process(self):
        pass
    def check(self):
        """Checks if the player needs to change state and updates the state of the player if so."""
        pass

class MovingLeft(Moving):    
    def process(self):
        # Move left
        self.player.pos -= 10
    def check(self):
        # If we have moved too far left, move right. 
        if self.player.pos < self.player.MIN_POS:
            self.player.state = MovingRight(self.player)
            
class MovingRight(Moving):    
    def process(self):
        # Move left
        self.player.pos += 10
    def check(self):
        # If we have moved too far left, move right. 
        if self.player.pos > self.player.MAX_POS:
            self.player.state = MovingLeft(self.player)
        

class Player:
    MIN_POS = 0
    MAX_POS = 50
    
    def __init__(self):
        self.pos = 0
        self.state = MovingRight(self)
        
    def process(self):
        self.state.process()
        
    def check(self):
        self.state.check()

    def __repr__(self):
        return f"<player at {self.pos} in state {self.state.__class__.__name__}>"


player = Player()

for i in range(30):
    player.process()
    player.check()
    print(player)
    time.sleep(1)
