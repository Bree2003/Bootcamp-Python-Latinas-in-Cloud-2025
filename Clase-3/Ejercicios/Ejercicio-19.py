# Crea una clase Persona con atributos como
# nombre y edad, y un método que muestre un saludo.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")


p1 = Persona("Brisa", 25)
p1.saludar()
