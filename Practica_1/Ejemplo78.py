import numpy as np
from numpy.linalg import solve

# Se crea la matriz de coeficientes con corrección
A = np.array([[2, 1], [3, -1]])

# Se crea el vector de términos independientes
b = np.array([4, 2])

# Se resuelve el sistema de ecuaciones
x = solve(A, b)

# Se imprime el resultado
print(x)