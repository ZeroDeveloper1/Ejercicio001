import json

# Crear un diccionario en Python
persona = {
    "nombre": "Jersson",
    "edad": 25,
    "ciudad": "Lima"
}

# Convertir el diccionario a JSON
persona_json = json.dumps(persona, indent=4)

print("Diccionario convertido a JSON:")
print(persona_json)
