import sys

if len(sys.argv) < 3:
    print("Usage: python myscript.py input.pgm output.pgm")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as picture:
    element = picture.readlines()

with open(output_file, 'w') as out:
    for i in range(len(element) - 4):
        element[i+4] = str(255 - int(element[i+4].replace('\n', ''))) + '\n'
    out.writelines(element)

