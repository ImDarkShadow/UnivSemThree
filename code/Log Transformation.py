import numpy as np
import sys

# Read input image from command line argument
if len(sys.argv) < 2:
    print("Please provide the input image as a command line argument")
    sys.exit()
    
input_file = sys.argv[1]
input_image = np.loadtxt(input_file, skiprows=3)

# Apply log transformation
c = 1  # Positive constant
log_transformed_image = c * np.log(1 + input_image)

# Normalize pixel values to 0-255 range
log_transformed_image = log_transformed_image / np.max(log_transformed_image) * 255

# Write log-transformed image to file
output_file = input_file[:-4] + "_log_transformed.pgm"
with open(output_file, "w") as f:
    # Write header
    f.write("P2\n")
    f.write("# Log-transformed image\n")
    f.write("{} {}\n".format(log_transformed_image.shape[1], log_transformed_image.shape[0]))
    f.write("255\n")

    # Write pixel values
    for x in range(log_transformed_image.shape[0]):
        for y in range(log_transformed_image.shape[1]):
            f.write(str(int(log_transformed_image[x][y])) + " ")
        f.write("\n")

print("Log-transformed image written to {}".format(output_file))

