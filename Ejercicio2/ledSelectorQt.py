# Contains the graphical Qt interface class for the ledRGBMain.py program

from PyQt5.QtWidgets import QWidget, QPushButton, QColorDialog, QLabel
from PyQt5.QtCore import Qt
from ledRGB import LedRGB

class AppQt(QWidget):
    """Led interface using Qt for graphical interface"""
    def __init__(self):
        # Initialice the window properties
        super().__init__()
        self.title = 'Led RGB color dialog'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 250
        self.initUI()
    
    def addLed(self, led:LedRGB):
        """Adds a RGB led to the interface"""
        self.led = led
    
    def initUI(self):
        """Initialice and set up the interface window"""
        # Main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Change color button
        self.button = QPushButton('Click here to change color', self)
        self.button.setFlat(True)
        self.button.setContentsMargins(0, 0, 0, 0)
        self.button.move(70,self.height - 40)
        self.button.clicked.connect(self.on_click)

        # Current color label
        self.currentColorText = QLabel('The current color is: None',self)
        self.currentColorText.setGeometry(40, 10, 240, 20)

        # Current color preview
        self.currentColorImage = QLabel('Click here to reset',self)
        self.currentColorImage.setGeometry(int(self.width / 4) , 40 , int(self.width / 2), int(self.width / 2) )
        self.currentColorImage.setAlignment(Qt.AlignCenter)
        self.currentColorImage.mousePressEvent =lambda event: self.resetColor()

        # Show the window on screen
        self.show()

    def on_click(self):
        """When clicked open the color dialog window"""
        self.openColorDialog()

    def openColorDialog(self):
        """Dialog window to chose a color"""
        color = QColorDialog.getColor()

        # If the color chosen exists
        if color.isValid():
            # Change the current color label to the rgb values
            self.currentColorText.setText(f"The current color is: ({color.red()}, {color.green()}, {color.blue()})")

            # Change the current color preview
            self.currentColorImage.setStyleSheet(f"background-color:rgba{color.getRgb()}")

            # Change the led color to the chosen rgb values
            self.led.on(color.red(), color.green(), color.blue())
    
    def resetColor(self):
        """Resets the led color"""
        # Reset the current color label to none
        self.currentColorText.setText("The current color is: None")

        # Reset the current color preview to transparent 
        self.currentColorImage.setStyleSheet("background-color:rgba(0,0,0,0)")

        # Turn off the led color
        self.led.off()
    
    def closeEvent(self, event):
        """Used whe closing the window, in order to do a cleanup"""
        self.led.clean()