import pandas as pd
paises = pd.DataFrame(
   {
       "Nombre": ["Venezuela","Colombia","Peru","Ecuador","Chile"],
        "poblacion": [28.52, 50.34, 32.51,17.64,19.12],       
    }
   
)
print(paises)

#agregar una nueva fila con los datos de Bolivia
paises = paises.append({"Nombre:": "Bolivia", "poblacion":11.51}, ignore_index= True)
print(paises)

