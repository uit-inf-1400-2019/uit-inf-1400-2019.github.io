# Program: MastermindGUI.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 15 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
from Mastermind import Mastermind
from GraphicsOutput import GraphicsOutput
from Dialog import Dialog
from Pattern import Pattern

class MastermindGUI(GraphicsOutput):
  """Class to provide full graphical interface to Mastermind"""
  def queryLengthOfPattern(self):
    """Ask the user how many pegs in the secret pattern."""
    dialog = Dialog('How many pegs are in the secret?', 
                    ['4', '6', '8', '10'], 'Length of pattern')
    return int(dialog.display())
  
  def queryNumberOfColors(self):
    """Ask the user how many colors to use for secret pattern."""
    inputOptions = []
    for i in range(2,len(self._colorNames)+1):
      inputOptions.append(str(i))
    dialog = Dialog('How many colors are available?', 
                    inputOptions, 'Number of color', 500)
    self._numberOfColors = int(dialog.display())
    return self._numberOfColors
  
  def queryNumberOfTurns(self):
    """Ask the user maximum number of guesses to be allowed."""
    dialog = Dialog('How many turns are allowed?', 
                    ['5', '10', '15', '20'], 'Number of turns')
    return int(dialog.display())
  
  def queryNewGame(self):
    """Offer the user a new game. Return True if accepted, False otherwise."""
    dialog = Dialog('Would you like to play again?', 
                    ['Yes', 'No'], 'Again?')
    return dialog.display() == 'Yes'

  def _setupBackground(self):
    """Draws the backgound to the graphics canvas."""    
    block = Rectangle(4*self._lengthOfPattern*self._pegRadius, 4*self._pegRadius)
    block.move((1 + 2*self._lengthOfPattern)*self._pegRadius, 3*self._pegRadius)
    block.setFillColor('brown')
    block.setDepth(60)
    self._canvas.add(block)

    self._holes = []
    for row in range(self._maxNumberOfTurns):
      self._holes.append( [None] * self._lengthOfPattern )
      for col in range(self._lengthOfPattern):
        self._holes[row][col] = Circle(self._pegRadius/2, self._getCenterPoint(row,col))
        self._holes[row][col].setFillColor('black')
        self._canvas.add(self._holes[row][col])
    self._canvas.refresh()
  
  def enterGuess(self):
    """Have user enter guess and return response."""    
    self._guess = Pattern(self._lengthOfPattern)
    
    handlers = []                            # Turn on handlers for each of the pegs
    self._pegEntered = [False] * self._lengthOfPattern
    for i in range(self._lengthOfPattern):
      handlers.append(PegHandler(self, i))
      self._holes[self._currentTurnNum][i].addHandler(handlers[i])

    button = Button('Guess')                 # Create a button with a handler
    button.move((4*self._lengthOfPattern+3.5)*self._pegRadius,
                (4*(self._maxNumberOfTurns-self._currentTurnNum-1)+7)*self._pegRadius)
    button.addHandler(ButtonHandler(self))
    self._canvas.add(button)
    self._canvas.refresh()

    self._finalized = Monitor()                   
    self._finalized.wait()                   # Wait for guess to be finalized

    for i in range(self._lengthOfPattern):   # Remove the holes
      self._holes[self._currentTurnNum][i].removeHandler(handlers[i])
      self._canvas.remove(self._holes[self._currentTurnNum][i])
    self._canvas.remove(button)              # Remove the "guess" button

    return self._guess

class PegHandler(EventHandler):
  """Manager for an overlay to select a peg color."""
  def __init__(self, gui, peg):
    """Create a new PegHandler instance.
    
    gui  reference to the user interface
    peg  integer indicating which peg is being set
    """
    EventHandler.__init__(self)
    self._gui = gui
    self._peg = peg
    self._monitor = Monitor()

  def handle(self, event):
    """Display options when the user mouse clicks on a peg."""
    if event.getDescription() == 'mouse click':
      hole = event.getTrigger()
      hole.removeHandler(self)               # disable handler until we are done

      box = Layer()                          # Create a box of options and display
      box.move(hole.getReferencePoint().getX(), hole.getReferencePoint().getY())
      box.setDepth(0)
      self._gui._canvas.add(box)

      numColumns = (1 + self._gui._numberOfColors) // 2
      r = 0.6 * self._gui._pegRadius
      background = Rectangle(r*2.5*numColumns, r*5)
      background.move(background.getWidth()/2, background.getHeight() / 2)
      background.setFillColor('light gray')
      background.setDepth(100)
      box.add(background)

      for i in range(2):
        for j in range(numColumns):
          if numColumns*i + j < self._gui._numberOfColors:
            peg = Circle(r, Point(r*(2.5*j+1.25), r*(2.5*i+1.25)))
            peg.setFillColor(self._gui._colorNames[numColumns*i + j])
            peg.addHandler(ChoiceHandler(self, numColumns*i + j))
            box.add(peg)
      self._gui._canvas.refresh()         # Redisplay gameboard with the choices
      self._monitor.wait()                # Wait for a choice to be selected
      self._gui._canvas.remove(box)
      self._gui._canvas.refresh()         # Redisplay gameboard without choices
      hole.addHandler(self)               # Allow user to change her choice

class ChoiceHandler(EventHandler):
  """Handler class for the selection of a colored peg."""
  def __init__(self, pegHandler, colorNum):
    """Create a new instance."""
    EventHandler.__init__(self)
    self._pegHand = pegHandler
    self._color = colorNum

  def handle(self, event):
    """Set the choice of color and close the popup."""
    if event.getDescription() == 'mouse click':
      gui = self._pegHand._gui
      gui._guess.setPegColor(self._pegHand._peg, self._color)
      hole = gui._holes[gui._currentTurnNum][self._pegHand._peg]
      hole.setRadius(gui._pegRadius)
      hole.setFillColor(gui._colorNames[self._color])
      gui._pegEntered[self._pegHand._peg] = True
      self._pegHand._monitor.release()

class ButtonHandler(EventHandler):
  """Handler for user submitting a guess."""
  def __init__(self, gui):
    """Create a new ButtonHandler."""
    EventHandler.__init__(self)
    self._gui = gui

  def handle(self, event):
    """Release the monitor waiting for a guess."""
    if event.getDescription() == 'mouse click':
      if False not in self._gui._pegEntered:          # all pegs have been chosen
        self._gui._finalized.release()

if __name__ == '__main__':
  palette = ('Red', 'Blue', 'Green', 'White', 'Yellow', 'Orange',
             'Purple', 'Turquoise')
  interface = MastermindGUI(palette)
  game = Mastermind(interface, interface)
