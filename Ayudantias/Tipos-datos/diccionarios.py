# Coleccion clave-valor, mutable, no permite claves duplicadas
# Se define con llaves {} y dos puntos :
persona = {"nombre": "Brisa", "edad": 23}

# Acceso y operaciones comunes
persona["nombre"]  # Acceso al valor por clave, "Brisa"
persona.get("edad")  # Acceso seguro al valor por clave, 22
persona["edad"] = 23  # Modifica el valor de una clave existente
persona["ciudad"] = "Santiago"  # Agrega una nueva clave-valor
del persona["edad"]  # Elimina una clave-valor
len(persona)  # Longitud del diccionario, cantidad de pares clave-valor
"nombre" in persona  # True verifica si la clave existe

# Metodos comunes
persona.keys()  # Retorna una vista de las claves
persona.values()  # Retorna una vista de los valores
persona.items()  # Retorna una vista de pares (clave, valor)
persona.clear()  # Elimina todos los pares clave-valor
persona.update({"edad": 24, "pais": "Chile"})  # Actualiza con otro diccionario
persona.pop("ciudad")  # Elimina y retorna el valor de la clave
