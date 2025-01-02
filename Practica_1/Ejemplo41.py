import numpy as pn
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
paises = pd.Series(
    [28.52, 50.34, 32.51, 17.64, 19.12],
    index=["Venezuela","Colombia", "Peru", "Ecuador","Chile"],
)
#se crea la figura y el eje donde se va a dibujar la animacion
fig, ax = plt.subplot()

#se crea el artista de tipo lena con los datos iniciales de la serie paises
(line,) = ax.plot(paises.index, paises,"r")

def animate(i):
    paises_mod = paises + np.random.uniform(-0.5,0.5,size = len(paises))
    line.set_ydata(paises_mod)
    return (line,)

ani = animation.FuncAnimation(fig,animate,frames=100, interval=100)
plt.show()

