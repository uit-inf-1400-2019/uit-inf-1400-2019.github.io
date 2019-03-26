# Program: Stopwatch.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Stopwatch(Layer, EventHandler):
  """Display a stopwatch with start, stop, and reset buttons."""
  
  def __init__(self):
    """Create a new Stopwatch instance."""    
    Layer.__init__(self)
    EventHandler.__init__(self)

    border = Rectangle(200,100)
    border.setFillColor('white')
    border.setDepth(52)
    self._display = Text('0:00', 36, Point(0,-20))

    self._start = Square(40, Point(-60,25))
    self._stop  = Square(40, Point(0,25))
    self._reset = Square(40, Point(60,25))
    buttons = [self._start, self._stop, self._reset]
    for b in buttons:
      b.setFillColor('lightgray')
      b.setDepth(51)               # in front of border, but behind icons

    self._startIcon = Polygon( Point(-70,15), Point(-70,35), Point(-50,25) )
    self._startIcon.setFillColor('black')
    self._stopIcon = Square(20, Point(0,25))
    self._stopIcon.setFillColor('black')
    self._resetIcon = Text('00', 24, Point(60,25))
    buttons.extend([self._startIcon, self._stopIcon, self._resetIcon])
    for obj in buttons + [self._display, border]:
      self.add(obj)                # add to the layer

    self._clock = 0                # measured in seconds
    self._timer = Timer(1, True)
    for active in [self._timer] + buttons:
      active.addHandler(self)      # we will handle all such events

  def getTime(self):
    """Convert the clock's time to a string with minutes and seconds."""
    min = str(self._clock // 60)
    sec = str(self._clock % 60)
    if len(sec) == 1:
      sec = '0'+sec                # pad with leading zero
    return min + ':' + sec

  def handle(self, event):
    """Deal with each of the possible events.
    
    The possibilities are timer events for advancing the clock,
    and mouse clicks on one of the buttons.
    """
    if event.getDescription() == 'timer':
      self._clock += 1
      self._display.setMessage(self.getTime())
    elif event.getDescription() == 'mouse click':
      if event.getTrigger() in (self._start, self._startIcon):
        self._timer.start()
      elif event.getTrigger() in (self._stop, self._stopIcon):
        self._timer.stop()
      else:  # must have been self._reset or self._resetIcon
        self._clock = 0
        self._display.setMessage(self.getTime())

if __name__ == '__main__':
  paper = Canvas(400,400)
  clock = Stopwatch()
  paper.add(clock)
  clock.move(200,200)
