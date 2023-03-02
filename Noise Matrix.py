import numpy as np
import random
import sys

    
input_file = sys.argv[1]
input_image = np.loadtxt(input_file, skiprows=3)

# Generate 10 noisy images
noisy_images = []
for i in range(10):
    # Generate uncorrelated noise matrix
    noise_matrix = np.zeros_like(input_image)
    for x in range(input_image.shape[0]):
        for y in range(input_image.shape[1]):
            noise_matrix[x][y] = random.uniform(-1, 1)
    
    # Add noise to input image
    noisy_image = input_image + noise_matrix
    noisy_images.append(noisy_image)

# Apply averaging to resolve noise
averaged_image = np.zeros_like(input_image)
for x in range(input_image.shape[0]):
    for y in range(input_image.shape[1]):
        pixel_sum = 0
        for noisy_image in noisy_images:
            pixel_sum += noisy_image[x][y]
        averaged_image[x][y] = pixel_sum / 10

# Write averaged image to file
output_file = input_file[:-4] + "_averaged.pgm"
with open(output_file, "w") as f:
    # Write header
    f.write("P2\n")
    f.write("# Averaged image\n")
    f.write("{} {}\n".format(averaged_image.shape[1], averaged_image.shape[0]))
    f.write("255\n")

    # Write pixel values
    for x in range(averaged_image.shape[0]):
        for y in range(averaged_image.shape[1]):
            f.write(str(int(averaged_image[x][y])) + " ")
        f.write("\n")


