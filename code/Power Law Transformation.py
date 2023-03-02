import sys
from math import pow


input_file = sys.argv[1]
output_file = sys.argv[2]
gamma = 2
C = 1.3

with open(input_file, 'r') as picture:
    element = picture.readlines()

with open(output_file, 'w') as out:
    for i in range(len(element) - 4):
        pix = int(C * pow(int(element[i+4].replace('\n', '')), gamma))
        if pix > 255:
            element[i+4] = '255\n'
        elif pix < 0:
            element[i+4] = '0\n'
        else:
            element[i+4] = str(pix) + '\n'
    out.writelines(element)

