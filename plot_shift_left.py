import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def power_function(x):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y / (np.pi/2)
    return y

def fit_func_3rd(x, a, b, c, d):
    return d*np.power(x, 3) + c*np.power(x, 2) + b*x + a

def fit_func_linear(x, a, b):
    return b*x + a


x = np.linspace(0, np.pi/3, 100)
y = power_function(x)

popt, pcov = curve_fit(fit_func_linear, y, x)
print(popt)

plt.plot(y, x)
plt.plot(y, fit_func_linear(y, *popt), 'r--')
#plt.plot(y, fit_func_linear(y, *popt) - x)
plt.show()
