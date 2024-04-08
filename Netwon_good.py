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

def Netwon(x, a):
    for i in range (100):
        x = x - (SCR_function(x, a)/Diff_func(x))
        x = x % np.pi
    return x

#x = np.linspace(0, np.pi, 100)
'''
y_1 = SCR_function(x, 0)
y_2 = linear(x)
y_3 = Netwon(y_2, y_1)
y_4 = Diff_func(x)

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_4)
plt.plot(y_3, y_1)

plt.show()
'''

power = int(input("Please input the power(in W) you want: "))
power = (power / p) * (np.pi/2)
deg_guess = linear(power)
deg_ans = Netwon(deg_guess, power)
print(deg_ans)
