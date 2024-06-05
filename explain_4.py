import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.font_manager import FontProperties as font

init_temp = 15
def power_function(current_temp, target_temp, init_temp):
    max_power = 250
    if(current_temp <= init_temp):
        return max_power
    elif(current_temp >= target_temp):
        return 0 
    else:
        diff_current = target_temp - current_temp
        diff_init = target_temp - init_temp
        if(target_temp - current_temp <= 3):
            return 150 * (np.power(diff_current, 2)/np.power(diff_init, 2)) + 10
        else:
            return min(250 * (np.power(diff_current, 2)/np.power(diff_init, 2)) + 10, max_power)

current_temp = np.arange(10, 50, 0.01)
output_power_1 = [power_function(i, 25, init_temp) for i in current_temp]
output_power_2 = [power_function(i, 30, init_temp) for i in current_temp]
output_power_3 = [power_function(i, 35, init_temp) for i in current_temp]
output_power_4 = [power_function(i, 40, init_temp) for i in current_temp]
output_power_5 = [power_function(i, 45, init_temp) for i in current_temp]

plt.plot(current_temp, output_power_1, label="target=25")
plt.plot(current_temp, output_power_2, label="target=30")
plt.plot(current_temp, output_power_3, label="target=35")
plt.plot(current_temp, output_power_4, label="target=40")
plt.plot(current_temp, output_power_5, label="target=45")
plt.xlabel("Current temperature(unit:Celsius)")
plt.ylabel("Output power(unit:watt)")
plt.title("Power control function under different target\n(Init temperature = 15)")
plt.grid()
plt.show()
