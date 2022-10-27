# RGB led class for the ledRGBMain.py program

import RPi.GPIO as GPIO


class LedRGB():
  def __init__(self, redPin:int, greenPin:int, bluePin:int, inverted:bool = False):

    # Set the GPIO mode to board
    self.GPIO = GPIO
    self.GPIO.setmode(GPIO.BOARD) # Select pin number mode 

    # If the led is inverted then the behavior is reversed
    self.__isInverted = inverted

    # Set the pin number and RGB values as privates atributes
    self.__redPin = redPin
    self.__r = 0
    self.__redInt = self.initColor(self.__redPin)

    self.__greenPin = greenPin
    self.__g = 0
    self.__greenInt = self.initColor(self.__greenPin)

    self.__bluePin = bluePin
    self.__b = 0
    self.__blueInt = self.initColor(self.__bluePin)

  def on(self,r:int, g:int, b:int):
    """Turn on the RGB values"""
    self.setR(r)
    self.setG(g)
    self.setB(b)

  def off(self):
    """Turn off the RGB value"""
    # Set the led values to (0,0,0) then the led is off
    self.on(0,0,0)

  def setR(self, r:int):
    """Set the red value"""
    # Check if the value is in range
    if r > 255: r = 255
    if r < 0: r = 0
    self.__r = r

    # Change the value from the range 255-0 to 100-0
    if r == 0:
      rInt = 0
    else:
      rInt = int((r*100)/255)

    # If the led is inverted, revert the value
    if self.__isInverted:
      rInt = 100 - rInt 

    # Change the red value
    self.__redInt.ChangeDutyCycle(rInt)
  
  def setG(self, g:int):
    """Set the green value"""
    # Check if the value is in range
    if g > 255: g = 255
    if g < 0: g = 0
    self.__g = g

    # Change the value from the range 255-0 to 100-0
    if g == 0:
      gInt = 0
    else:
      gInt = int((g*100)/255)

    # If the led is inverted, revert the value
    if self.__isInverted:
      gInt = 100 - gInt 

    # Change the green value
    self.__greenInt.ChangeDutyCycle(gInt)

  def setB(self, b:int):
    """Set the blue value"""
    # Check if the value is in range
    if b > 255: b = 255
    if b < 0: b = 0
    self.__b = b

    # Change the value from the range 255-0 to 100-0
    if b == 0:
      bInt = 0
    else:
      bInt = int((b*100)/255)

    # If the led is inverted, revert the value
    if self.__isInverted:
      bInt = 100 - bInt 


    # Change the blue value
    self.__blueInt.ChangeDutyCycle(bInt)
  
  def initColor(self,pin:int):
    """Initialice the color pin"""
    GPIO.setup(pin, GPIO.OUT) # Change pin mode to output
    pinInt = self.GPIO.PWM(pin,100)

    if not self.__isInverted:
      pinInt.start(0) # Led is off (RGB value od 0,0,0)
    else:
      pinInt.start(100) # Led is off (RGB value od 0,0,0)
    
    return pinInt

  def clean(self):
    """Clean the GPIO channels"""
    self.off()
    self.GPIO.cleanup()
  
  def getRGB(self):
    """Return the current RGB values"""
    return (self.__r, self.__g, self.__b)
