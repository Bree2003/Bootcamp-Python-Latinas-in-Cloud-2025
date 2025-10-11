# Escribe un programa que determine si un número dado es primo.

n = int(input("Número: "))
es_primo = True

if n < 2:
    es_primo = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

print("Es primo" if es_primo else "No es primo")
