# Program: CircleDrawHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class CircleDrawHandler(EventHandler):
  def handle(self, event):
    if event.getDescription() == 'mouse click':
      c = Circle(5, event.getMouseLocation())
      event.getTrigger().add(c)

if __name__ == '__main__':
  paper = Canvas(100, 100)
  handler = CircleDrawHandler()
  paper.addHandler(handler)
