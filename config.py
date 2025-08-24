import os
from dotenv import load_dotenv


#Cargar variables de entorno desde el archivo .env
load_dotenv()


class Config:
    """
    #Connection String a la base de datos de PostgreSQL en SUPABASE
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


    #Evitar advertencias innecesarias de SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #Clave secreta para firmar cookies y proteger sesiones
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-dev")


    #Configuracion de JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secreta-dev") #Clave secreta para firmar y validar tokens JWT
    JWT_TOKEN_LOCATION = ["cookies"]   # Guardar el token en cookies
    JWT_COOKIE_SECURE = False          # True en producción con HTTPS
    JWT_COOKIE_CSRF_PROTECT = False    # Para simplificar pruebas
    """

    # Connection String a la base de datos de PostgreSQL en SUPABASE
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "sslmode": "require"
        }
    }

    
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-dev")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secreta-dev")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = False

