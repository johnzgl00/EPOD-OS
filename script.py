from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import demo_mode
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
import time

WIDTH = 128
HEIGHT = 160
SPEED_HZ = 4000000
option = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(12, GPIO.IN)

DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

selected_mode = False

disp = TFT.ST7735(
    DC,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=SPEED_HZ))

# Initialize display.
disp.begin()

disp.clear((0, 0, 0))

# Alternatively can clear to a black screen by calling:
# disp.clear()

# Get a PIL Draw object to start drawing on the display buffer.
draw = disp.draw()
# Load default font.
font = ImageFont.load_default()

def draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)

def main():
    selected_mode = False
    option = 0

    #TITLE
    draw_rotated_text(disp.buffer, "E", (117, 75), 270, font, fill=(0,255,0))
    draw_rotated_text(disp.buffer, "POD", (117, 81), 270, font, fill=(255,255,255))
    
    #HACKING MODE BUTTON
    draw.rectangle((80,40,108,130), outline=(0,0,255), fill=(0,0,0))
    draw_rotated_text(disp.buffer, "Hacking Mode", (90 ,50), 270, font, fill=(0,0,255))
    
    #DEMO MODE BUTTON
    draw.rectangle((40,40,68,130), outline=(255,0,255), fill=(0,0,0))
    draw_rotated_text(disp.buffer, "Demo Mode", (50 ,58), 270, font, fill=(255,0,255))

    disp.display()

    while not selected_mode:
        if GPIO.input(16):
            option += 1
        if option == 1:
            draw.rectangle((80,40,108,130), outline=(0,0,255), fill=(0,0,200))
            draw_rotated_text(disp.buffer, "Hacking Mode", (90 ,50), 270, font, fill=(0,0,255))
            draw.rectangle((40,40,68,130), outline=(255,0,255), fill=(0,0,0))
            draw_rotated_text(disp.buffer, "Demo Mode", (50 ,58), 270, font, fill=(255,0,255))
        elif option == 2:
            draw.rectangle((80,40,108,130), outline=(0,0,255), fill=(0,0,0))
            draw_rotated_text(disp.buffer, "Hacking Mode", (90 ,50), 270, font, fill=(0,0,255))
            draw.rectangle((40,40,68,130), outline=(255,0,255), fill=(200,0,200))
            draw_rotated_text(disp.buffer, "Demo Mode", (50 ,58), 270, font, fill=(255,0,255))
        elif option == 3:
            option = 1
        if GPIO.input(12):
            selected_mode = True
            time.sleep(0.2)
        disp.display()
        time.sleep(0.1)
    print("passed")
    selected_mode = False
    if option == 1:
        disp.clear((0,0,0))
        draw_rotated_text(disp.buffer, "Hacking Mode", (60 ,50), 270, font, fill=(0,0,255))
        disp.display()
        time.sleep(1.5)
        disp.clear((0,0,0))
    elif option == 2:
        disp.clear((0,0,0))
        draw_rotated_text(disp.buffer, "Demo Mode", (60 ,58), 270, font, fill=(255,0,255))
        disp.display()
        time.sleep(1.5)
        disp.clear((0,0,0))
        demo_mode.show()
    disp.display()
main()
