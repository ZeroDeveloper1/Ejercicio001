result = []
while True:
    element = input("Introduce un elemento(o "stop" para temrinar la entrada): ")
    if element.lower() == ´stop´:
        break
    result.append(element)
    print("Lista Final: ", result)
    