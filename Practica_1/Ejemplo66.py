import numpy as np
a = np.array([1, 2, 3, 4, 5])# se crea el arreglo con el rango
mascara = a > 3
print(mascara)
print(a[mascara])
