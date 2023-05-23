import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image as grayscale
img = cv2.imread('/ci2/FTD-programs/road.jpg', 0)

# Perform FFT
fft_img = np.fft.fft2(img)
fft_shifted = np.fft.fftshift(fft_img)

# Compute the magnitude spectrum
magnitude_spectrum = 20 * np.log(np.abs(fft_shifted))

# Display the magnitude spectrum
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.colorbar()
plt.show()

# Amplitude scaling factor (adjust as needed)
scaling_factor = 2.0

# Scale the magnitude spectrum
scaled_spectrum = magnitude_spectrum * scaling_factor

# Display the scaled magnitude spectrum
plt.imshow(scaled_spectrum, cmap='gray')
plt.title('Scaled Magnitude Spectrum')
plt.colorbar()
plt.show()
