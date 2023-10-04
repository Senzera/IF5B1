import cv2 as cv
import numpy as np

image = cv.imread("gojo.png")

if image is None:
    print('Could not open or find the image: ')
    exit(0)


negative_image = np.zeros_like(image)

negative_image[:, :, 0] = 255 - image[:, :, 0]  # (Red)
negative_image[:, :, 1] = 255 - image[:, :, 1]  # (Green)
negative_image[:, :, 2] = 255 - image[:, :, 2]  # (Blue)

cv.imshow('Original Image', image)
cv.imshow('Negative Image', negative_image)

cv.waitKey(0)
cv.destroyAllWindows()
