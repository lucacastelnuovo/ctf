# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/194

# Pixel everywhere
# HINT: Green pixel are your friend remove blank and black one!

from PIL import Image

input = Image.open("pixel.png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FILTER_PIXELS = [
    WHITE,
    BLACK,
]


INPUT_WIDTH = 35  # Temporary
INPUT_HEIGHT = 10  # Temporary
# [INPUT_WIDTH, INPUT_HEIGHT] = input.size

output = Image.new(mode="RGB", size=(INPUT_WIDTH, INPUT_HEIGHT), color=WHITE)


def getPixels():
    pixels = []

    for y in range(INPUT_HEIGHT):
        pixelsY = []

        for x in range(INPUT_WIDTH):
            pixelVal = input.getpixel((x, y))
            pixelsY.append(pixelVal)

        pixels.append(pixelsY)

    return pixels


def filterImage():
    for x in range(INPUT_WIDTH):
        for y in range(INPUT_HEIGHT):
            pixel = input.getpixel((x, y))

            # Debug
            # output.putpixel((x, y), pixelVal)
            # continue

            if pixel[0] == pixel[1] and pixel[1] == pixel[2]:
                continue

            if pixel not in FILTER_PIXELS:
                output.putpixel((x, y), BLACK)

    output.save("edit.png")


filterImage()
