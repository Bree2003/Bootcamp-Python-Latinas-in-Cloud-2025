# Ordena una lista de números sin usar .sort().

numeros = [5, 2, 8, 1, 3]

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada:", numeros)
