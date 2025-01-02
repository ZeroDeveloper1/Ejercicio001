import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("alumnos.csv")

# Calcular la nota media
df['Nota_Media'] = (df['Nota_de_Matematicas'] + df['Nota_Lengua'] + df['Nota_Ingles']) / 3

# Calcular la media por género
media_por_genero = df.groupby('Genero')['Nota_Media'].mean()

# Crear la gráfica
plt.figure(figsize=(10, 6))
media_por_genero.plot(kind='bar')
plt.title('Nota Media por Género')
plt.ylabel('Nota Media')
plt.xlabel('Género')
plt.grid(True, axis='y')
plt.xticks(rotation=0)

# Añadir etiquetas de valor sobre cada barra
for i, v in enumerate(media_por_genero):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
