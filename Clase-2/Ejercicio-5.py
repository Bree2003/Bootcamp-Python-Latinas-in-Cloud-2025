# Guarda un texto en un archivo saludo.txt con el mensaje "Hola desde Python"
# Y luego ábrelo para leerlo e imprimir su contenido.

# Escribir en el archivo
with open("Clase-2/saludo.txt", "w") as archivo:
    archivo.write("Hola desde Python")

# Leer del archivo
with open("Clase-2/saludo.txt", "r") as arc:
    contenido = arc.read()
    print("Contenido del archivo: ", contenido)
