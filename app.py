from flask import Flask, redirect  # <-- add redirect
from flask_jwt_extended import JWTManager
from config import Config
from models import db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos y JWT
    db.init_app(app)
    JWTManager(app)

    # Registrar rutas
    from routes.auth_routes import auth_bp
    from routes.provider_routes import provider_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(provider_bp)

    # Redirect root to /create_admin
    @app.route("/")
    def root():
        return redirect("/create_admin")

    return app

# Punto de entrada
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Crea las tablas si no han sido creado previamente
        if os.getenv("FLASK_INIT_DB", "True") == "True":
            db.create_all()
            print("Tablas creadas en la base de datos.")
    app.run(host="0.0.0.0", port=5000, debug=True)