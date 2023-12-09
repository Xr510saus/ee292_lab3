import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

sr = 125
lowcut = 0.5
highcut = 2
nds = 50

data = np.loadtxt('NabidWrist.txt')

fft = np.fft.fft(data)
n = len(fft)
w = np.fft.fftfreq(n, d=1/sr)[:n//2]
fft = abs(fft[:n//2])

plt.figure()
#plt.plot(w[(w > 0.5) & (w < 2)], abs(fft)[(w > 0.5) & (w < 2)])
plt.plot(w[1:], fft[1:])
plt.title('Unfiltered Wrist FFT')

midx = np.argmax(fft[(w > 0.5) & (w < 2)])
wf = w[(w > 0.5) & (w < 2)][midx]
print('HR: ', 60*wf)

plt.show()