# Program: Dialog.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Dialog(EventHandler):                          # Note: handles itself!
  """Provides a pop-up dialog box offering a set of choices."""

  def __init__(self, prompt='Continue?', options=('Yes', 'No'),
               title = 'User response needed', width=300, height=100):
    """Create a new Dialog instance but does not yet display it.

    prompt     the displayed string (default 'Continue?')
    options    a sequence of strings, offered as options (default ('Yes', 'No') )
    title      string used for window title bar (default 'User response needed')
    width      width of the pop-up window (default 300)
    height     height of the pop-up window (default 100)
    """
    EventHandler.__init__(self)
    self._popup = Canvas(width, height, 'lightgray', title)
    self._popup.close()                           # hide, for now
    self._popup.add(Text(prompt, 14, Point(width/2,20)))

    xCoord = (width - 70*(len(options)-1))/2      # Center buttons
    for opt in options:
      b = Button(opt, Point(xCoord, height-30))
      b.addHandler(self)                          # we will handle this button ourselves
      self._popup.add(b)
      xCoord += 70

    self._monitor = Monitor()
    self._response = None

  def display(self):
    """Display the dialog, wait for a response and return the answer."""
    self._response = None                         # clear old responses
    self._popup.open()                            # make dialog visible
    self._monitor.wait()                          # wait until some button is pressed
    self._popup.close()                           # then close the popup window
    return self._response                         # and return the user's response

  def handle(self, event):
    """Check if the event was a mouse click and have the dialog return."""
    if event.getDescription() == 'mouse click':
      self._response = event.getTrigger().getMessage()    # label of chosen option
      self._monitor.release()                             # ready to end dialog

if __name__ == '__main__':
  survey = Dialog('How would you rate this interface?',
                  ('good', 'so-so', 'poor'), 'User Survey')

  answer = survey.display()     # waits for user response
  if answer != 'good':
    print "Let's see you do better (see exercises)"
    
