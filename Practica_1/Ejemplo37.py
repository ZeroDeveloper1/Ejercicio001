import pandas as pd
import matplotlib.pyplot as plt
paises = pd.Series(
    [28.52, 50.34, 32.51, 17.64, 19.12],
    index=["Venezuela","Colombia", "Peru", "Ecuador","Chile"],
)

fuente_titulo = {"Family": "Serif", "Size": 14, "style": "italic" }
plt.rcParams["font.family"] = "sans-serif"
plt.plot(paises)
plt.title("Poblacion de algunos paises",fontdict=fuente_titulo)
plt.xlabel("Pais",fontsize=12)
plt.ylabel("Millones de habitantes")
plt.show()
