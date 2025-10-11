# Genera los primeros n números de la secuencia Fibonacci.

n = int(input("¿Cuántos números de Fibonacci?: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
