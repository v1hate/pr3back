from flask import Flask
from flask_cors import CORS
from .models import db  # Importa db aquí
from .routes import main as main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config.Config')  # Asegúrate de que la configuración sea correcta
    CORS(app)  # Habilitar CORS

    db.init_app(app)  # Inicializa SQLAlchemy con la app

    app.register_blueprint(main_routes)  # Registra las rutas

    return app
