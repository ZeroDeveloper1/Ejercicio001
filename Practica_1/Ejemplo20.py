import pandas as pd
#Crear un datafframe con algunos datos

ventas = pd.DataFrame({
    "descripcion": ["Productos1","Productos2","Productos3"],
    "venta":[3456,5646,7656]
})
#Escribir el dataframe en un archivo de excel llamado ventas.xlsx
ventas.to_excel("ventas.xlsx")
#mostrar el contenido que se guarda en ventas.xlsx
print(ventas)
