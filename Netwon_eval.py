import matplotlib.pyplot as plt
import numpy as np
import math

p = 250

def linear(x):
    y = 1 - (x / np.pi)
    return y

def Diff_func(x):
    y = (np.cos(2*x) - 1) / np.pi
    return y

def SCR_function(x, a):
    y = 1 + np.sin(2*x)/(2*np.pi) - x/np.pi
    y = y-a
    return y

def Netwon(x_guess, a):
    for i in range (8):
        x_guess = x_guess - (SCR_function(x_guess, a)/(Diff_func(x_guess)))
        x_guess = x_guess % np.pi
    x_ans = x_guess
    return x_ans

x = np.linspace(0, np.pi, 100)
x = x[1:-1]
y_target = SCR_function(x, 0)

x_guess = linear(x)
x_ans1 = Netwon(x_guess, y_target)
y_ans1 = SCR_function(x_ans1, 0)

x_ans2 = Netwon(1e-6, y_target)
y_ans2 = SCR_function(x_ans2, 0)

'''
plt.plot(x_ans, y_ans)
plt.plot(x, y_target)
'''
y_diff1 = y_ans1 - y_target
y_diff1 = 250*y_diff1
y_diff2 = y_ans2 - y_target
y_diff2 = 250*y_diff2

plt.plot(x, y_diff1)
plt.plot(x, y_diff2)
plt.show()
