from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
import time
import script

WIDTH = 128
HEIGHT = 160
SPEED_HZ = 4000000

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(12, GPIO.IN)

loop = True
selection = 0

DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

disp = TFT.ST7735(DC,rst=RST,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=SPEED_HZ))

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

def show():
    selection = 0
    loop = True
    while loop:
        #TITLE
        draw_rotated_text(disp.buffer, "E", (117, 75), 270, font, fill=(0,255,0))
        draw_rotated_text(disp.buffer, "POD", (117, 81), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
        draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
        disp.display()
        if GPIO.input(16):
            selection = selection + 1
            if selection == 1:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 2:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 3:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 4:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 5:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 6:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 7:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 8:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(0,255,0))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(255,255,255))
                disp.display()
            if selection == 9:
                draw_rotated_text(disp.buffer, "Nmap", (110, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "HPing3", (100, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Nikto", (90, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Wifite", (80, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Dirbuster", (70, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Gobuster", (60, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Aircrack-ng", (50, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Netdiscover", (40, 10), 270, font, fill=(255,255,255))
                draw_rotated_text(disp.buffer, "Tshark", (30, 10), 270, font, fill=(0,255,0))
                disp.display()
            if selection == 10:
                selection = 1
            time.sleep(0.1)
        disp.display()
        if GPIO.input(12):
            loop = False
    script.main()
