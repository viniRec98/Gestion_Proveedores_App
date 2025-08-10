from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Crear objeto de tipo SQLALchemy
db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    country = db.Column(db.String(100),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Admin {self.email}>"

class Provider(db.Model):
    __tablename__ = "providers"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    contact_person = db.Column(db.String(200))
    email = db.Column(db.String(120))
    type = db.Column(db.String(50))
    nit = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    city = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Provider {self.company_name}>"
