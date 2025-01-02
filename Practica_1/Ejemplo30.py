import pandas as pd
import matplotlib.pyplot as plt

# Creación del DataFrame con correcciones
paises = pd.DataFrame({
    "nombre": ["venezuela", "colombia", "peru", "ecuador", "chile"],
    "poblacion": [28.52, 50.34, 32.51, 17.64, 19.12],
    "area": [916.445, 1141.748, 1285.216, 283.561, 756.096]  # Quitamos la coma al final
})

# Gráfico con las claves corregidas
plt.bar(paises["nombre"], paises["poblacion"], color="r", label="Poblacion")
plt.bar(
    paises["nombre"],
    paises["area"],
    color="b",
    label="Area",
    bottom=paises["poblacion"],
)
plt.title("Poblacion y area de algunos paises")
plt.xlabel("Pais")
plt.ylabel("Millones de habitantes / Kilometros cuadrados")
plt.legend()
plt.show()
