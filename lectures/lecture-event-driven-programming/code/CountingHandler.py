# Program: CountingHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class CountingHandler(EventHandler):
  def __init__(self):
    EventHandler.__init__(self)   # call the parent constructor!
    self._count = 0

  def handle(self, event):
    self._count += 1
    print 'Event Triggered. Count:', self._count

if __name__ == '__main__':
  paper = Canvas(100, 100)
  paper.addHandler(CountingHandler())    # activate the handler
