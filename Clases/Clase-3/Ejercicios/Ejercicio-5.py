# Pide un número y muestra su tabla de multiplicar del 1 al 10.

n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
