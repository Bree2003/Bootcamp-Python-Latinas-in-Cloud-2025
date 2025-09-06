# Pide dos números al usuario e imprime su suma,
# resta, multiplicación y división

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir entre 0")
