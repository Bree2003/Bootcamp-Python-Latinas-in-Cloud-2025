# Pide una frase e imprime cuántas vocales contiene.

frase = input("Frase: ").lower()
vocales = "aeiou"
contador = sum(1 for letra in frase if letra in vocales)
print("Cantidad de vocales:", contador)
