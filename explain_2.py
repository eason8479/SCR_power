import matplotlib.pyplot as plt
import math
import numpy as np

x = np.arange(0, math.pi, 0.01)
y = [(1 + math.sin(2*i)/(2*math.pi) - i/math.pi) for i in x]

plt.plot(x, y)
plt.show()

power = [250 * i for i in y]

plt.plot(x, power)
plt.show()

plt.plot(power, x)
plt.show()
