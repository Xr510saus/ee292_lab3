import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft, fftfreq

# TODO: convert max HRV to diff from mean
# TODO: use dB scale for amplitude in FFT plots

### --------------------------------- PART A : Time Domain -------------------------------- ###

fs = 125 # sampling freq 125 Hz
ppg_data = np.loadtxt('NabidFastRocking.txt') # load in data, CHOOSE PROPER TEXT FILE
ts = np.arange(0, len(ppg_data)*1/fs, 1/fs)

N = 8
ppg_data_smooth = np.convolve(ppg_data, np.ones(N)/N, mode='valid')

peaks, _ = find_peaks(ppg_data, height=3.4)

peak_diffs = np.diff(peaks * 1/fs)

avg_HR = 60.0 / np.mean(peak_diffs)
print(f'Avg Heart Rate (time analysis) = {avg_HR} bpm')

max_hrv = np.max(np.abs(peak_diffs - np.mean(peak_diffs)))
print(f'Max HRV = {max_hrv} seconds')

hrv = peak_diffs - np.mean(peak_diffs)
rms_hrv = np.sqrt(np.sum(hrv**2)/len(hrv))
print(f'RMS HRV = {rms_hrv} seconds')

# print(peak_diffs)
# print(np.mean(60.0 / peak_diffs))

plt.figure()
plt.plot(ts,ppg_data)
# plt.plot(ts[:1017], ppg_data_smooth)
# plt.plot(peaks*1/fs, ppg_data[peaks], "x")
plt.xlabel('Time (s)')
plt.title('PPG Finger: Fast Rocking')
plt.legend(['Raw','Peaks'])
# plt.legend(['Raw','MovingAvg'])

### ------------------------------- PART B : Frequency Domain ------------------------------- ###
window = np.hanning(len(ppg_data))
ppg_data_windowed = ppg_data * window

fft_values = fft(ppg_data_windowed)
fft_freqs = fftfreq(len(ppg_data), d=1/fs)
mask_freqs = fft_freqs[(fft_freqs > 0.5) & (fft_freqs < 2)] # include freqs in human range of 0.5 - 4 Hz only
mask_fftvals = fft_values[(fft_freqs > 0.5) & (fft_freqs < 2)]
# print(mask_freqs)

heart_rate = mask_freqs[np.argmax(np.abs(mask_fftvals)[:len(mask_fftvals)//2])] * 60.0
print(f'Avg Heart Rate (freq analysis) = {heart_rate} bpm')

plt.figure()
plt.plot(fft_freqs[:len(fft_freqs)//2], np.abs(fft_values)[:len(fft_values)//2])
plt.plot(mask_freqs, np.abs(mask_fftvals))
plt.title('FFT of PPG Finger: Fast Rocking')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend(['Raw', 'Bandpass'])

plt.figure()
plt.plot(mask_freqs, np.abs(mask_fftvals))
plt.title('Band-Passed 0.5-2Hz FFT of PPG Finger: Fast Rocking')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()