import pandas as pd
import matplotlib.pyplot as plt
paises = pd.Series(
    [28.52, 50.34, 32.51, 17.64, 19.12],
    index=["Venezuela","Colombia", "Peru", "Ecuador","Chile"],
)
plt.plot(
    paises, "b-"
)
plt.title("Poblacion de algunos paises")
plt.xlabel("Pais")
plt.ylabel("Millones de habitaciones")
plt.show()

