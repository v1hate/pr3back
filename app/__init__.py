from flask import Flask
from flask_cors import CORS
from .routes import main as main_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(main_routes)

    return app