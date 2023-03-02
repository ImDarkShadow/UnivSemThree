import sys
input_file_path = sys.argv[1]
output_file_path = sys.argv[1]
def sobel_operator(input_file_path, output_file_path):
    """
    Apply the Sobel operator to a PGM file.
    """
    # Read the input image
    width, height, pixel_values = read_pgm(input_file_path)

    # Define the Sobel kernels for computing the x and y gradients
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Pad the input image with zeros to avoid border issues
    padded_pixel_values = [0] * ((width + 2) * (height + 2))
    for i in range(height):
        for j in range(width):
            padded_pixel_values[(i + 1) * (width + 2) + (j + 1)] = pixel_values[i * width + j]

    # Compute the x and y gradients of the image by convolving the image with the Sobel kernels
    gradient_x = [0] * (width * height)
    gradient_y = [0] * (width * height)
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            gx = sum([sobel_x[k][l] * padded_pixel_values[(i + k) * (width + 2) + (j + l)] for k in range(-1, 2) for l in range(-1, 2)])
            gy = sum([sobel_y[k][l] * padded_pixel_values[(i + k) * (width + 2) + (j + l)] for k in range(-1, 2) for l in range(-1, 2)])
            gradient_x[(i - 1) * width + (j - 1)] = gx
            gradient_y[(i - 1) * width + (j - 1)] = gy

    # Compute the magnitude and direction of the gradient at each pixel
    gradient_magnitude = [0] * (width * height)
    gradient_direction = [0] * (width * height)
    for i in range(height):
        for j in range(width):
            index = i * width + j
            gradient_magnitude[index] = int(((gradient_x[index] ** 2) + (gradient_y[index] ** 2)) ** 0.5)
            gradient_direction[index] = int((180 / 3.14159) * math.atan2(gradient_y[index], gradient_x[index]))

    # Write the output image
    write_pgm(output_file_path, width, height, gradient_magnitude)

