import sys
from math import sqrt

# Parse command-line arguments
if len(sys.argv) != 6:
    print("Usage: python distances.py <input_file> <output_file> <x1> <y1> <x2> <y2>")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
x1, y1, x2, y2 = map(int, sys.argv[3:])

# Read the input image file line by line
with open(input_file, 'r') as f:
    lines = f.readlines()

# Extract the image dimensions and pixel values
assert lines[0].startswith('P2')
width, height = map(int, lines[1].split())
max_value = int(lines[2])
pixels = [[int(val) for val in line.split()] for line in lines[3:]]

# Compute the Euclidean distance between the two pixels
euclidean_distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Compute the D4 distance between the two pixels
d4_distance = abs(x1 - x2) + abs(y1 - y2)

# Compute the D8 distance between the two pixels
d8_distance = max(abs(x1 - x2), abs(y1 - y2))

# Compute the Dm distance between the two pixels
dm_distance = max(abs(x1 - x2), abs(y1 - y2), abs(x1 - y1), abs(x2 - y2))

# Write the distances to the output file
with open(output_file, 'w') as f:
    f.write(f"Euclidean distance: {euclidean_distance:.2f}\n")
    f.write(f"D4 distance: {d4_distance}\n")
    f.write(f"D8 distance: {d8_distance}\n")
    f.write(f"Dm distance: {dm_distance}\n")

