from PIL import Image 



def add_gaussian_noise(image, mean = 0.0, var = 0.1):
    sigma = var**2

    row, col, _ = image.shape

