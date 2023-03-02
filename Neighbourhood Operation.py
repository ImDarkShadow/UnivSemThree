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

# Define the size of the neighborhood window (m x n)
m = 3  # number of rows in the neighborhood window
n = 3  # number of columns in the neighborhood window

# Define the Sxy set of pixel coordinates to use for the operation
Sxy = [(i, j) for i in range(-m//2, m//2+1) for j in range(-n//2, n//2+1)]

# Apply the neighborhood operation to each pixel in the input image
new_pixels = []
for y in range(height):
    new_row = []
    for x in range(width):
        # Extract the neighborhood window centered at (x, y)
        neighborhood = [(x + i, y + j) for i, j in Sxy if 0 <= x+i < width and 0 <= y+j < height]
        # Compute the average pixel value using the formula
        avg_value = sum(pixels[j][i] for i, j in neighborhood) / (m * n)
        new_row.append(int(avg_value))
    new_pixels.append(new_row)

# Write the processed image to the output file
with open(output_file, 'w') as f:
    f.write('P2\n')
    f.write(f'{width} {height}\n')
    f.write(f'{max_value}\n')
    for row in new_pixels:
        f.write(' '.join(str(p) for p in row))
        f.write('\n')

