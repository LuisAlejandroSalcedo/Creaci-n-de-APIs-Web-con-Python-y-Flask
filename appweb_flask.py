# Importamos Flask
from flask import Flask

# Instanciamos Flask
app = Flask(__name__)


@app.route('/')
def index():
    # Cuerpo de la pagina. Un simple "Hola Mundo"
    return "Hola Mundo"

if __name__ == '__main__':
    # Corremos la aplicación en modo "debug"
    app.run(debug=True)
