import pandas as pd 
paises = pd.DataFrame({"Nombre": ["America","America", "America","America","America"], "Poblacion":[25.52, 50.34, 32.51, 17.64,19.12],"area":[916.445, 1141.748,1285.216, 283.561, 756.096]})
print(paises.pivot_table(index="contiene", columns="nombre", values="poblacion", aggfunc="sum"))