import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('ppg.txt')

plt.plot(data)
plt.show()