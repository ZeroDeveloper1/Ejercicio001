import numpy as np
a = np.array([1, 2, 3, 4, 5])# se crea el arreglo con el rango
# se crea 5 elementos
b = np.array([True, False, True, False, True]) 
e = a > 3 # se compara los elementos con el valor de 3
f = np.logical_and(e,b)# se aplica la funcion logica and
print(e) # se imprime el nuevo arreglo
print(f) # se imprime el nuevo arreglo
