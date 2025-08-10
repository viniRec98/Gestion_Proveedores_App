# routes/provider_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required
from models import db, Provider

# url_prefix organiza las rutas bajo /providers
provider_bp = Blueprint("provider", __name__, url_prefix="/providers")

# Listar + Buscar + Crear 
@provider_bp.route("/", methods=["GET", "POST"])
@jwt_required()
def list_providers():
    # Crear proveedor 
    if request.method == "POST":
        p = Provider(
            company_name=request.form.get("company_name", "").strip(),
            contact_person=request.form.get("contact_person", "").strip(),
            email=request.form.get("email", "").strip(),
            type=request.form.get("type", "").strip(),
            nit=request.form.get("nit", "").strip(),
            phone=request.form.get("phone", "").strip(),
            city=request.form.get("city", "").strip(),
        )
        db.session.add(p)
        db.session.commit()
        flash("Proveedor creado exitosamente.", "success")
        return redirect(url_for("provider.list_providers"))

    # Búsqueda por nombre y tipo (GET)
    qname = request.args.get("name", "").strip()
    qtype = request.args.get("type", "").strip()

    query = Provider.query
    if qname:
        query = query.filter(Provider.company_name.ilike(f"%{qname}%"))
    if qtype:
        query = query.filter(Provider.type == qtype)

    providers = query.order_by(Provider.created_at.desc()).all()
    return render_template("providers.html", providers=providers, qname=qname, qtype=qtype)

# Editar proveedor
@provider_bp.route("/edit/<int:pid>", methods=["GET", "POST"])
@jwt_required()
def edit_provider(pid):
    p = Provider.query.get_or_404(pid)
    if request.method == "POST":
        p.company_name   = request.form.get("company_name", "").strip()
        p.contact_person = request.form.get("contact_person", "").strip()
        p.email          = request.form.get("email", "").strip()
        p.type           = request.form.get("type", "").strip()
        p.nit            = request.form.get("nit", "").strip()
        p.phone          = request.form.get("phone", "").strip()
        p.city           = request.form.get("city", "").strip()
        db.session.commit()
        flash("Proveedor actualizado", "success")
        return redirect(url_for("provider.list_providers"))
    return render_template("edit_provider.html", provider=p)

# Eliminar proveedor
@provider_bp.route("/delete/<int:pid>", methods=["POST"])
@jwt_required()
def delete_provider(pid):
    p = Provider.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash("Proveedor eliminado", "success")
    return redirect(url_for("provider.list_providers"))
