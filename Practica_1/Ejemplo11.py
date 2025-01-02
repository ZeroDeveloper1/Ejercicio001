import pandas as pd
import numpy as pn 
#crear una lista con datos numericos
datos = [10, 20, 30, 40, 50, 60]
#crear un dataframe con la lista de
df = pd.DataFrame(datos, columns = ["Datos"])

#mostrar dataframe
print(df)
# mostrar el dataframe

df["divisible por 2"] = df["Datos"]% 2 == 0

print(df)

