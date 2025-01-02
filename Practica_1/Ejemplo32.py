import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#se crea un serie con 100 valores aleatorios entre 18 y 65
edades = pd.Series(np.random.randint(18, 65, size=100))
plt.hist(edades, bins=10, color = "g")
plt.title("Edades de 100 persona")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
