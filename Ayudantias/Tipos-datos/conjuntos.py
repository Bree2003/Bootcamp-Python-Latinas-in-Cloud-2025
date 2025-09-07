# Coleccion desordenada, mutable, no permite duplicados
# Se define con llaves {}
# Puede contener cualquier tipo de dato
numeros = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Operaciones y metodos comunes
# -----------------------------
len(numeros)  # Longitud del conjunto, cantidad de elementos
numeros.add(5)  # Agrega un elemento al conjunto
numeros.remove(3)  # Elimina el elemento, error si no existe
numeros.discard(10)  # Elimina el elemento, no da error si no existe
numeros.pop()  # Elimina y retorna un elemento arbitrario
numeros.clear()  # Elimina todos los elementos del conjunto

a = {1, 2, 3}
b = {3, 4, 5}
a.union(b)  # {1, 2, 3, 4, 5} union de conjuntos
a.intersection(b)  # {3} interseccion de conjuntos
# {1, 2} diferencia de conjuntos, devuelve los elementos que
# estan en a pero NO en b
a.difference(b)
# {1, 2, 4, 5} diferencia simetrica, elementos que
# estan en a o b, pero NO en ambos
a.symmetric_difference(b)
