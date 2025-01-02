import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alumnos.csv')

plt.figure()
df.boxplot(column='Nota_Ingles', by='Genero')
plt.title('Distribución de la Nota de Inglés por Género')
plt.suptitle('')
plt.xlabel('Género')
plt.ylabel('Nota de Inglés')
plt.grid(True)
plt.show()
