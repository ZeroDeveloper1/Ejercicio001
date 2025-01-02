#Importar la libreria pandas
import pandas as pd
#Leer el archivo de excel y guardar el resultado en un datframe (Paises)
paises = pd.read_excel("paises.xlsx")
print(paises)

paises.head()
