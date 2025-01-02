import pandas as pd
#Leer el archivo de JSON y guardar el resultado en un Dataframe
utiles_escolares  = pd.read_json("Utiles.json")

# se imprime el contenido de archivos utilies .json
print(utiles_escolares)

#mostrar las primeras filas de dataframe
utiles_escolares.head()
