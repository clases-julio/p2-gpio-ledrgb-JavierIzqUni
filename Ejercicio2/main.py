# Main function of the Practica 2 that changes the color of an RGB led

import sys
from ledSelectorQt import AppQt
from PyQt5.QtWidgets import QApplication
from ledRGB import LedRGB
from ledSelectorBash import AppBash

# Pin numbers
rojoPin = 11
azulPin = 15
verdePin = 13
  
if __name__ == '__main__':
  if (len(sys.argv) > 1):
    if (sys.argv[1] == '--interface'):
      # If the command line argument is interface then use the graphical Qt interface
      app = QApplication(sys.argv)
      interface = AppQt()
      ledRGB = LedRGB(rojoPin, azulPin, verdePin, inverted = True)  # Creates the led object
      interface.addLed(ledRGB)  # Adds the led to the interface
      sys.exit(app.exec_())
    else:
      # If the command line argument is invalid then exit
      print(f"{sys.argv[1]} is not valid. The only valid argument is --interface")
      exit(1)
  else:
    # The default interface is Bash
    interface = AppBash()
    ledRGB = LedRGB(rojoPin, azulPin, verdePin, inverted = True) # Creates the led object
    interface.addLed(ledRGB) # Adds the led to the interface
    interface.start() # Starts the input mode

# -------------------------------------Use cases---------------------------------------
# Input man.py ---> Opens the bash interface
# Input man.py -h ---> Error: "-h is not valid. The only valid argument is --interface"
# Input man.py --interface --> Opens the graphical interface
#   -----------------------Use cases bash interface----------------------
#    Input rojo ---> Output led red
#    Input green --> Output led green
#    Input Blue ---> Output 'Invalid input: Blue not available', led no color
#    Input Add ----> Output 'Invalid input', led no color
#    Input Add naranja --> Output Ask the user to enter the RGB value, led no change
#     -- Input 244 42 21 --> Output Value saved, back to normal, led no change
#     -- Input a 345 ------> Output 'Invalid input', led no change
#     -- Input a b c ------> Output 'Invalid input', led no change
#     -- Input 23 3 12 32 -> Output 'Invalid input', led no change
#    Input apagar red ---> Output led red values are 0, no red, led doesn't reset the other colors
#    Input Off amarillo ---> Output add color yellow to the led, led doesn't reset the other colors
#    Input salta 23 ---> Output 'Invalid input', led no change
#    Input 23 43 23 ---> Output led changes color to RGB value
#    Input a 43 r3 ---> Output 'Invalid input', led no color
#    Input 23 43 23 34 ---> Output 'Invalid input', led no color
#    Input End ---> Output lef off, ends the program
#   ------------------------------------------------------------------------
#
#   -----------------------Use cases Graphical Interface -------------------
#   Open color select dialog --> select color --> led changes color
#   Click on reset dialog -----> led color resets
#   Close window -----> led off, ends the program
#   ------------------------------------------------------------------------