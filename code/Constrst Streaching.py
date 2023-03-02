import sys

# read input file name and output file name from command line arguments
if len(sys.argv) < 3:
    print('Usage: python contrast.py <input_file> <output_file>')
    sys.exit(1)
input_file = sys.argv[1]
output_file = sys.argv[2]

# read pixel values from input file
with open(input_file, 'r') as picture:
    element = picture.readlines()

pixel = []
for i in range(len(element) - 4):
    pixel.append(int(element[i+4].replace('\n', '')))

# calculate maximum and minimum pixel values
max_pixel = max(pixel)
min_pixel = min(pixel)

# write updated pixel values to output file
with open(output_file, 'w') as out:
    for i in range(len(element) - 4):
        element[i+4] = str(round(((pixel[i] - min_pixel)/(max_pixel - min_pixel)*255), 0)) + '\n'
    out.writelines(element)

