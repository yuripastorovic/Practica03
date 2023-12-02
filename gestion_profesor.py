"""
this is gestion_profesion
"""
import utiles_validaciones
import gestion_BBDD


def alta(conn):
    print("Alta profesor:")
    done = False
    while not done:
        dni = None
        nombre = None
        direccion = None
        telefono = None
        dni = utiles_validaciones.check_dni()
        if dni is not None:
            nombre = utiles_validaciones.check_campo("nombre", 25)
        if nombre is not None:
            direccion = utiles_validaciones.check_campo("direccion, 50")
        if direccion is not None:
            telefono = utiles_validaciones.check_telefono()
        if telefono is not None:

            datos = {"dni":dni, "nombre": nombre, "direccion": direccion, "telefono": telefono}

            gestion_BBDD.insert(conn, "profesores", datos)

        if not utiles_validaciones.confirmacion("Quieres tratar de dar de alta otro profesor?"):
            done = True


def baja(conn):
    return None


def buscar(conn):
    return None


def mostrar_todos(conn):
    return None


def modificar(conn):
    return None
