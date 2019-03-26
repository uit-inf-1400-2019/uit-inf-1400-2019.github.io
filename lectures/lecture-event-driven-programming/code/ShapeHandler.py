# Program: ShapeHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class ShapeHandler(EventHandler):
  def __init__(self, monitor):
    EventHandler.__init__(self)
    self._monitor = monitor

  def handle(self, event):
    if event.getDescription() == 'mouse drag':
      self._monitor.release()

if __name__ == '__main__':
  paper = Canvas()
  checkpoint = Monitor()
  handler = ShapeHandler(checkpoint)

  cir = Circle(10, Point(50,50))
  cir.setFillColor('blue')
  cir.addHandler(handler)
  paper.add(cir)
  square = Square(20, Point(25,75))
  square.setFillColor('red')
  square.addHandler(handler)
  paper.add(square)

  checkpoint.wait()
  paper.setBackgroundColor('green')
