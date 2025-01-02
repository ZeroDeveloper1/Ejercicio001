import pandas as pd
import matplotlib.pyplot as plt
aises = pd.Series(
    [28.52, 50.34, 32.51, 17.64, 19.12],
    index=["Venezuela","Colombia", "Peru", "Ecuador","Chile"],
)
plt.ion()# se activa el modo interactivo
#se crea el grafico de linea y se guarda el artista de la linea en una varibale
(linea,) = plt.plot(paises)
plt.show() # se muestra el grafica
linea.set_color ("red")#se cambio el color de la linea a rojo
plt.draw() # se actualizo el grafico

