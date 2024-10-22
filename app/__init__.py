from flask import Flask
from flask_cors import CORS
from .models import db  # Asegúrate de importar db
from .routes import main as main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config.Config')  # Asegúrate de que esta ruta sea correcta
    CORS(app)  # Habilitar CORS para todas las rutas

    db.init_app(app)  # Inicializa db con la app

    app.register_blueprint(main_routes)

    return app
