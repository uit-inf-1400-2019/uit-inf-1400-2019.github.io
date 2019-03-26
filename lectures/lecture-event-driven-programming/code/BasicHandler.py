# Program: BasicHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class BasicHandler(EventHandler):
  def handle(self, event):
    print 'Event Triggered'

if __name__ == '__main__':
  simple = BasicHandler()
  paper = Canvas()
  paper.addHandler(simple)
