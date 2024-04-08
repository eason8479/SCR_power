import matplotlib.pyplot as plt
import numpy as np

p_1 = 250 / (np.pi / 2)
p_2 = (110 * 110 ) / 48.4

def linear(x):
    y = (x*np.pi/2) / np.pi
    y = y * p_1
    return y

def Diff_func(x):
    y = np.power(np.sin(x), 2)
    y = y * p_2
    return y

def SCR_function(x, a):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = y * p_1
    y = y-a
    return y

def Netwon(x, a):
    for i in range (10):
        x = x - (SCR_function(x, a)/Diff_func(x))
        x = x % np.pi
    return x

x = np.linspace(0, np.pi, 1000)

y_1 = SCR_function(x, 0)
y_2 = linear(x)
# Netwon(y_2, y_1)
y_3 = Diff_func(x)

x_guess = Netwon(y_2, y_1)

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)
#plt.plot(y_3, y_1)
plt.plot(x_guess, y_1)

plt.show()
