# Program: alarmDemo.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
from CountingHandler import CountingHandler

alarm = Timer(1, True)
stopwatch = CountingHandler()
alarm.addHandler(stopwatch)
print 'Ready...'
alarm.start()                   # yet never stops...
