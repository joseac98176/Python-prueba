from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importar y registrar controladores (Blueprints)
    from app.controllers.acceso_controller import acceso_bp
    app.register_blueprint(acceso_bp)

    return app