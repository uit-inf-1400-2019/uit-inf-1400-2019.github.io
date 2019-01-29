# Program: SimplePoint.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 6 of the book
# Object-Oriented Programming in Python
#
# Edit: Minor modifications for Python 3

class Point:
  def __init__(self):
    self._x = 0
    self._y = 0

  def getX(self):
    return self._x

  def setX(self, val):
    self._x = val

  def getY(self):
    return self._y

  def setY(self, val):
    self._y = val


if __name__ == '__main__':
  a = Point()
  if a.getX() != 0:
    print('New point does not report having x=0.')
  if a.getY() != 0:
    print('New point does not report having y=0.')

  a.setX(5)
  if a.getX() != 5:
    print('Trouble with get/set combination for X-coordinate.')
  
  a.setY(7)
  if a.getY() != 7:
    print('Trouble with get/set combination for Y-coordinate.')

  b = Point()
  b.setX(-8)
  b.setY(-3)
  

  if b.getX() != -8:
    print('Trouble with second point X-coordinate.')
  if b.getY() != -3:
    print('Trouble with second point Y-coordinate.')

  if a.getX() != 5:
    print('Trouble with persistence of first point X-coordinate.')
  if a.getY() != 7:
    print('Trouble with persistence of first point Y-coordinate.')

    
