import matplotlib.pyplot as plt
import numpy as np
import math

p = 250

def linear(x):
    y = np.pi - x
    return y

def Diff_func(x):
    y = np.cos(2*x) - 1
    return y

def SCR_function(x, a):
    y = np.pi + np.sin(2*x)/2 - x
    y = y-a
    return y

def Netwon(x_guess, a):
    for i in range (10):
        x_guess = x_guess - (SCR_function(x_guess, a)/(Diff_func(x_guess)))
        x_guess = x_guess % np.pi
    x_ans = x_guess
    return x_ans

x = np.linspace(0, np.pi, 100)
x = x[1:-1]
y_target = SCR_function(x, 0)

plt.plot(x, y_target)
plt.show()

x_guess = linear(x)
x_ans = Netwon(x_guess, y_target)
y_ans = SCR_function(x_ans, 0)

plt.plot(x_ans, y_ans)
plt.plot(x, y_target)
plt.show()

y_diff = y_ans - y_target
plt.plot(250*y_target, 250*y_diff)
plt.show()
