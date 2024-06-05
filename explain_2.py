import matplotlib.pyplot as plt
import math
import numpy as np

x = np.arange(0, math.pi, 0.01)
y = [(math.pi/2 + math.sin(2*i)/4 - i/2) for i in x]

plt.plot(x, y)
plt.show()

power = [250 * (i*2/math.pi) for i in y]

plt.plot(x, power)
plt.show()

plt.plot(power, x)
plt.show()
