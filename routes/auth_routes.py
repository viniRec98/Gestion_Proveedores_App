from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from models import db, Admin

auth_bp = Blueprint("auth", __name__)

# Ruta de login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        
        admin = Admin.query.filter_by(email=email).first()
        
        if admin and check_password_hash(admin.password_hash, password):
            # Generar token JWT válido por 1 hora y lo guarda como cookie
            token = create_access_token(identity=admin.email, expires_delta=timedelta(hours=1))
            
            resp = redirect(url_for("provider.list_providers"))
            set_access_cookies(resp, token)
            flash("Inicio de sesión exitoso", "success")
            return resp
        else:
            flash("Credenciales inválidas", "danger")
    
    return render_template("login.html")

# Ruta de logout
@auth_bp.route("/logout")
def logout():
    resp = redirect(url_for("auth.login"))
    unset_jwt_cookies(resp) #elimina la cookie del JWT
    flash("Sesión cerrada", "success")
    return resp

# Crear admin inicial (solo desarrollo)
@auth_bp.route("/create_admin", methods=["GET", "POST"])
def create_admin():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        country = request.form.get("country", "").strip()
        gender = request.form.get("gender", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        
        if Admin.query.filter_by(email=email).first():
            flash("Ya existe un admin con ese email", "warning")
        else:
            hashed_pw = generate_password_hash(password)
            admin = Admin(
                name=name,
                country=country,
                gender=gender,
                email=email,
                password_hash=hashed_pw
            )
            db.session.add(admin)
            db.session.commit()
            flash("Administrador creado exitosamente", "success")
            return redirect(url_for("auth.login"))
    
    return render_template("create_admin.html")
