# Calcula el factorial de un número usando un bucle.

n = int(input("Número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)
