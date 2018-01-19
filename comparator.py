import numpy as np
import PIL.Image as image
import sys
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

""" This code loads 2 images and determine if they are close enough to each other

INPUT: IMAGE_1, IMAGE_2(.jpg/.png/.bmp etc)

OUTPUT: SIMILARITY(FLOAT) || BOOLEAN """

# Load image from source
def load_image(path):
    pic = image.open(path)
    pic = pic.convert('LA')
    pix = np.asarray(pic)[:,:,0]
    # print(pix.shape)
    return pix
    # plt.imshow(pix, cmap = 'gray')

def mse(pix1, pix2):
    err = np.sum((pix1.astype("float") - pix2.astype("float")) ** 2)
    err /= float(pix1.shape[0] * pix1.shape[1])
    return err

# Convert the pixel array with 2D Fourier Transform
def switch_pix(pix):
    transformed = fft.fft2(pix)
    transformed = fft.fftshift(transformed)
    # Ignore wave state
    transformed = np.real(transformed)
    return transformed

# Compared the matrices with algorithm central to this method.
def compare_matrices(apix, bpix):
    dpix = apix - bpix
    return sum(dpix)/sum(apix)
    pass

def compare_images(img1, img2):
    pix1 = load_image(img1)
    pix2 = load_image(img2)
    # sw1 = switch_pix(pix1)
    # sw2 = switch_pix(pix2)
    # fft_compare = compare_matrices(sw1, sw2)
    err = mse(pix1, pix2)
    return err

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Not enough arguments')
    IMAGE_1 = sys.argv[1]
    IMAGE_2 = sys.argv[2]
    print(compare_images(IMAGE_1, IMAGE_2))
