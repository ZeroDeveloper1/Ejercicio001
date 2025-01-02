import pandas as pd
# crear un dataframe con algunos datos de una libreria
utiles_escolares = pd.dateframe({
    "Descripcion": ["Lapiz", "Cuaderno", "Regla", "Borrador"],
    "Codigo": [3456, 5646, 7656, 2541]
})

#escriba el dataframe en un archivo JSON llamdo utiles.jason
utiles_escolares.to_json("utiles.json")
#se guardo correctamente
print("Se guardo correctamente")
print("=======================")
print(utiles_escolares)
