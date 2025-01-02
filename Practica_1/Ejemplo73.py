import numpy as np
a = np.array([1, 2, 3]) # se crea un vector de 3 elemntos
b = np.array ([4,5,6]) # se crea otro vector de 3 elemntos
A = np.array([[1,2],[3,4]]) # se crea otra matriz de 2x 2 elemntos
B = np.array([[5,7],[7,8]]) # Se crea otra matriz de 2x 2
d = np.cross(a,b)#se calcula el producto vectorial de los vectores
D = np.cross(A,B) # se calcula el producto de harald de las matrices 
print(d) # se imprime el resultado
print(D) # se imprime el resultado