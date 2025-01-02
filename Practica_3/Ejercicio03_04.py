import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alumnos.csv')
notas_matematicas = df['Nota_Matematicas'].value_counts()

plt.figure()
notas_matematicas.plot(kind='pie', autopct='%1.1f%%')
plt.title('Proporción de Alumnos por Nota de Matemáticas')
plt.ylabel('')
plt.show()
