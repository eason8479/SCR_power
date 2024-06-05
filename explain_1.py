import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.font_manager import FontProperties as font

plt.rc('font', size=20)
plt.xlim([0, math.pi])

x = np.arange(0, math.pi, 0.01)
y = [math.sin(i)**2 for i in x]
y_0 = [0 for i in x]

t = 1 
plt.fill_between(x, y, 0, where = (x > t), color='green', alpha=0.5)

plt.plot(x, y)
plt.plot(x, y_0, color = "black")
plt.title("g(t) in the range 0 ~ pi")

plt.xlabel("t(deg)")
plt.ylabel("g(t)")
plt.show()
