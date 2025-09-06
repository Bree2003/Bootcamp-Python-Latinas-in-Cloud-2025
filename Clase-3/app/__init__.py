from flask import Flask

# Versión simple
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hola, Flask! Esta es la versión simple"

# Renderizar HTMLS
def create_app():
    app = Flask(__name__)

    # Importar rutas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
