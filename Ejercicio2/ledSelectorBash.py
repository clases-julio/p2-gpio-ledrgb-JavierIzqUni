# Contains the bash interface class for the ledRGBMain.py program

from ledRGB import LedRGB

class AppBash():
  """Led interface for bash"""
  def __init__(self):
    # Interface menu help
    print('Led RGB color dialog')
    print("In order to exit: 'End', 'Exit' or 'Fin'")
    print("In order to add a new color: Add colorName")
    print("Input a color to change or its rgb values:")

    # Lists and dictionaries that will be used as options in the interface. Could be stored in a config file.
    self.onOrder = ["encender","Encender","on","On"]
    self.offOrder = ["apagar","Apagar","off","Off"]
    self.exitOrder = ["End","Exit","Fin"]
    self.availableColorsEN = {"red": (255,0,0), "green": (0,255,0), "blue": (0,0,255), "white": (255,255,255),
      "yellow": (255,255,0), "cyan": (0,255,255), "magenta": (255,0,255)}      
    self.availableColorsSP = {"rojo": (255,0,0), "verde": (0,255,0), "azul": (0,0,255), "blanco": (255,255,255),
      "amarillo": (255,255,0), "cyan": (0,255,255), "magenta": (255,0,255)} 
    self.availableColorsCustom = {}
    # ----------------------------------------------------------------

  def addLed(self, led:LedRGB):
    """Adds a RGB led to the interface"""
    self.led = led
  
  def addColor(self, colorName:str):
    """Store a custom color in the interface"""

    # Ask the user to specify the rgb values of the color
    rgbInput = input("Type its RGB values: ")
    rgbList = rgbInput.split(' ')

    # Check if the values input are 3
    if len(rgbList) != 3 :
      print('Invalid input')
      return

    # Check if the values input are integers
    try:
      r = int(rgbList[0])
      g = int(rgbList[1])
      b = int(rgbList[2])
    except ValueError:
      print('Invalid input')
      return
    
    # Store the color an its RGB value
    self.availableColorsCustom[colorName] = (r,g,b)
  
  def start(self):
    # Start the program to allow the user to use the led
    while True:
      order = input("> ") # Allow the user to input commands

      # If the user inputs a exit command then exit the program
      if order in self.exitOrder:
        self.closeEvent()

      orderList = order.split(' ') # Create a list of the command input 

      if len(orderList) == 1:
        # The command is a color. The led color resets and change to the input color
        self.led.off()
        self.changeColor(order)

      elif len(orderList) == 2:
        # The command has an action and a color.
        if orderList[0] in self.onOrder:
          # The action turns on the color, but doesn't reset before
          self.changeColor(orderList[1])
        elif orderList[0] in self.offOrder:
          # The action turns off the color, but not the rest
          self.turnOffColor(orderList[1])
        elif orderList[0] == "Add":
          # The action allows the user to add a custom color
          self.addColor(orderList[1])
        else:
          # If the action is incorrect then go back to ask the user
          print('Invalid input')
          continue

      elif len(orderList) == 3:
        # The command is an RGB value. The led color resets and change to the input values
        self.led.off()

        # Check if the values input are integers
        try:
          r = int(orderList[0])
          g = int(orderList[1])
          b = int(orderList[2])
        except ValueError:
          print('Invalid input')
          continue
        
        # Change the led color to the chosen rgb values
        self.led.on(r,g,b)
      else:
        # If the action is incorrect then go back to ask the user
        print('Invalid input')
        continue

  def getRGB(self, colorName:str)-> tuple:
    """Gets the RGB values from the colors dictionaries."""
    # Checks in the color dictionaries, if not found then set color to (0,0,0)
    colorRGB = self.availableColorsEN.get(colorName,(0,0,0)) # Checks in the english colors
    if colorRGB == (0,0,0):
      colorRGB = self.availableColorsSP.get(colorName,(0,0,0)) # Checks in the spanish colors
    
    if colorRGB == (0,0,0):
      colorRGB = self.availableColorsCustom.get(colorName,(0,0,0)) # Checks in the custom colors

    return colorRGB # Return the RGB values in a tuple

  def changeColor(self, colorName:str):
    colorRgb = self.getRGB(colorName) # Get the RGB values
    if colorRgb == (0,0,0):
      # If the RGB values are (0,0,0), then the color hasn't been found 
      print(f'Invalid input: {colorName} not available')
      return

    # Change the led color to the chosen rgb values
    currentRGB = self.led.getRGB()

    r = colorRgb[0] + currentRGB[0]
    g = colorRgb[1] + currentRGB[1]
    b = colorRgb[2] + currentRGB[2]

    self.led.on(r,g,b)
  
  def turnOffColor(self, colorName:str):
    colorRgb = self.getRGB(colorName) # Get the RGB values
    if colorRgb == (0,0,0):
      # If the RGB values are (0,0,0), then the color hasn't been found 
      print(f'Invalid input: {colorName} not available')
      return
    
    currentRGB = self.led.getRGB() # Get the current RGB values

    # Get the RGB values from turning off the input color
    r = currentRGB[0] - colorRgb[0] 
    g = currentRGB[1] - colorRgb[1]
    b = currentRGB[2] - colorRgb[2]

    self.led.on(r,g,b) # Turn off the color
  
  def closeEvent(self):
    """Used whe closing the interface, in order to do a cleanup"""
    self.led.clean()
    exit(0)