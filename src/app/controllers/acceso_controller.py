from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.acceso_service import crear_usuario

acceso_bp = Blueprint("acceso", __name__)


@acceso_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@acceso_bp.route("/registro", methods=["GET"])
def vista_registro():
    return render_template("registro.html")

@acceso_bp.route("/registro", methods=["POST"])
def procesar_registro():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    clave = request.form.get("clave", "").strip()
    rol = request.form.get("rol", "empleado").strip()

    exito, mensaje = crear_usuario(nombre, correo, clave, rol)

    if exito:
        flash(mensaje, "success")

        return redirect(url_for("acceso.vista_registro"))

    flash(mensaje, "error")

    return render_template(
        "registro.html",
        nombre=nombre,
        correo=correo,
        rol=rol
    )