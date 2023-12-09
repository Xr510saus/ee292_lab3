import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import ADS1256

with open('ppg.txt', 'w') as file:
    pass

fs = 125
T = 1/(fs+2)

# init ADC
ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_SetChannal(0)

length = 4096
data = np.ones(length)

dts = []

init_time = time.time()

for x in range(length):
    if x == 0:
        prev_time = time.time()
    else:
        dt = time.time()-prev_time

        if dt < T:
            time.sleep(T - dt)

        #dts.append(time.time() - prev_time)
        prev_time = time.time()

    data[x] = ADC.ADS1256_Read_ADC_Data() * 5.0/0x7fffff

#print("Avg SR: ", 1/np.mean(dts))
print("Total time taken: ", time.time() - init_time)

print("Writing to File")
for x in range(length):
    with open('ppg.txt', 'a') as file:
        file.write('%f' % data[x])
        file.write('\n')