import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image as grayscale
img = cv2.imread('/ci2/FTD-programs/road.jpg', 0)

# Generate a signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Rotation angle in radians
rotation_angle = np.pi/4

# Compute FFT
fft = np.fft.fft(signal)

# Frequency domain rotation
rotated_fft = fft * np.exp(-1j * rotation_angle * np.arange(len(fft)))

# Perform inverse FFT
rotated_signal = np.fft.ifft(rotated_fft)

# Plot the original and rotated signals
plt.plot(t, signal, label='Original')
plt.plot(t, rotated_signal.real, label='Rotated')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()