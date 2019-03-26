# Program: KeyHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class KeyHandler(EventHandler):
  def __init__(self, textObj):
    EventHandler.__init__(self)
    self._textObj = textObj

  def handle(self, event):
    if event.getDescription() == 'keyboard':
      self._textObj.setMessage(self._textObj.getMessage() + event.getKey())
    elif event.getDescription() == 'mouse click':
      self._textObj.setMessage('')   # clear the text

if __name__ == '__main__':
  paper = Canvas()
  textDisplay = Text('', 12, Point(100,100))  # empty string initially
  paper.add(textDisplay)
  echo = KeyHandler(textDisplay)
  paper.addHandler(echo)
