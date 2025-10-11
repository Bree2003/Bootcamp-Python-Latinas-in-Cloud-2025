# El programa genera un número aleatorio y el usuario debe adivinarlo.

import random

numero = random.randint(1, 100)
intento = None

while intento != numero:
    intento = int(input("Adivina el número (1-100): "))
    if intento < numero:
        print("Más alto")
    elif intento > numero:
        print("Más bajo")

print("¡Correcto! El número era", numero)
