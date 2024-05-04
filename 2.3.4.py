puntaje = 0

# Pregunta 1
respuesta = input("¿Cuál es la sintaxis correcta para definir una función en Python?\na) def nombre_funcion():\nb) function nombre_funcion():\nc) create function nombre_funcion():\nd) define nombre_funcion():\n")
if respuesta.lower() == "a":
    puntaje += 1

# Pregunta 2
respuesta = input("¿Cuál es el operador utilizado para la concatenación de cadenas en Python?\na) +\nb) &\nc) |\nd) ^\n")
if respuesta.lower() == "a":
    puntaje += 1

# Pregunta 3
respuesta = input("¿Cuál es la estructura de control utilizada para iterar sobre una secuencia en Python?\na) for\nb) while\nc) if\nd) switch\n")
if respuesta.lower() == "a":
    puntaje += 1

print(f"Puntaje obtenido: {puntaje}")

if puntaje == 3:
    nota = "Excelente"
elif puntaje == 2:
    nota = "Bien"
elif puntaje == 1:
    nota = "Regular"
else:
    nota = "Deficiente"

print(f"Nota: {nota}")