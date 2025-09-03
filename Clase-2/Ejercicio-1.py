# Pide un número al usuario y determina si es par o impar.

numero = int(input("Ingresa un número: "))
# input, permite leer entradas del usuario
# int convierte la entrada en un número entero

if numero % 2 == 0:
    print("El número es par ", numero)  # concatenación de cadenas
else:
    print(f"El número {numero} es impar")  # interpolación de cadenas
