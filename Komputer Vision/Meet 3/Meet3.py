import cv2 as cv
import numpy as np

image = cv.imread("gojo.png", 0)
if image is None:
    print('Could not open or find the image: ')
    exit(0)

new_image = np.zeros(image.shape, image.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        new_image[y, x] = 255 - image[y, x]

cv.imshow('Original Image', image)
cv.imshow('Negative Image', new_image)
# Wait until user prerss some key
cv.waitKey()