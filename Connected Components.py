import sys

# Parse command-line arguments
if len(sys.argv) != 3:
    print("Usage: python connected_components.py <input_file> <output_file>")
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

# Define a list to keep track of the visited pixels
visited = [[False]*width for _ in range(height)]

# Define a counter variable to keep track of the number of connected components
counter = 0

# Define a DFS function to mark all the pixels in the same connected component as visited
def dfs(x, y):
    visited[y][x] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < width and 0 <= new_y < height and not visited[new_y][new_x] and pixels[new_y][new_x]:
            dfs(new_x, new_y)

# Find the number of connected components
for y in range(height):
    for x in range(width):
        if not visited[y][x] and pixels[y][x]:
            counter += 1
            dfs(x, y)

# Write the counter value to the output file
with open(output_file, 'w') as f:
    f.write(str(counter))

