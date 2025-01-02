import pandas as pd
import matplotlib.pyplot as plt
paises = pd.DataFrame(
    {
    "nombre": ["Venezuela", "Colombia", "Peru", "Ecuador", "Chile"],
    "Poblacion":[28.52, 50.34, 32.51, 17.64, 19.12],
    "area": [916.445, 1141.748, 1285.216, 283.561, 756.096],

    }
)
    # se crea el grafico de dispercion
plt.scatter(paises["Poblacion"],paises["area"])
plt.show()
puntos = plt.ginput(3)
print(puntos)#se imprime la lista de tuplas con las cordenadas

