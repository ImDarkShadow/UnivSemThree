from PIL import Image
from PIL import ImageDraw

# Open image and get pixel values
img = Image.open('input_image.png')
pixels = list(img.getdata())

# Create histogram
histogram = [0] * 256
for pixel in pixels:
    histogram[pixel] += 1

# Normalize histogram values to [0, 255]
max_count = max(histogram)
normalized_hist = [round((count / max_count) * 255) for count in histogram]

# Create histogram image
hist_img = Image.new('RGB', (256, 256), color='white')
draw = ImageDraw.Draw(hist_img)
for i, count in enumerate(normalized_hist):
    draw.line((i, 255, i, 255-count), fill='black', width=1)

# Save histogram image
hist_img.save('histogram.png')

