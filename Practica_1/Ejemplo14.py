import pandas as pd
#crear un diccionario con los datos de la temperatura
datos = {
    "Meses": ["Ene.","Feb.","Marz","Abr.","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
    "Maxima": [ 32, 32, 33, 33, 33, 33, 34, 34, 33, 32, 32, 32],
    "Temperatura": [ 28, 28, 28, 29, 29, 29, 29, 30, 29, 28, 28, 28],
    "Minima": [24, 24, 25, 26, 26, 26, 26, 26, 26, 25, 25, 24],
}
#crear un dataframe con el codigo
temperaturas = pd.DataFrame(datos)

#calcular la media de los campos maximo, temperatura y minima
maximo = temperaturas.max(axis=0)
minimo = temperaturas.min(axis=0)


#Mostrar resultados en una tabla
print("l  campo  l   media")
print("l  -----  l   -----")
print(f"Maxima l {maximo['Maxima']} c l{minimo['Maxima']} C L")
print(f"Temperatura l {maximo['Temperatura']} c l{minimo['Temperatura']} C L")
print(f"Minima l {maximo['Minima']} c l {minimo['Minima']} C L")
