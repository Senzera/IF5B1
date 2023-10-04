import cv2 as cv
import numpy as np

# Membaca gambar grayscale
image = cv.imread("gojo.png", 0)

if image is None:
    print('Could not open or find the image: ')
    exit(0)

# Melakukan histogram equalization untuk mengurangi kontras
equalized_image = cv.equalizeHist(image)

cv.imshow('Original Image', image)
cv.imshow('Decreased Contrast Image', equalized_image)

cv.waitKey(0)
cv.destroyAllWindows()
