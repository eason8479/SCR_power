import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def power_function(x):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y / (np.pi/2)
    return y

def shift_x(x):
    return x - np.pi/2

def shift_y(y):
    return y-0.5

def fit_func_3rd(x, a, b, c):
    return c*np.power(x, 3) + b*x + a

# mid part of curve
x = np.linspace(np.pi/3, 2*(np.pi/3), 100)
y = power_function(x)

# shift x and y
x = shift_x(x)
y = shift_y(y)

popt, pcov = curve_fit(fit_func_3rd, y, x)
print(popt)

#plt.plot(y, x)
#plt.plot(y, fit_func_3rd(y, *popt), 'r--')
plt.plot(y, fit_func_3rd(y, *popt) - x)
plt.show()
