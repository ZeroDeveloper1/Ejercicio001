import pandas as pd
from pandas.core import series
#Importacion de ficheros datos-colesterol.csv
df_colesterol = pd.read_csv("colesterol.csv")
print(".info()")
print("-------")
print("Devuelve informacion: numero de filas, numoero de ccomlunas")
print("indices, tipo de las columnas y memoria usado")
print("-------------------------------------------------")
print(df_colesterol.info())
print("====================================================================")
print(".head()")
print("------------")
print("Devuleve las n primeras filas del dataframe df")
print("-------------------------------------------------")
print(df_colesterol.head)
print(".tail")
print("------")
print("devuelve las n ultimas filas del dataframe df")
print("-------------------------------------------------")
print(df_colesterol.tail())
print("===================================================================")
print(".shape")
print("--------")
print(df_colesterol.shape)
print("===================================================================")
print(".size")
print("-------")
print("devueleve el numero de elementos de l dataframe")
print("------------------------------------------------")
print(df_colesterol.size)
print("===================================================================")
print(".dtypes")
print("---------")
print("devuelve una serie con los tipos de datos de las columnas del dataframe df")
print("------------------------------------------------")
print(df_colesterol.dtypes)
print("==================================================================")
print(".columns")
print("---------")
print("Devuelve una lista con los nombres de las columnas de dataframe df")
print("---------------------------------------------------")
print(df_colesterol.columns)
print("===================================================================")
