#escribe un programa que cree una lista de elementos aleatorios, muestre la longuitud de la lista y luego el primer y el ultimo elemento de la lista
import random

random_list=[random.randit(0,100)for _ in range(random.randint(5,15))]

#mostramos la longuitud de la lista
print("Longuitud de la lista:", len(random_list))

#mostramos el primer elemento de la lista
print("Primer elemento de la lista: ", random_list[0])

#mostramos el ultimo elemento de la lista
print("Ultimo elemento de la lista", random_list[-1])

