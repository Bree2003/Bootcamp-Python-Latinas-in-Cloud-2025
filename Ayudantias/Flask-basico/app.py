# Importamos las funciones necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for
# Flask -> clase principal del framework, con ella creas la aplicación web
# render_template -> función para renderizar plantillas HTML
# que tienes en la carpeta 'templates'
# request -> objeto que contiene datos de la solicitud HTTP
# redirect -> función para redirigir a otra ruta
# url_for -> función para construir URLs para funciones de vista

# Creamos la aplicación Flask, "__name__" le dice a Flask
# que este archibo es el punto de entrada
app = Flask(__name__)

# Lista en memoria para guardar tareas (simula una base de datos por ahora)
tareas = []

# Definimos una ruta para la página principal
# Solo acepta el método GET (por defecto)


@app.route('/')
def index():

    print(tareas)
    # Renderizamos la plantilla 'index.html' y le
    # pasamos la lista de tareas como variable
    return render_template('index.html', tareas=tareas)

# Definimos una ruta para agregar nuevas tareas
# Acepta solo el método POST (cuando se envía el formulario)


@app.route('/agregar', methods=['GET'])
def agregar():
    # Obtenemos los datos que vienen del formulario
    titulo = request.form.get("titulo")
    descripcion = request.form.get("descripcion")

    # Validamos que al menos tenga un título antes de guardar
    if titulo:
        # Agregamos un diccionario con los datos a la lista "tareas"
        tareas.append({
            "titulo": titulo,
            "descripcion": descripcion
        })

    # Redirigimos al usuario de vuelta a la página principal
    # return redirect(url_for("index"))
    return render_template('index.html', tareas=tareas)


# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecutamos la aplicación en modo debug
    # (recarga automática y mensajes de error detallados)
    app.run(debug=True)
