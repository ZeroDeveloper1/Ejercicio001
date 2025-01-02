import pandas as pd
import numpy as np
#crear una lista de datos numericos
datos = [10, 20, 30, 40, 50, 60]
# crear un datafrema con la lista
df = pd.DataFrame(datos, columns = ["Datos"])
#mostrar el dataframe
print(df)

#calcular el logaritmo de los datos y colocar el resultado en una columna nueva
df["Logaritmo"] = np.log(df["Datos"])
#Mostrar  el dataframe con la nueva columna
print(df)cle