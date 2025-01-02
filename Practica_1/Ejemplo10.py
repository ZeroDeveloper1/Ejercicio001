import pandas as pd
import numpy as np
#crear una lista de datos numericos
datos = [10, 20, 30, 40, 50, 60]
# crear un datafrema con la lista
df = pd.DataFrame(datos, columns = ["Datos"])
#mostrar el dataframe
print(df)

#observar en el campo cual valoo es mayor a 30
df["Mayor a 30"] = df["Datos"] > 30

# mostrar el dataframe con la nueva columna 
print(df)
