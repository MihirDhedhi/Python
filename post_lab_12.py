import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
f1 = 5
f2 = 10
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
result_signal = signal1 + signal2
plt.figure(figsize=(10, 5))
plt.plot(t, result_signal)
plt.title("Combined Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()





import numpy as np
import matplotlib.pyplot as plt
fs = 500
duration = 2
t = np.linspace(0, duration, fs * duration, endpoint=False)
f_sine = 5
f_cosine = 10
sine_wave = np.sin(2 * np.pi * f_sine * t)
cosine_wave = np.cos(2 * np.pi * f_cosine * t)
multiplied_signal = sine_wave * cosine_wave
plt.figure(figsize=(10, 5))
plt.plot(t, multiplied_signal)
plt.title("Product of Sine and Cosine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
fs = 100
duration = 1
t = np.linspace(0, duration, fs * duration, endpoint=False)
f = 5
shift = 0.1
original_signal = np.sin(2 * np.pi * f * t)
shifted_signal = np.sin(2 * np.pi * f * (t - shift))
plt.figure(figsize=(10, 5))
plt.plot(t, original_signal, label="Original Signal")
plt.plot(t, shifted_signal, label="Shifted Signal (0.1s)")
plt.title("Time Shift of a Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
fs = 1000  # Sampling frequency
duration = 1  # 1 second
t = np.linspace(0, duration, fs * duration, endpoint=False)
f = 10  # Frequency in Hz
original_signal = np.sin(2 * np.pi * f * t)
scaled_signal = 3 * original_signal
plt.figure(figsize=(10, 5))
plt.plot(t, original_signal, label="Original Signal")
plt.plot(t, scaled_signal, label="Scaled Signal (x3)")
plt.title("Amplitude Scaling of a Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()









import numpy as np
import matplotlib.pyplot as plt
fs = 1000  # Sampling frequency
duration = 1  # 1 second
t = np.linspace(0, duration, fs * duration, endpoint=False)
f = 5  # Frequency in Hz
original_signal = np.sin(2 * np.pi * f * t)
reversed_signal = original_signal[::-1]
plt.figure(figsize=(10, 5))
plt.plot(t, original_signal, label="Original Signal")
plt.plot(t, reversed_signal, label="Reversed Signal")
plt.title("Time Reversal of a Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()





















