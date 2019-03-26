# Program: TallyHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class TallyHandler(EventHandler):
  def __init__(self, textObj):
    EventHandler.__init__(self)
    self._count = 0
    self._text = textObj
    self._text.setMessage(str(self._count))  # reset to 0

  def handle(self, event):
    self._count += 1
    self._text.setMessage(str(self._count))

if __name__ == '__main__':
  paper = Canvas(100, 100)
  score = Text('', 12, Point(40,40))
  paper.add(score)
  referee = TallyHandler(score)       # create the handler
  paper.addHandler(referee)           # activate the handler
