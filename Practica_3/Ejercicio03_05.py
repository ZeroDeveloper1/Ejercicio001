import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alumnos.csv')

plt.figure()
plt.scatter(df['Nota_Lengua'], df['Nota_Ingles'])
plt.title('Relación entre Nota de Lengua y Nota de Inglés')
plt.xlabel('Nota de Lengua')
plt.ylabel('Nota de Inglés')
plt.grid(True)
plt.show()
