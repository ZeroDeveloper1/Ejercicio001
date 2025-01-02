import pandas as pd
import matplotlib.pyplot as plt

paises = pd.Series([25.52, 50.34, 32.51, 17.64, 19.12], index =["venezuela","Colombia", "Peru","Ecuador", "Chile"])
paises.plot(kind="Line", title="Poblacion de algunos paises", xlabel="Pais", ylabel = "Millones de habitantes")
plt.show()
