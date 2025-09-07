# Coleccion ordenada, inmutable, permite duplicados
# Se define con parentesis ()
# Puede contener cualquier tipo de dato
coordenadas = (10, 20)

#  Operaciones y metodos comunes
# -----------------------------
len(coordenadas)  # Longitud de la tupla, cantidad de elementos
coordenadas.count(10)  # Cuenta cuantas veces aparece el valor
coordenadas.index(20)  # Retorna el indice de la primera ocurrencia del valor
10 in coordenadas  # True verifica si el valor esta en la tupla
20 not in coordenadas  # True verifica si el valor no esta en la tupla
