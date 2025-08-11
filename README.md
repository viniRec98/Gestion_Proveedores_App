# Gestión de Proveedores App

Aplicación web en Flask para gestionar proveedores y administradores, con autenticación JWT y base de datos PostgreSQL.

## Requisitos

- Python 3.12+
- PostgreSQL

## Instalación

1. **Clona el repositorio:**
   ```sh
   git clone <URL_DEL_REPO>
   cd Gestion_Proveedores_App
   ```

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   - Crea el archivo `.env`
   - Usa Supabase para crear y gestionar tu base de datos PostgreSQL. Copia la URL de conexión y asígnala a `DATABASE_URL`.
   - Genera las claves secretas ejecutando:
     ```sh
     python3 -c "import secrets; print(secrets.token_hex(32))"
     ```
     Asigna el resultado a `SECRET_KEY` y `JWT_SECRET_KEY` en tu `.env`


   - Deja que Flask cree las tablas automáticamente al iniciar si `FLASK_INIT_DB=True` en `.env`.

## Ejecución

```sh
python app.py
```

La app estará disponible en [http://localhost:5000](http://localhost:5000).

## Estructura

- `app.py` — Punto de entrada Flask
- `config.py` — Configuración de entorno y JWT
- `models.py` — Modelos SQLAlchemy
- `routes/` — Rutas de autenticación y proveedores
- `templates/` — HTML con Bootstrap
- `requirements.txt` — Dependencias Python
- `script.sql` — Esquema inicial de la base de datos

## Acceso a rutas principales

- `/login` — Iniciar sesión como administrador.
- `/logout` — Cerrar sesión.
- `/providers` — Listar, buscar y registrar proveedores.
- `/providers/edit/<id>` — Editar proveedor.
- `/providers/delete/<id>` — Eliminar proveedor.
- `/create_admin` — Crear un nuevo usuario administrador (solo accesible si no hay)

## Autenticación

- Acceso solo para administradores registrados.
- JWT almacenado
