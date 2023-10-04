import cv2 as cv
import numpy as np

image = cv.imread("gojo.png", 0)  

if image is None:
    print('Could not open or find the image: ')
    exit(0)

brightness_increase = 50  
brightened_image = np.clip(image + brightness_increase, 0, 255).astype(np.uint8)

cv.imshow('Original Image', image)
cv.imshow('Brightened Image', brightened_image)

cv.waitKey(0)
cv.destroyAllWindows
