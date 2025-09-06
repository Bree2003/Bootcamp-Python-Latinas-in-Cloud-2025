# Cuenta cuántas veces aparece cada palabra en una frase.

frase = input("Frase: ").lower().split()
frecuencia = {}

for palabra in frase:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)
