import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def power_function(x):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y / (np.pi/2)
    return y

def shift_x(x):
    return x - np.pi/3 - 10

def shift_y(y):
    return y - power_function(np.pi/3) - 3

def fit_func_linear(x, a, b):
    return b*x + a

def fit_func_3rd(x, a, b, c):
    return c*np.power(x, 3) + b*x + a

def fit_func_5th(x, a, b, c, d, e, f):
    return f*np.power(x, 10) + e*np.power(x, 8) + d*np.power(x, 6) + c*np.power(x, 4) + b*np.power(x, 2) + a

def fit_func_test(x, a, b, c, d, e):
    return a*np.power(b*x+c, d) + e
    #return a*np.log(b*np.power(x, 2) + c*np.power(x, 1) + d) + e

x = np.linspace(0, np.pi/3, 100)
#x = np.linspace(2*(np.pi/3), np.pi, 100)
#x = np.linspace(0, np.pi, 100)
y = power_function(x)

# shift x and y
x = shift_x(x)
y = shift_y(y)

popt, pcov = curve_fit(fit_func_5th, y, x)
print(popt)

plt.plot(y, x)
plt.plot(y, fit_func_5th(y, *popt), 'r--')
#plt.plot(y, fit_func_test(y, *popt) - x)
plt.show()
