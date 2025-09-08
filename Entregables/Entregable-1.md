Parte 1: 20 Ejercicios Intermedios de Python
Estos ejercicios están diseñados para practicar lógica de programación, manipulación de estructuras de datos y funciones. El ejemplo de la "caja de ventas" es una excelente base para varios de ellos.
Conceptos a evaluar: Listas, diccionarios, bucles, condicionales, funciones, manejo de entradas del usuario.
Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)
Calculadora de Factorial: Crea una función que calcule el factorial de un número ingresado por el usuario.
Verificador de Números Primos: Escribe un programa que determine si un número ingresado es primo o no.
Secuencia de Fibonacci: Genera los primeros N números de la secuencia de Fibonacci, donde N es un número proporcionado por el usuario.
Adivina el Número: El programa genera un número aleatorio y el usuario debe adivinarlo. El programa debe dar pistas de "más alto" o "más bajo".
Conversor de Temperatura: Crea funciones para convertir de Celsius a Fahrenheit y viceversa.
Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)
Contador de Vocales y Consonantes: Pide al usuario una frase y cuenta cuántas vocales y consonantes contiene.
Palíndromo: Verifica si una palabra o frase ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha y viceversa).
Eliminar Duplicados de una Lista: Dada una lista, crea una nueva lista que contenga solo los elementos únicos de la original.
Buscador de Elemento Común: Escribe una función que reciba dos listas y devuelva una lista con los elementos que tienen en común.
Ordenamiento de Lista: Implementa el algoritmo de ordenamiento de burbuja para ordenar una lista de números de menor a mayor.
Grupo 3: Diccionarios y Estructuras de Datos Complejas (Ejercicios 11-15)
Contador de Frecuencia de Palabras: Dado un texto, cuenta la frecuencia de cada palabra y almacénala en un diccionario.
Agenda de Contactos: Crea un programa que permita al usuario añadir, buscar y eliminar contactos. Cada contacto debe ser un diccionario con nombre, teléfono y email.
Gestor de Calificaciones: Permite al usuario ingresar nombres de estudiantes y sus calificaciones. Almacénalos en un diccionario y luego calcula el promedio de la clase.
Traductor Simple: Crea un pequeño diccionario que funcione como traductor de español a inglés para unas 10 palabras.
Inventario de Tienda: Define un diccionario para un inventario de productos donde la clave es el nombre del producto y el valor es otro diccionario con "precio" y "stock".
Grupo 4: Proyecto "Caja de Ventas" (Ejercicios 16-20)[1][2][3]
Estos ejercicios construyen progresivamente un sistema de caja registradora.[2]
Definir Productos: Crea un diccionario de productos con su respectivo precio.[2]
Mostrar Menú y Agregar al Carrito: Muestra los productos al usuario y permite que seleccione productos y cantidades para agregarlos a una lista que funcionará como carrito de compras.[2]
Calcular Subtotal: Crea una función que calcule el total de la compra en base a los productos en el carrito.[2]
Aplicar Descuentos: Modifica el programa para que aplique un descuento (por ejemplo, 10%) si el total de la compra supera un cierto monto.[2]
Finalizar Compra y Mostrar Ticket: Muestra un resumen de la compra con el subtotal, el descuento aplicado (si corresponde) y el total a pagar.
Parte 2: Aplicación Básica con Flask y Jinja
Este proyecto introduce a los estudiantes al desarrollo web con Python, enfocándose en el manejo de rutas y la renderización de plantillas dinámicas.
Objetivo: Crear una aplicación de lista de tareas (To-Do List) donde las tareas se guardan en una lista en memoria mientras el servidor está en ejecución.
Estructura del Proyecto:
code
Code
/todo_app
├── app.py
└── /templates
    ├── index.html
    └── agregar.html
app.py
code
Python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las tareas en memoria
tareas = ["Aprender Python", "Crear un entregable", "Practicar Flask"]

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nueva_tarea = request.form['tarea']
        tareas.append(nueva_tarea)
        return redirect(url_for('index'))
    return render_template('agregar.html')

@app.route('/eliminar/<int:tarea_id>')
def eliminar(tarea_id):
    if 0 <= tarea_id < len(tareas):
        tareas.pop(tarea_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
templates/index.html
code
Html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Tareas</title>
</head>
<body>
    <h1>Mis Tareas</h1>
    <ul>
        {% for i in range(tareas|length) %}
            <li>{{ tareas[i] }} <a href="{{ url_for('eliminar', tarea_id=i) }}">Eliminar</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('agregar') }}">Agregar Tarea</a>
</body>
</html>
templates/agregar.html
code
Html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar Tarea</title>
</head>
<body>
    <h1>Agregar Nueva Tarea</h1>
    <form method="post">
        <label for="tarea">Tarea:</label>
        <input type="text" id="tarea" name="tarea" required>
        <button type="submit">Agregar</button>
    </form>
    <br>
    <a href="{{ url_for('index') }}">Volver a la lista</a>
</body>
</html>
Parte 3: 10 Ejercicios de Ciencia de Datos con Google Colab
El objetivo de esta sección es que los estudiantes se familiaricen con el entorno de Google Colab y las librerías fundamentales de ciencia de datos en Python.[4][5][6]
Librerías principales: NumPy, Pandas, Matplotlib.[7][8]
Introducción a Colab:
Ejercicio: Crear un nuevo notebook en Google Colab, añadir una celda de texto con un título y una celda de código que imprima "Hola, Ciencia de Datos".[5]
Fundamentos de NumPy:
Ejercicio: Crear un array de NumPy con 10 números aleatorios. Calcular la media, la mediana y la desviación estándar de ese array.[9]
Manipulación de Arrays con NumPy:
Ejercicio: Crear una matriz de 3x3 con números del 1 al 9. Luego, seleccionar y mostrar solo la segunda fila de la matriz.
Introducción a Pandas - Series:
Ejercicio: Crear una Serie de Pandas a partir de una lista de 5 países y otra con sus respectivas capitales.
Introducción a Pandas - DataFrames:
Ejercicio: Crear un DataFrame de Pandas a partir de un diccionario que contenga nombres, edades y ciudades de 4 personas.[10]
Carga de Datos desde un CSV:
Ejercicio: Encontrar un archivo CSV sencillo en internet (ej. datos de un censo simple, resultados deportivos). Subirlo a Google Colab y cargarlo en un DataFrame de Pandas.[11]
Exploración Básica de un DataFrame:
Ejercicio: Usando el DataFrame del ejercicio anterior, mostrar las primeras 5 filas (.head()), las últimas 5 (.tail()) y obtener un resumen estadístico básico (.describe()).[11]
Selección y Filtrado de Datos:
Ejercicio: Del DataFrame cargado, seleccionar una columna específica. Luego, filtrar las filas que cumplan una condición (ej. edad > 30).
Visualización Básica con Matplotlib:
Ejercicio: Crear un gráfico de barras simple usando Matplotlib que muestre la población de 5 ciudades diferentes.
Análisis y Visualización Integrada:
Ejercicio: A partir del DataFrame del ejercicio 6, elegir una columna numérica y crear un histograma para visualizar su distribución. Luego, elegir dos columnas y crear un gráfico de dispersión para ver si hay alguna relación entre ellas