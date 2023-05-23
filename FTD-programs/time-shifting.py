import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Time shift factor
shift_factor = 0.3

# Perform time shifting
shifted_signal = np.interp(t - shift_factor, t, signal)

# Plot the original and shifted signals
plt.plot(t, signal, label='Original')
plt.plot(t, shifted_signal, label='Shifted')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()