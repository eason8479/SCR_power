# draw two plot
# one is f(x)=110*(2**0.5)*sin(x)
# with name "原始市電波形"
# another is f(x)=110*(2**0.5)*abs(sin(x))
# with name "整流後波形"

import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.font_manager import FontProperties as font

font1 = font(fname=r"c:\windows\fonts\kaiu.ttf", size=14)

# plot f(x)=110*(2**0.5)*sin(x)
# with name "原始市電波形"
x = np.arange(0,(2/60)*1000,0.01)
y = [110*(2**0.5)*math.sin((i/(1000/60))*2*math.pi) for i in x]
plt.plot(x,y)
plt.title("市電波形", fontproperties=font1)
plt.xlabel("時間(ms)", fontproperties=font1)
plt.ylabel("電壓(V)", fontproperties=font1)
plt.show()

# plot f(x)=110*(2**0.5)*abs(sin(x))
# with name "整流後波形"
y = [110*(2**0.5)*abs(math.sin((i/(1000/60))*2*math.pi)) for i in x]
plt.plot(x,y)
plt.title("整流後波形", fontproperties=font1)
plt.xlabel("時間(ms)", fontproperties=font1)
plt.ylabel("電壓(V)", fontproperties=font1)
plt.show()

def f(a,b):
    if a%180 > b:
        return 110*(2**0.5)*abs(math.sin((a/(1000/60))*2*math.pi))
    else:
        return 0
