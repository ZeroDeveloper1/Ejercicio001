#Ejemplo06
import pandas as pd
#crear un diccionario con los datos de frutas y cantidades
datos = {
    "Frutas": ["Manzana","pera","Mandarina","naranja","piña"], "Cantidad": [50, 20, 30, 40, 20]
}
#Crear un dataframe con el diccionario sin especificar el indice
fruteria = pd.DataFrame(datos)
#mostrar el data frame
print(fruteria)
