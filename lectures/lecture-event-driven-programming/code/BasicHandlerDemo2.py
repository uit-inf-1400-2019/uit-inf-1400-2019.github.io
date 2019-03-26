# Program: BasicHandlerDemo2.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
from BasicHandler import BasicHandler

sun = Circle(30, Point(50,50))
sun.setFillColor('yellow')
paper = Canvas()
paper.add(sun)
simple = BasicHandler()
sun.addHandler(simple)            # register directly with the sun
