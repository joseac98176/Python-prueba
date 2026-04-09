from app.database.connection import get_connection

def existe_usuario_por_correo(correo: str) -> bool:
    connection = get_connection()

    cursor = connection.cursor()

    query = "SELECT COUNT(*) FROM usuarios WHERE correo = %s"

    cursor.execute(query, (correo,))

    resultado = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return resultado > 0


def registrar_usuario(nombre: str, correo: str, clave: str, rol: str = "empleado") -> None:

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO usuarios (nombre, correo, clave, rol, estado)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (nombre, correo, clave, rol, True))

    connection.commit()

    cursor.close()
    connection.close()

