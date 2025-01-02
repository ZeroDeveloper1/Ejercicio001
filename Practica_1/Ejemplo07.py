import pandas as pd
#crear un dicionario con los datos de frutas y cantidad
datos = {
   "Frutas": ["Manzana","pera","Mandarina","naranja","piña"], "Cantidad": [50, 20, 30, 40, 20]
    
}
# crear un dataframe con el diccionario sin especificar el indice
fruteria = pd.DataFrame(datos)
#MOSTRAR FRAME
print(fruteria)

#agregar un nuevo campo con los datos de precios
precios = [0.5, 0.4, 0.3, 0.2, 0.6]
fruteria = fruteria.assign(precios = precios)
#mostrar el dataframe con el nuevo campo
print(fruteria)

#crear un nuevo campo que sea el producto de los campos y precios
fruteria["Total productos"] = fruteria["Cantidad"] * fruteckeria["Precios"]

#mostrar dataframe con el nuevo campo
print(fruteria)
