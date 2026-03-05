from flask import Blueprint, render_template, request, session, redirect, url_for
from app.services.acceso_service import validar_acceso, normalizar_nombre

acceso_bp = Blueprint("acceso", __name__)

@acceso_bp.route("/", methods=["GET"])
def index():
    intentos = session.get("intentos", 0)
    ultimo = session.get("ultimo_nombre", "")
    return render_template("index.html", intentos=intentos, ultimo=ultimo)

@acceso_bp.route("/procesar", methods=["POST"])
def procesar():
    nombre = normalizar_nombre(request.form.get("nombre", ""))

    session["intentos"] = session.get("intentos", 0) + 1
    session["ultimo_nombre"] = nombre

    permitido, mensaje = validar_acceso(nombre)

    return render_template(
        "resultado.html",
        nombre=nombre,
        permitido=permitido,
        mensaje=mensaje
    )

@acceso_bp.route("/reiniciar", methods=["POST"])
def reiniciar():
    session.clear()
    return redirect(url_for("acceso.index"))

