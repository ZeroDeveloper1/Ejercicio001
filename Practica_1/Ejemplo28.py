import matplotlib.pyplot as plt 
import numpy as np
fig=plt.figure(figsize=(10,6),facecolor="lightgray")
ax1=plt.subplot(2,1,1)
ax2=plt.subplot(2,1,2)

x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
line = ax1.plot(
    x,y1, "r-"
)
bar = ax2.bar(
    x, y2, color = "b"
)
plt.show()
