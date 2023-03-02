import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the input image file line by line
with open(input_file, 'r') as f:
    lines = f.readlines()

# Extract the image dimensions and pixel values
assert lines[0].startswith('P2')
width, height = map(int, lines[2].split())
max_value = int(lines[3])
pixels = [list(map(int, line.split())) for line in lines[4:]]

# Compute the minimum pixel value in the image
min_value = min(min(row) for row in pixels)

# Subtract the minimum value from all pixels
new_pixels = [[p - min_value for p in row] for row in pixels]

# Compute the maximum pixel value in the new image
new_max_value = max(max(row) for row in new_pixels)

# Scale the pixel values in the new image
k = 255  # for 8-bit image
scaled_pixels = [[int(k * p / new_max_value) for p in row] for row in new_pixels]

# Write the processed image to the output file
with open(output_file, 'w') as f:
    f.write('P2\n')
    f.write(f'{width} {height}\n')
    f.write(f'{k}\n')
    for row in scaled_pixels:
        f.write(' '.join(str(p) for p in row))
        f.write('\n')

