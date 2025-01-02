import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alumnos.csv')
conteo_por_edad = df['Edad'].value_counts()

plt.figure()
conteo_por_edad.sort_index().plot(kind='bar')
plt.title('Número de Alumnos por Edad')
plt.ylabel('Número de Alumnos')
plt.xlabel('Edad')
plt.grid(axis='y')
plt.show()
