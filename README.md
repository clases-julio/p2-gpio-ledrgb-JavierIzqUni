# p2-gpio-ledrgb
## Execution

## Hardware problems
Before entering the software part, we needed to check if the led worked properly. 

In the beggining we weren't able to make the led light because the led polarity was changed. After rewiring the led the following way we were able to make the led work:

We change the ground wire to a 3V3 power one, and in the software in order to light a color instead of send power, we convert the GPIO pin to ground.

Another problem was the lack of resistors, which lead us to use ones that were a little bit more powerful than needed.

## Observations

### Ejercicio 1
In this program we didn't want to change much the code provided because of the hardware issues explained above. So instead of spending much time in this introduction excercise, we decided to center our attention on the next excercise.

Also in this excercise we didn't use any OOP.

### Ejercicio 2
This program is divided into four different files in order to make the code look cleaner.
#### Main file
This file contains the main program and is the file that has to be executed.

The function of this program is to chose the interface used, chosen from the arguments passed by the user.

The defualt interface is the one implemented in [bash](#bash-interface-file), the other option is the [graphical interface using Qt](#bash-interface-file).

Also in this file is were the values of the pins are declared.
```python
# Pin numbers
rojoPin = 11
azulPin = 15
verdePin = 13
```

#### Bash interface file
This file contains the AppBash class that contains the bash interface.

The commands are implemented in Spanish and English using lists of key words, and checking if the command is in the list.
```python
self.onOrder = ["encender","Encender","on","On"]
# .....
if command in self.onOrder:
  # Do something
```

The commands available are listed in the [execution segment](#execution)

#### Qt interface file
This file contains the AppQt class that contains the graphical interface.

The interface is implemented using the [PyQt5 library](https://pypi.org/project/PyQt5/)

The only problem with the interface was the need to implement a custom closing event, in order to clean the GPIO pins before ending the program.
```python
def closeEvent(self, event):
  """Used whe closing the window, in order to do a cleanup"""
  self.led.clean() # Clean the GPIO pins
```

#### RGB led file
This file contains the LedRGB that is responsible of controlling the rgb led.
