import matplotlib.pyplot as plt
import numpy as np

p = 250

def linear(x):
    y = (np.pi / 2) - ((x*np.pi/2) / np.pi)
    return y

def Diff_func(x):
    y = -np.power(np.sin(x), 2)
    return y

def SCR_function(x, a):
    y = -(np.sin(2*x) / 4) + (x/2)
    y = (np.pi / 2) - y
    y = y-a
    return y

def Netwon(x_guess, a):
    for i in range (15):
        x_guess = x_guess - (SCR_function(x_guess, a)/Diff_func(x_guess))
        x_guess = x_guess % np.pi
    x_ans = x_guess
    return x_ans

def AC_function(x):
    y = (110 * 110 * 2/ 48.4) * np.power(np.sin(x), 2)
    return y

x = np.linspace(0, np.pi, 100)

# target
y_target = SCR_function(x, 0)

# Netwon method result
x_guess = linear(y_target)
x_ans = Netwon(x_guess, y_target)

# Evulate result from Netwon method
x_eval = np.linspace(x_ans, np.pi, 100)
y_eval = AC_function(x_eval)
y_ans = np.trapz(y_eval, x_eval) / np.pi

# Calculate difference between result and target
y_target = y_target * (250 * 2 / np.pi)
y_diff = y_ans - y_target

plt.plot(y_diff)
plt.show()
