import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def power_function(x):
    y = -(np.sin(2*x) / 4) + (x/2)
    return y

def fit_func_3rd(x, a, b, c):
    return c*np.power(x, 3) + b*x + a

def fit_func_5th(x, a, b, c, d, e, f):
    return f*np.power(x, 5) + e*np.power(x, 4) + d*np.power(x, 3) + c*np.power(x, 2) + b*x + a

#x = np.linspace(0, np.pi/3, 100)
x = np.linspace(np.pi/5, 4*(np.pi/5), 100)
#x = np.linspace(2*(np.pi/3), np.pi, 100)
y = power_function(x)

popt, pcov = curve_fit(fit_func_5th, y, x)
print(popt)

plt.plot(y, x)
plt.plot(y, fit_func_5th(y, *popt), 'r--')
plt.show()
