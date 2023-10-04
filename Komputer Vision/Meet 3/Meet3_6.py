import cv2 as cv
import numpy as np

image = cv.imread("gojo.png")

if image is None:
    print('Could not open or find the image: ')
    exit(0)

# Menggunakan kontrast stretching untuk meningkatkan kontras dalam setiap saluran warna (R, G, B)
increased_contrast_image = np.zeros_like(image)

for channel in range(3):  # Loop untuk masing-masing saluran warna (R, G, B)
    min_intensity = np.min(image[:, :, channel])
    max_intensity = np.max(image[:, :, channel])

    # Menentukan nilai intensitas piksel minimum dan maksimum yang baru
    new_min_intensity = 0
    new_max_intensity = 255

    # Melakukan normalisasi histogram dalam saluran warna tertentu
    channel_contrast = ((image[:, :, channel] - min_intensity) / (max_intensity - min_intensity)) * (new_max_intensity - new_min_intensity) + new_min_intensity

    # Menyimpan hasil normalisasi ke dalam gambar berwarna yang ditingkatkan kontras
    increased_contrast_image[:, :, channel] = np.uint8(channel_contrast)

cv.imshow('Original Image', image)
cv.imshow('Increased Contrast Image', increased_contrast_image)

cv.waitKey(0)
cv.destroyAllWindows()
