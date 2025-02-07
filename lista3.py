#escribe un programa que cree un alista de 5 elementos solicitados al usuario
el programa debe mostrar la lista, luego solictar al usuario el indice de un elemento y mostar el valor del elemento en ese indice.

elements=[]

#solictamos al usuario 5 elementos
for _ in range (5):
    element=input("Ingrese 5 elementos: ")
    elements.append(element)

#mostrar la lista obtenida
print("lista de elementos: ". elements)

#solicitamos al usuario el indice de un elemento
index = int(input("Introduce el indice del elemento: "))
#mostrar el valor del elemento en el indice especifico
print("Valor del elemento en el indice", index, ":", elements(index))
