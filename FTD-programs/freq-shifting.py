import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
t = np.linspace(0, 1, 1000)
frequency = 10  # Original frequency in Hz
signal = np.sin(2 * np.pi * frequency * t)

# Frequency shift factor
shift_factor = 5  # Amount of frequency shift in Hz

# Perform frequency shifting
shifted_signal = np.sin(2 * np.pi * (frequency + shift_factor) * t)

# Plot the original and shifted signals
plt.plot(t, signal, label='Original')
plt.plot(t, shifted_signal, label='Shifted')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()