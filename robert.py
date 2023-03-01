from PIL import Image

# Load the input image
input_image = Image.open("input1.pgm")

# Apply Sobel operator for image sharpening
def sobel_operator(pixel):
    row, col = pixel.shape
    output_pixel = pixel.copy()

    for i in range(1, row-1):
        for j in range(1, col-1):
            sobel_x = ((-1) * pixel[i-1][j-1] + (-2) * pixel[i-1][j] + (-1) * pixel[i-1][j+1]) + \
                      (pixel[i+1][j-1] + 2 * pixel[i+1][j] + pixel[i+1][j+1])
            sobel_y = ((-1) * pixel[i-1][j-1] + (-2) * pixel[i][j-1] + (-1) * pixel[i+1][j-1]) + \
                      (pixel[i-1][j+1] + 2 * pixel[i][j+1] + pixel[i+1][j+1])
            output_pixel[i][j] = int((sobel_x**2 + sobel_y**2)**0.5)

    return output_pixel

# Convert the pixel values to numpy array and apply the operator
pixel = np.array(input_image)
output_pixel = sobel_operator(pixel)

# Create an output image from the numpy array
output_image = Image.fromarray(output_pixel)
output_image.save("sobel.pgm")
output_image.show()

