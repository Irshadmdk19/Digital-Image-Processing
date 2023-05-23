import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Time scaling factor
scale_factor = 2

# Perform time scaling
scaled_signal = np.interp(scale_factor * t, t, signal)

# Plot the original and scaled signals
plt.plot(t, signal, label='Original')
plt.plot(t, scaled_signal, label='Scaled')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()