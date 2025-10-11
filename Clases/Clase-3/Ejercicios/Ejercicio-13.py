# Verifica si una palabra o frase es palíndroma.

texto = input("Texto: ").replace(" ", "").lower()
if texto == texto[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")
