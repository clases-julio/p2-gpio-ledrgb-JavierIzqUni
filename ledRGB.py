# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO

# Pin numbers
rojoPin = 11
azulPin = 13
verdePin = 15

# Turn on pin
def encender(pin):
    GPIO.setmode(GPIO.BOARD) # Select pin number mode 
    GPIO.setup(pin, GPIO.OUT) # Change pin mode to output
    GPIO.output(pin, GPIO.LOW) # Turn on pin

# Turn off pin
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# -------Primary colors-----------
# Turn on the red pin
def encenderRojo():
    encender(rojoPin)
def apagarRojo():
    apagar(rojoPin)

# Turn on the blue pin
def encenderAzul():
    encender(azulPin)
def apagarAzul():
    apagar(azulPin)
    
# Turn on the green pin
def encenderVerde():
    encender(verdePin)
def apagarVerde():
    apagar(verdePin)
#---------------------------------

#---------Mixed colors-----------
def encenderAmarillo():
    encenderRojo()
    encenderVerde()
def apagarAmarillo():
    apagarRojo()
    apagarVerde()
    
def encenderMagenta():
    encenderAzul()
    encenderRojo()
def apagarMagenta():
    apagarAzul()
    apagarRojo()

def encenderCyan():
    encenderAzul()
    encenderVerde()
def apagarCyan():
    apagarAzul()
    apagarVerde()

def encenderBlanco():
    encenderAzul()
    encenderVerde()
    encenderRojo()
def apagarBlanco():
    apagarAzul()
    apagarVerde()
    apagarRojo()

#--------------------------------

# Main program
i=0
while True:
    order = input("Input a color to change('End' to exit)") # Ask the user to choose the color
    if (i==1):
        remove() # Turns off the color when you change between colors
    i=1
    if (order == "red"):
        encenderRojo()
        remove = apagarRojo
    elif (order == "blue"):
        encenderAzul()
        remove = apagarAzul
    elif (order == "green"):
        encenderVerde()
        remove = apagarVerde
    elif (order == "yellow"):
        encenderAmarillo()
        remove = apagarAmarillo
    elif (order == "magenta"):
        encenderMagenta()
        remove = apagarMagenta
    elif (order == "cyan"):
        encenderCyan()
        remove = apagarCyan
    elif (order == "white"):
        encenderBlanco()
        remove = apagarBlanco
    elif (order == "End"):
        #Clean the pins used
        GPIO.cleanup()
        break
    
