import cv2 as cv
import numpy as np

image = cv.imread("gojo.png")

if image is None:
    print('Could not open or find the image: ')
    exit(0)

# Mengurangi kontras dalam setiap saluran warna (R, G, B)
decreased_contrast_image = np.zeros_like(image)

for channel in range(3):  # Loop untuk masing-masing saluran warna (R, G, B)
    # Mengurangkan kontras dalam saluran warna tertentu dengan mengalikan nilai piksel dengan faktor kurang dari 1
    factor = 0.7  # Anda dapat mengganti faktor ini sesuai dengan seberapa banyak Anda ingin mengurangi kontras
    channel_contrast = image[:, :, channel] * factor

    # Memastikan nilai piksel tetap dalam rentang 0 hingga 255
    channel_contrast[channel_contrast < 0] = 0
    channel_contrast[channel_contrast > 255] = 255

    # Menyimpan hasil pengurangan kontras ke dalam gambar berwarna yang kontrasnya dikurangi
    decreased_contrast_image[:, :, channel] = np.uint8(channel_contrast)

cv.imshow('Original Image', image)
cv.imshow('Decreased Contrast Image', decreased_contrast_image)

cv.waitKey(0)
cv.destroyAllWindows()
