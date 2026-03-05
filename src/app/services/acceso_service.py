from app.models.acceso_models import USUARIOS_PERMITIDOS, BLOQUEADOS

def normalizar_nombre(nombre:str) -> str:

#limpiar espacios y normalizar para evitar errores de entrada
    
    return(nombre or "").strip

def validar_acceso(nombre:str)->tuple[bool,str]:
    """ 
    Retorna:
        -permitido(bool)
        -mensaje(str)
    """
    nombre = normalizar_nombre(nombre)

    if nombre == "":
        return False, "Debe ingresar un nombre"
    if nombre in BLOQUEADOS:
        return False, "Usuario bloqueado"
    if nombre in USUARIOS_PERMITIDOS:
        return True, "Acceso permitido"

    return False, "Usuario no registrado"


