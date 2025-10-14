# 1. Suma de dos números
import threading
import json
from functools import reduce
import time
from statistics import mean, median, mode
a = int(input("Número 1: "))
b = int(input("Número 2: "))
print("Suma:", a + b)
# 2. Número par o impar
n = int(input("Número: "))
print("Par" if n % 2 == 0 else "Impar")
# 3. Mayor de tres números
a, b, c = 10, 25, 15
print("Mayor:", max(a, b, c))
# 4. Contar vocales en una palabra
palabra = "programacion"
vocales = "aeiou"
contador = sum(1 for letra in palabra if letra in vocales)
print("Vocales:", contador)
# 5. Invertir una cadena
texto = "python"
print(texto[::-1])
# 6. Factorial de un número
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial de {n} es {fact}")
# 7. Tabla de multiplicar
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
# 8. Sumar los dígitos de un número
n = 1234
suma = sum(int(d) for d in str(n))
print("Suma de dígitos:", suma)
# 9. Comprobar si es palíndromo
texto = "radar"
print("Palíndromo" if texto == texto[::-1] else "No lo es")
# 10. Promedio de una lista
numeros = [4, 8, 15, 16, 23, 42]
promedio = sum(numeros) / len(numeros)
print("Promedio:", promedio)
# 11. Números primos hasta n
n = 20
for i in range(2, n+1):
    if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
        print(i, end=" ")
# 12. Contar palabras en un texto
texto = "hola mundo hola python"
palabras = texto.split()
conteo = {p: palabras.count(p) for p in set(palabras)}
print(conteo)
# 13. Fibonacci con función


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci(10)
# 14. Eliminar duplicados de una lista
lista = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(lista))
print(sin_duplicados)
# 15. Ordenar diccionario por valor
notas = {"Ana": 8, "Luis": 5, "Juan": 9}
ordenado = dict(sorted(notas.items(), key=lambda x: x[1], reverse=True))
print(ordenado)
# 16. Suma de matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
resultado = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print(resultado)
# 17. Diccionario de cuadrados
n = 5
cuadrados = {i: i**2 for i in range(1, n+1)}
print(cuadrados)
# 18. Comprobar anagrama
a, b = "amor", "roma"
print(sorted(a) == sorted(b))
# 19. Calcular media, mediana y moda
nums = [1, 2, 2, 3, 4]
print("Media:", mean(nums))
print("Mediana:", median(nums))
print("Moda:", mode(nums))
# 20. Contador de caracteres
texto = "banana"
frecuencia = {}
for c in texto:
    frecuencia[c] = frecuencia.get(c, 0) + 1
print(frecuencia)
# Clase Persona con métodos


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


p = Persona("Brisa", 25)
p.saludar()
# 22. Decorador para medir tiempo


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        print("Tiempo:", round(time.time() - inicio, 4), "s")
        return resultado
    return wrapper


@medir_tiempo
def tarea():
    sum([i**2 for i in range(10_000)])


tarea()
# 23. Generador de números pares


def pares(n):
    for i in range(0, n+1, 2):
        yield i


for p in pares(10):
    print(p)
# 24. Leer archivo y contar líneas
with open("archivo.txt", "r") as f:
    lineas = f.readlines()
    print("Líneas:", len(lineas))
# 25. Clase Banco con saldo


class Banco:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")


b = Banco("Brisa", 1000)
b.retirar(200)
print(b.saldo)
# 26. Manejador de excepciones
try:
    n = int(input("Número: "))
    print(10 / n)
except ValueError:
    print("Debe ser un número.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
# 27. Buscar el número mayor en una lista anidada
lista = [[3, 8, 2], [10, 5], [7, 12, 1]]
mayor = max(max(sub) for sub in lista)
print("Mayor:", mayor)
# 28. Uso de map, filter y reduce

nums = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x*2, nums))
pares = list(filter(lambda x: x % 2 == 0, dobles))
suma = reduce(lambda a, b: a + b, pares)
print(dobles, pares, suma)
# 29. Leer JSON

data = '{"nombre": "Brisa", "edad": 25}'
obj = json.loads(data)
print(obj["nombre"])
# 30. Hilos con threading


def tarea(nombre):
    for i in range(3):
        print(f"{nombre} ejecutando {i}")
        time.sleep(1)


t1 = threading.Thread(target=tarea, args=("Hilo 1",))
t2 = threading.Thread(target=tarea, args=("Hilo 2",))
t1.start()
t2.start()
t1.join()
t2.join()
print("Tareas completadas")
