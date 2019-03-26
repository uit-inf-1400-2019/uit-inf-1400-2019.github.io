# Program: ClickAndReleaseHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class ClickAndReleaseHandler(EventHandler):
  def __init__(self):
    EventHandler.__init__(self)
    self._mouseDragged = False

  def handle(self, event):
    if event.getDescription() == 'mouse click':
      self._mouseDragged = False
    elif event.getDescription() == 'mouse drag':
      self._mouseDragged = True
    elif event.getDescription() == 'mouse release':
      if self._mouseDragged:
        print 'Mouse was dragged'
      else:
        print 'Mouse was clicked without dragging'

if __name__ == '__main__':
  paper = Canvas()
  dragDetector = ClickAndReleaseHandler()
  paper.addHandler(dragDetector)
