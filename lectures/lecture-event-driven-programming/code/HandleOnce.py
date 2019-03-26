# Program: HandleOnce.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class HandleOnce(EventHandler):
  def handle(self, event):
    print "That's all folks!!!"
    event.getTrigger().removeHandler(self)

if __name__ == '__main__':
  paper = Canvas()
  oneTime = HandleOnce()
  paper.addHandler(oneTime)
