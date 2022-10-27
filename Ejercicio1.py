# Practica 2. Se encarga de encender los colores
# primarios y varias mezclas de colores de un led

import RPi.GPIO as GPIO

# Pin numbers
rojoPin = 11
azulPin = 15
verdePin = 13

# Turn on pin
def encender(pin,intensity = 100):
    GPIO.setmode(GPIO.BOARD) # Select pin number mode 
    GPIO.setup(pin, GPIO.OUT) # Change pin mode to output
    pwm = GPIO.PWM(pin,100) # Start PWM
    intensity = 100 - intensity
    pwm.start(intensity) # Turn on pin

# Turn off pin
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH) # Turn off pin

# -------Primary colors-----------
# Turn on the red pin
def encenderRojo(intensity = 100):
    encender(rojoPin,intensity)
def apagarRojo():
    apagar(rojoPin)

# Turn on the blue pin
def encenderAzul(intensity = 100):
    encender(azulPin,intensity)
def apagarAzul():
    apagar(azulPin)
    
# Turn on the green pin
def encenderVerde(intensity = 100):
    encender(verdePin,intensity)
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

def encenderNaranja():
    encenderRojo()
    encenderVerde(50)
def apagarNaranja():
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

# Main program. Uncomment the lines below to change the color
# # -----Rojo-----
# encenderRojo()
# apagarRojo
# # -----Azul-----
# encenderAzul()
# apagarAzul()
# # ----Verde-----
# encenderVerde()
# apagarVerde()
# # ---Amarillo---
# encenderAmarillo()
# apagarAmarillo()
# # ---Magenta----
# encenderMagenta()
# apagarMagenta()
# # -----Cyan-----
# encenderCyan()
# apagarCyan()
# # ----Blanco----
# encenderBlanco()
# apagarBlanco()
# # ---Naranja----
# encenderNaranja()
# apagarNaranja()
# #----------------

#Clean the pins used
GPIO.cleanup()    

#-------Use cases-------
# Uncomment red ----> Output led red
# Uncomment white --> Output led white
#-----------------------