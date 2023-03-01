from PIL import Image
import random

# Load image
im = Image.open("input1.pgm")

# Add 20 to each pixel and clip values over 255
sum_im = im.copy()
width, height = im.size
for i in range(width):
    for j in range(height):
        sum_im.putpixel((i,j), im.getpixel((i,j)) + 20)
        if sum_im.getpixel((i,j)) > 255:
            sum_im.putpixel((i,j), 255)
sum_im.save("SumImage.pgm")

# Create two random images and select the maximum pixel-wise
max_im = Image.new("L", im.size)
f1_im = Image.new("L", im.size)
f2_im = Image.new("L", im.size)
a = random.randint(0, 2)
b = random.randint(0, 2)
for i in range(width):
    for j in range(height):
        f1_im.putpixel((i,j), a*im.getpixel((i,j)))
        f2_im.putpixel((i,j), b*im.getpixel((i,j)))
f1_im = f1_im.convert("L")
f2_im = f2_im.convert("L")
f1_im = f1_im.point(lambda x: x * (255/f1_im.getextrema()[1]))
f2_im = f2_im.point(lambda x: x * (255/f2_im.getextrema()[1]))
for i in range(width):
    for j in range(height):
        if f1_im.getpixel((i,j)) > f2_im.getpixel((i,j)):
            max_im.putpixel((i,j), f1_im.getpixel((i,j)))
        else:
            max_im.putpixel((i,j), f2_im.getpixel((i,j)))
max_im.save("MaxImage.pgm")

