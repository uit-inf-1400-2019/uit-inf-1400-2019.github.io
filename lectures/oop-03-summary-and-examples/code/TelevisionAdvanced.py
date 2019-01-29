# Program: TelevisionAdvanced.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 6 of the book
# Object-Oriented Programming in Python
#

class Television:
  # class-level attributes will be shared by all
  #  JMB: This is only sort-of-true. You can access Television._minVolume, but
  #  JMB: each object can also access _minVolume through self._minVolume. 
  #  JMB: If you assign a new value to self._minValue, it will not change the 
  #  JMB: class value, but it will create a new object attribute called _minVolume that 
  #  JMB: will shadow the shared class-level attribute (we will make this clearer in 
  #  JMB: another example). 
  _minVolume = 0
  _maxVolume = 10
  _minChannel = 2
  _maxChannel = 99
  
  def __init__(self):
    self._powerOn = False
    self._muted = False
    self._volume = (Television._minVolume + Television._maxVolume) // 2
    self._channel = Television._minChannel
    self._prevChan = Television._minChannel

  def togglePower(self):
    self._powerOn = not self._powerOn

  def toggleMute(self):
    if self._powerOn:
      self._muted = not self._muted
      
  def volumeUp(self):
    if self._powerOn:
      if self._volume < Television._maxVolume:
        self._volume += 1
      self._muted = False
      return self._volume
      
  def volumeDown(self):
    if self._powerOn:
      if self._volume > Television._minVolume:
        self._volume -= 1
      self._muted = False
      return self._volume
      
  def channelUp(self):
    if self._powerOn:
      if self._channel == Television._maxChannel:
        goto = Television._minChannel
      else:
        goto = self._channel + 1
      return self.setChannel(goto)                      # rely upon other method

  def channelDown(self):
    if self._powerOn:
      self._prevChan = self._channel
      if self._channel == Television._minChannel:
        goto = Television._maxChannel
      else:
        goto = self._channel - 1
      return self.setChannel(goto)                      # rely upon other method

  def setChannel(self, number):
    if self._powerOn:
      if Television._minChannel <= number <= Television._maxChannel:
        self._prevChan = self._channel                  # record the current value
        self._channel = number
      return self._channel

  def jumpPrevChannel(self):
    return self.setChannel(self._prevChan)

  def __str__(self):
    display = 'Power setting is currently ' + str(self._powerOn) + '\n'
    display += 'Channel setting is currently '+ str(self._channel) + '\n'
    display += 'Volume setting is currently '+ str(self._volume) + '\n'
    display += 'Mute is currently ' + str(self._muted)
    return display


if __name__ == '__main__':
  t = Television()
  t.togglePower()
  print(t)
  print()
  
  t.setChannel(11)
  print(t)
  print()

  t.jumpPrevChannel()
  print(t)
  print()

  t.channelDown()
  print(t)
  print()

  t.jumpPrevChannel()
  print(t)
  print()
