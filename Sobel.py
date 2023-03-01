from PIL import Image

# Load the input image
input_image = Image.open("input1.pgm")

# Apply Roberts Cross-Gradient operator for image sharpening
def roberts_cross_gradient_operator(pixel):
    row, col = pixel.shape
    output_pixel = pixel.copy()

    for i in range(1, row):
        for j in range(1, col):
            robert_x = (-1) * pixel[i-1][j-1] + pixel[i][j]
            robert_y = (-1) * pixel[i-1][j] + pixel[i][j-1]
            output_pixel[i][j] = int((robert_x**2 + robert_y**2)**0.5)

    return output_pixel

# Convert the pixel values to numpy array and apply the operator
pixel = np.array(input_image)
output_pixel = roberts_cross_gradient_operator(pixel)

# Create an output image from the numpy array
output_image = Image.fromarray(output_pixel)
output_image.save("robert.pgm")

