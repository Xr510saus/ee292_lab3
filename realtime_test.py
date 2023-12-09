import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import ADS1256

# init ADC
ADC = ADS1256.ADS1256()
ADC.ADS1256_init()


# Set up the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data, label='Sensor Data')
ax.legend()


# Function to update the plot in real-time
def update_plot(frame):
    x_data.append(frame)

    # ADC_Value = ADC.ADS1256_GetChannalValue(0)
    ADC_Value = ADC.ADS1256_GetAll()
    ADC_Value = ADC_Value[0]*5.0/0x7fffff
    # print(ADC_Value)
    # ADC_Value = ADC_Value*5.0/0x7fffff
    y_data.append(ADC_Value)

    line.set_data(x_data[-50:], y_data[-50:])
    ax.relim()
    ax.autoscale_view()

    return line,

# Set up animation
animation = FuncAnimation(fig, update_plot, interval=0, blit=True)

# Show the plot
plt.show()
