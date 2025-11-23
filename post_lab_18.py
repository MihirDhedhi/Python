import numpy as np
import librosa
import matplotlib.pyplot as plt

audio, sr = librosa.load("M1.wav", sr=None)
ir, sr2 = librosa.load("I1.wav", sr=None)

linear_conv = np.convolve(audio, ir)

N = max(len(audio), len(ir))
a = np.pad(audio, (0, N - len(audio)))
b = np.pad(ir, (0, N - len(ir)))
circular_conv = np.real(np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)))

plt.plot(linear_conv)
plt.title("Linear Convolution")
plt.show()

plt.plot(circular_conv)
plt.title("Circular Convolution")
plt.show()





import numpy as np
import librosa
import matplotlib.pyplot as plt

x, sr = librosa.load("clean_audio.wav", sr=None)
y, sr2 = librosa.load("noisy_audio.wav", sr=None)
z, sr3 = librosa.load("periodic_audio.wav", sr=None)

cross_corr = np.correlate(x, y, mode="full")
auto_corr_clean = np.correlate(x, x, mode="full")
auto_corr_periodic = np.correlate(z, z, mode="full")

plt.plot(cross_corr)
plt.title("Cross-Correlation (Clean vs Noisy)")
plt.show()

plt.plot(auto_corr_clean)
plt.title("Autocorrelation (Clean Audio)")
plt.show()

plt.plot(auto_corr_periodic)
plt.title("Autocorrelation (Periodic Audio)")
plt.show()













