Summary and examples
====================

Lecture 2019-01-29
@ John Markus Bjørndalen

Today's lecture topics
----------------------
- Looking through some of the topics covered by now through example code. 
- Example code 
  - Simple point class
  - Robust point class
  - Television class
  - Fraction class
- Object vs. class
  - class attributes (read vs. assign) 
  - searching for attributes (through examples) 
    - public static void main in Java vs. main() in C. 
  - adding methods to objects at runtime. 


Some of the example code is from Goldwasser's "Object Oriented
Programming in Python" with some minor modifications for Python3 (see
comments in the code). Some of the points below are from Chapter 6 in
that book.

Later: 
- getter/setter (covered in chapter 5 with decorators and properties)
- properties (a much better alternative to getters/setters)
- decorators 



Point class example
-------------------

[Point.py](code/Point.py)


Some points: 
- indentation of methods
- connection between self and object in the code
- `__init__` is the constructor. Executed when a new object is created. 
- Accessor: accesses (or returns) data from an object without modifying the object. 
- Mutator: modifies an object (typically by changing one or more attributes).
- getters and setters typical implementation of accessors and mutators. 

Connection between self and object in the code: 
```python
# when calling this: 
corner.setX(side)      

# corner->self,  side -> val
def setX(self, val):
    ...
```

Using the point class: 
```python
# create a new object corner of type Point
from Point import Point
corner = Point()
corner.setX(8)  # sets _x in corner
corner.setY(6)
```

Improved Point class
--------------------

[PointRobust.py](code/PointRobust.py)

- introduces default values for parameters and shows example code
- adds some useful methods
- overloading operators
- examples of polymorphism (int, float)
- Can not use <3,5> to initialize an object. 

Checking type of objects: 
```python
isinstance(variable, Type) # returns True if variable is of type Type. 
```

Television class
-----------------

[Television.py](code/Television.py)

- Simple class to emulate a TV 
- General principles
  - On-off and mute are both toggle switches
  - All controls only work when the TV is on
  - Volume control goes from 1 to 10 inclusive
  - Channels range from 2-99 inclusive. It wraps around. 
  - Can change channel by entering a channel number. 

Switching values, method 1:
```python
  def jumpPrevChannel(self):
    if self._powerOn:
      incoming = self._channel
      self._channel = self._prevChan
      self._prevChan = incoming
      return self._channel
```

Switching values, flawed:
```python
      self._channel = self._prevChan
      self._prevChan = self._channel
```

Switching values, simpler and more Pythonic version:
```python
  def jumpPrevChannel(self):
    if self._powerOn:
      self._channel, self._prevChan = self._prevChan, self._channel
      return self._channel
```


Fraction class
--------------
* [Fraction.py](code/Fraction.py)
* [Fraction-modified.py](code/Fraction-modified.py) (same code with some comments)
* [Fraction-docstring.py](code/Fraction-docstring.py) (same code with some docstrings)

A fraction consists of two numbers: numerator and denomiator
- Must be in lowest terms 
- Denomiators must be non-negative
- Denomiators must be non-zero
- Method types: 
  - constructor
  - arithmetic operators
  - comparison operators
  - type conversion operators

Television - "Advanced" 
--------------------

* [TelevisionAdvanced.py](code/TelevisionAdvanced.py)

- Adds class level attributes - safer than hard-coded values and an alternative to constants that clutter the module namespace. 
- Methods call support methods in the class to reduce copy and paste code



Class attributes and attribute search
-------------------------------------

This example code illustrates how Python finds an attribute in an object. 
* [classattribs.py](code/classattribs.py)

A more complete example that prints out the attributes of objects and classes. This illustrates the discussion we had about attribute search and method resolution order (MRO) in the previous lecture: 

* [inherit-mechanism.py](code/inherit-mechanism.py)


