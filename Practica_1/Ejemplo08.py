import pandas as pd
#crear una lista de datos numericos
datos = [10, 20, 30, 40, 50, 60]
# crear un datafrema con la lista
df = pd.DataFrame(datos, columns = ["datos del Dataframe"])
#mostrar el dataframe
print(df)
