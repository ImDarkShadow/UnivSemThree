import sys
import math

# Parse command-line arguments
if len(sys.argv) != 3:
    print("Usage: python adjacency_connectivity.py <input_file> <output_file>")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the input image file line by line
with open(input_file, 'r') as f:
    lines = f.readlines()

# Extract the image dimensions and pixel values
assert lines[0].startswith('P2')
width, height = map(int, lines[1].split())
max_value = int(lines[2])
pixels = [[int(val >= 128) for val in line.split()] for line in lines[3:]]

# Define the coordinates of two pixels to compare
x1, y1 = 10, 10
x2, y2 = 20, 20

# Check adjacency between the two pixels
dx, dy = abs(x1 - x2), abs(y1 - y2)
dist = math.sqrt(dx**2 + dy**2)
if dist == 1:
    print("The two pixels are 4-adjacent.")
elif dist == math.sqrt(2):
    print("The two pixels are 8-adjacent.")
else:
    print("The two pixels are m-adjacent.")

# Check connectivity between the two pixels
visited = [[False]*width for _ in range(height)]
stack = [(x1, y1)]
visited[y1][x1] = True
connected = False
while stack:
    x, y = stack.pop()
    if x == x2 and y == y2:
        connected = True
        break
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < width and 0 <= new_y < height and not visited[new_y][new_x] and pixels[new_y][new_x]:
            visited[new_y][new_x] = True
            stack.append((new_x, new_y))

if connected:
    print("The two pixels are connected.")
else:
    print("The two pixels are not connected.")

# Compute the digital path between the two pixels
if connected:
    path = []
    x, y = x1, y1
    dx, dy = x2 - x1, y2 - y1
    sx, sy = 1 if dx > 0 else -1, 1 if dy > 0 else -1
    dx, dy = abs(dx), abs

