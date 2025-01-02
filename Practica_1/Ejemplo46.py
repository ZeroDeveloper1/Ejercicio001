import matplotlib as plt
fig, axs = plt.subplots(2,2) # se crea una figura y cuaro ejes
# se puede acceder a cada eje usndo el arreglo asx, por ejemplo
#para dibujar un grafico de linea en el primer eje se puede hacer:
asx[0, 0].plot([1, 2, 3, 4],[1,4,9,16])
plt.show()
