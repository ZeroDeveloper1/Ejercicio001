import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alumnos.csv')
df['Nota_Media'] = (df['Nota_Matematicas'] + df['Nota_Lengua'] + df['Nota_Ingles']) / 3

plt.figure()
plt.hist(df['Nota_Media'], bins=10)
plt.title('Distribución de Frecuencias de la Nota Media')
plt.xlabel('Nota Media')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()
