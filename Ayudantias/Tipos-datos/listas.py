# Coleccion ordenada, mutable, permite duplicados
# Se define con corchetes []
# Puede contener cualquier tipo de dato

numeros = [1, 2, 3, 4]
frutas = ["manzana", "banana", "pera"]
mixta = [1, "hola", 3.14, True]

#  Operaciones y metodos comunes
# -----------------------------
len(numeros)  # Longitud de la lista, cantidad de elementos
numeros.append(5)  # Agrega un elemento al final
numeros.insert(0, 0)  # Inserta un elemento en la posicion dada
numeros.remove(3)  # Elimina la primera ocurrencia del valor
numeros.pop()  # Elimina y retorna el ultimo elemento
numeros.pop(0)  # Elimina y retorna el elemento en la posicion dada
numeros.index(2)  # Retorna el indice de la primera ocurrencia del valor
2 in numeros  # True verifica si el valor esta en la lista
3 not in numeros  # True verifica si el valor no esta en la lista
numeros.sort()  # Ordena la lista en orden ascendente
numeros.reverse()  # Invierte el orden de la lista

# Adcceso a elementos
numeros[0]  # Primer elemento
numeros[-1]  # Ultimo elemento
numeros[1:3]  # Sublista desde indice 1 hasta 2
numeros[::2]  # Sublista con paso 2, cada dos elementos
numeros[:]  # Copia de la lista completa
numeros[1] = 10  # Modifica el elemento en la posicion dada
numeros.clear()  # Elimina todos los elementos de la lista
numeros.extend([6, 7, 8])  # Agrega multiples elementos al final
