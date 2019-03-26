# Program: NewShapeHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class ShapeHandler(EventHandler):
  def __init__(self):
    EventHandler.__init__(self)
    self._mouseDragged = False
    
  def handle(self, event):
    shape = event.getTrigger()
    if event.getDescription() == 'mouse drag':
      old = event.getOldMouseLocation()
      new = event.getMouseLocation()
      shape.move(new.getX()-old.getX(), new.getY()-old.getY())
      self._mouseDragged = True
    elif event.getDescription() == 'mouse click':
      self._mouseDragged = False
    elif event.getDescription() == 'mouse release':
      if not self._mouseDragged:
        shape.scale(1.5)
    elif event.getDescription() == 'keyboard':
      shape.setFillColor(Color.randomColor())

class NewShapeHandler(EventHandler):
  def __init__(self):
    EventHandler.__init__(self)
    self._shapeCode = 0
    self._handler = ShapeHandler()  # single instance handles all shapes

  def handle(self, event):
    if event.getDescription() == 'mouse click':
      if self._shapeCode == 0:
        s = Circle(10)
      elif self._shapeCode == 1:
        s = Square(10)
      elif self._shapeCode == 2:
        s = Rectangle(15,5)
      elif self._shapeCode == 3:
        s = Polygon(Point(5,5), Point(0,-5), Point(-5,5))
      self._shapeCode = (self._shapeCode + 1) % 4  # advance cyclically

      s.move(event.getMouseLocation().getX(), event.getMouseLocation().getY())
      s.setFillColor('white')
      event.getTrigger().add(s)       # add shape to the underlying canvas
      s.addHandler(self._handler)     # register the ShapeHandler with the new shape

if __name__ == '__main__':
  paper = Canvas(400, 300, 'white', 'Click me!')
  paper.addHandler(NewShapeHandler())   # instantiate handler and register all at once
