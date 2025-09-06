# Renderizar htmls
from app import create_app

app = create_app()

# Versión simple
# from app import app

if __name__ == '__main__':
    app.run(debug=True)
