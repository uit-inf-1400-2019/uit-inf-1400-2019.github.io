# Program: RotationHandler.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class RotationHandler(EventHandler):
  def __init__(self, shape):
    self._shape = shape

  def handle(self, event):
    self._shape.rotate(1)

paper = Canvas(100,100)
sampleCircle = Circle(20, Point(50,20))
sampleCircle.adjustReference(0,30)
paper.add(sampleCircle)

alarm = Timer(0.1, True)
rotator = RotationHandler(sampleCircle)
alarm.addHandler(rotator)
alarm.start()
