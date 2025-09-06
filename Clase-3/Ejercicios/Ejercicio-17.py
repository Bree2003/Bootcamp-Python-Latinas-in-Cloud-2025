# Crea un diccionario con nombres y teléfonos,
# y permite agregar/buscar contactos.

agenda = {}

while True:
    opcion = input(
        "\n1. Agregar contacto\n2. Buscar contacto\n3. Salir\nOpción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        print("Teléfono:", agenda.get(nombre, "No encontrado"))
    elif opcion == "3":
        break
    else:
        print("Opción inválida")
