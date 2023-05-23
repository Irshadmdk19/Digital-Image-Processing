import numpy as np
import matplotlib.pyplot as plt

# Generate a frequency domain signal
freq = np.fft.fftfreq(1000, 1 / 1000)
signal_freq = np.exp(-0.2 * np.abs(freq))

# Compute IFFT
signal = np.fft.ifft(signal_freq)

# Plot the time domain signal
plt.plot(signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()