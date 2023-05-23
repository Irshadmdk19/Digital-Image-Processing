import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)

# Frequency scaling factor
scale_factor = 2

# Perform frequency scaling
scaled_signal = np.interp(t * scale_factor, t, signal)

# Plot the original and scaled signals
plt.plot(t, signal, label='Original')
plt.plot(t, scaled_signal, label='Scaled')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()