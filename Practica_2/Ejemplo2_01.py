import pandas as pd
datos = {"nombres": ["Juan", "Pedro", "Margarita"], 
        "edad":[22,34,42],
        "curso": ["PNL","DISEÑO WEB", "PYTHON"],
        "email":["juan@gmail.com","pedro@gmail.com","margarita@gmail.com"] }
df = pd.DataFrame(datos)
print(df)
