
import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0


class nokiaLCD:
    def __init__(self):
        self.disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

        # Initialize library.
        self.disp.begin(contrast=60)

        # Clear display.
        self.disp.clear()
        self.disp.display()

        # Create image buffer.
        self.image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

        # Load default font.
        self.font = ImageFont.load_default()

        # Create drawing object.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a white filled box to clear the image.
        self.draw.rectangle((0, 0, LCD.LCDWIDTH, LCD.LCDHEIGHT), outline=255, fill=255)

    def drawOnePoint(self, X, Y):
        self.draw.rectangle((0, 0, 83, 47), outline=255, fill=255)
        self.draw.rectangle((X, Y, X+2, Y+2), outline=0, fill=255)

    def drawLine(self, startX, endX, startY, endY):
        self.draw.line((startX, startY, endX, endY), fill=0)

    def clearImagePart(self, startX, endX, startY, endY):
        self.draw.rectangle((startX, startY, endX, endY), outline=255, fill=255)


    def drawPoint(self, X, Y, fill):
        self.draw.rectangle((X, Y, X + 2, Y + 2), outline=0, fill=fill)

    def clearImage(self):
        self.draw.rectangle((0, 0, 83, 47), outline=255, fill=255)

    def printText(self, info, X, Y):
      self.draw.text((X, Y), info, font = self.font)

    def displayImage(self):
        # Display image.
        self.disp.image(self.image)
        self.disp.display()




