# Convierte una cantidad de dólares a pesos (o viceversa) usando una tasa fija.

tasa = 900  # Ejemplo: 1 dólar = 900 pesos
opcion = input("¿Convertir a (P)esos o (D)ólares?: ").lower()
cantidad = float(input("Cantidad: "))

if opcion == "p":
    print("Resultado:", cantidad * tasa, "pesos")
elif opcion == "d":
    print("Resultado:", cantidad / tasa, "dólares")
