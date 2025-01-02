import numpy as np
# se importa la funcion norm desde el modulo numpy. linalg
from numpy.linalg import inv
#se crea una matriz de 2 x 2 elemetos
A = np.array([[1, 2], [3, 4]])
F = inv(A)
print(F)
