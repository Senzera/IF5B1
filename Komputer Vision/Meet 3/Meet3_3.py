import cv2 as cv
import numpy as np


image = cv.imread("gojo.png", 0)

if image is None:
    print('Could not open or find the image: ')
    exit(0)

decreased_brightness_image = image - 50  

decreased_brightness_image[decreased_brightness_image < 0] = 0
decreased_brightness_image[decreased_brightness_image > 255] = 255

cv.imshow('Original Image', image)
cv.imshow('Decreased Brightness Image', decreased_brightness_image)

cv.waitKey(0)
cv.destroyAllWindows()
