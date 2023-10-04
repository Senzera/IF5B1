import cv2 as cv
import numpy as np

image = cv.imread("gojo.png", 0)

if image is None:
    print('Could not open or find the image: ')
    exit(0)

min_intensity = np.min(image)
max_intensity = np.max(image)

new_min_intensity = 0
new_max_intensity = 255

increased_contrast_image = ((image - min_intensity) / (max_intensity - min_intensity)) * (new_max_intensity - new_min_intensity) + new_min_intensity
# Mengonversi tipe data piksel kembali ke tipe data integer (uint8)
increased_contrast_image = np.uint8(increased_contrast_image)

cv.imshow('Original Image', image)
cv.imshow('Increased Contrast Image', increased_contrast_image)

cv.waitKey(0)
cv.destroyAllWindows()
