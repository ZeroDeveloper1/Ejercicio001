import pandas as pd
#crear un diccionario con los datos de la temperatura
datos = {
    "Meses": ["Ene.","Feb.","Marz","Abr.","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
    "Maxima": [ 32, 32, 33, 33, 33, 33, 34, 34, 33, 32, 32, 32],
    "Temperatura": [ 28, 28, 28, 29, 29, 29, 29, 30, 29, 28, 28, 28],
    "Minima": [24, 24, 25, 26, 26, 26, 26, 26, 26, 25, 25, 24],
}
#crear un dataframe con el diccionario
temperaturas = pd.DataFrame(datos)
# usar un funcion lamba para calcular el rango de temperatura (Maxima - Minima)
#y agregarlo como una nueva columna

temperaturas["Promedio"]= temperaturas.apply(lambda x: x["Maxima"] -  x["Minima"]/ 2,axis=1)
print(temperaturas)