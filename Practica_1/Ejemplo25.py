import pandas as pd
paises = pd.DataFrame(
    {
    "nombre": ["Venezuela", "Colombia", "Peru", "Ecuador", "Chile"],
    "Poblacion":[28.52, 50.34, 32.51, 17.64, 19.12],
    "area": [916.445, 1141.748, 1285.216, 283.561, 756.096],

    }
)
paises.style.applymap(
    lambda x: "Color: red" if x > 30 else "color: black", subset = ["Poblacion", "Area"]
)

print(paises)