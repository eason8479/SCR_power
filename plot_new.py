import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import optimize

def power_function(x):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y/(np.pi/2)
    return y

def linear(x):
    y = (x*np.pi/2) / np.pi
    return y

def Diff_func(x):
    y = np.power(np.sin(x), 2)
    return y

def SCR_function(x, a):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y-a
    return y

def Netwon(x, a):
    for i in range (5):
        x = x - (SCR_function(x, a)/Diff_func(x))
    return x

x = np.linspace(0, np.pi, 100)

y_1 = SCR_function(x, 0)
y_2 = linear(x)
y_3 = Netwon(y_2, y_1)

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(y_3, y_1)

plt.show()
