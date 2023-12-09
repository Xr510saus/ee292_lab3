import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft, fftfreq


### --------------------------------- PART A : Time Domain -------------------------------- ###

fs = 125 # sampling freq 125 Hz
ppg_data_raw = np.loadtxt('NabidLongDataFinger.txt') # load in data
ts = np.arange(0, len(ppg_data_raw)*1/fs, 1/fs)

N = 10

ppg_data = np.convolve(ppg_data_raw, np.ones(N)/N, mode='valid')

plt.figure()
plt.plot(ppg_data)
plt.plot(ppg_data_raw)
plt.legend(['3-pt MovingAvg', 'Raw'])
plt.ylabel('Voltage')
plt.title('Raw vs Moving Avg PPG')


peaks, _ = find_peaks(ppg_data, height=3.35)

peak_diffs = np.diff(peaks * 1/fs)

print(f'peak_diffs(ms) = {peak_diffs*1e3}')

avg_HR = 60.0 / np.mean(peak_diffs)
print(f'Avg Heart Rate (time analysis) = {avg_HR} bpm')

max_hrv = np.max(np.abs(peak_diffs - np.mean(peak_diffs)))
print(f'Max HRV = {max_hrv*1e3} ms')

hrv = peak_diffs - np.mean(peak_diffs)
rms_hrv = np.sqrt(np.sum(hrv**2)/len(hrv))
print(f'RMS HRV = {rms_hrv*1e3} ms')

# print(peak_diffs)
# print(np.mean(60.0 / peak_diffs))

plt.figure()
plt.plot(ts[:len(ppg_data)],ppg_data)
plt.plot(peaks*1/fs, ppg_data[peaks], "x")
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('PPG')
plt.legend(['Raw','Peaks'])

plt.show()