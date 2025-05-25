from PIL import Image
import board
import digitalio
import adafruit_st7735r

# Display configuration (change pins if your wiring differs)
TFT_DC = digitalio.DigitalInOut(board.D24)
TFT_RST = digitalio.DigitalInOut(board.D25)
TFT_CS = digitalio.DigitalInOut(board.CE0)  # usually CE0 for SPI device 0

# Initialize SPI bus
spi = board.SPI()

# Initialize display
disp = adafruit_st7735r.ST7735R(
    spi,
    cs=TFT_CS,
    dc=TFT_DC,
    rst=TFT_RST,
    width=128,
    height=160,
    rotation=90
)

disp.fill(0)  # Clear display (fill black)

print("Loading image...")
image = Image.open("cat.jpg")

# Resize image to display size
image = image.resize((128, 160))

# Show image on the display
disp.image(image)

print("Done")

