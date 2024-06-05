import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.font_manager import FontProperties as font

font1 = font(fname=r"c:\windows\fonts\kaiu.ttf", size=14)

# create a function that return absolute value of sine of x
def abs_sin(x):
    if 0 <= x <= 180:
        return abs(math.sin(x/(180/math.pi)))
    else:
        return math.sin((x%180)/(180/math.pi))

# create a function that take two number a,b as input
# if a%180 > b return 110*(2**0.5)*abs(sin(a))
# else return 0
def f(a,b):
    if a%180 > b:
        return 110*(2**0.5)*abs_sin(a)
    else:
        return 0

# calculate the RMS value of f from 0 to 720, with step 0.1
# with b form 0 to 180, with step 1
# plot the result with name "經SCR在不同相位下截波的RMS電壓值"
x = np.arange(0,720,0.1)
b = np.arange(0,180,1)
rms = []

y = [f(i,45) for i in x]
plt.plot(x,y)
plt.title("與0點相位差45度下截波的波形圖", fontproperties=font1)
plt.xlabel("相位角(degree)", fontproperties=font1)
plt.ylabel("電壓(V)", fontproperties=font1)
plt.show()

for i in b:
    rms.append(np.sqrt(np.mean(np.square([f(j,i) for j in x]))))

plt.plot(b,rms)
plt.title("不同相位差下截波後的RMS電壓值", fontproperties=font1)
plt.xlabel("相位差(degree)", fontproperties=font1)
plt.ylabel("RMS電壓值(V)", fontproperties=font1)
plt.show()

# take rms as voltage, calculate the power assume it pass 50 ohm resistor
# plot the result with name "經SCR在不同相位下截波的平均功率"
power = [i**2/50 for i in rms]
plt.plot(b,power)
plt.title("不同相位差下截波後的平均功率(負載=50ohm)", fontproperties=font1)
plt.xlabel("相位差(degree)", fontproperties=font1)
plt.ylabel("平均功率(W)", fontproperties=font1)
plt.show()

# save power and matching i to a csv file
# with name "平均功率.csv"
import csv
with open("平均功率.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["相位角", "平均功率"])
    for i in range(len(b)):
        writer.writerow([b[i], power[i]])
