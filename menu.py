"""
Este fichero Python se de organizar el menu y todas sus opciones
"""
import gestion_BBDD
import gestion_alumno
import gestion_profesor
import gestion_curso
import gestion_relaciones


def menu_alumno(conn):
    """
    Funcion que gestiona el menu alumno
    :param conn: Conexion con BBDD
    :return: None
    """
    salida = False
    while not salida:
        respuesta = input("--MENU ALUMNO--\nSeleccione una opcion:\n1. Alta\n2. Baja\n3. Buscar\n4. Modificar\n5. Mostrar Todos\n------\n0. Volver a Main Menu\n")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                gestion_alumno.alta(conn)
            if respuesta == "2":
                gestion_alumno.baja(conn)
            if respuesta == "3":
                gestion_alumno.busqueda(conn)
            if respuesta == "4":
                gestion_alumno.modificar(conn)
            if respuesta == "5":
                gestion_alumno.mostrar_todos(conn)
        else:
            print("\nIntroduzca una opcion valida\n")

def menu_profesor(conn):
    """
    Funcion que gestiona el menu profesor
    :param conn: Conexion con BBDD
    :return: None
    """
    salida = False
    while not salida:
        respuesta = input("--MENU PROFESOR--\nSeleccione una opcion:\n1. Alta\n2. Baja\n3. Buscar\n4. Modificar\n5. Mostrar Todos\n------\n0. Volver a Main Menu\n")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                gestion_profesor.alta(conn)
            if respuesta == "2":
                gestion_profesor.baja(conn)
            if respuesta == "3":
                gestion_profesor.buscar(conn)
            if respuesta == "4":
                gestion_profesor.modificar(conn)
            if respuesta == "5":
                gestion_profesor.mostrar_todos(conn)
        else:
            print("\nIntroduzca una opcion valida\n")


def menu_curso(conn):
    """
    Funcion que gestiona el menu curso
    :param conn: Conexion con BBDD
    :return: None
    """
    salida = False
    while not salida:
        respuesta = input("--MENU CURSO--\nSeleccione una opcion:\n1. Alta\n2. Baja\n3. Buscar\n4. Modificar\n5. Mostrar Todos\n------\n0. Volver a Main Menu\n")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                gestion_curso.alta(conn)
            if respuesta == "2":
                gestion_curso.baja(conn)
            if respuesta == "3":
                gestion_curso.buscar(conn)
            if respuesta == "4":
                gestion_curso.modificar(conn)
            if respuesta == "5":
                gestion_curso.mostrar_todos(conn)
        else:
            print("\nIntroduzca una opcion valida\n")


def menu_relaciones(conn):
    """
    Funcion que gestiona el menu relaciones
    :param conn: Conexion con BBDD
    :return: None
    """
    salida = False
    while not salida:
        respuesta = input("--MENU RELACIONES--\nSeleccione una opcion:\n1. Asinar Profesor a un curso\n2. Desasinar Profesor a un curso\n3. Matricular Alumno a un curso\n4. Desmatricular Alumno de un curso\n------\n0. Volver a Main Menu\n")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                gestion_relaciones.matricular_profesor_curso(conn)
            if respuesta == "2":
                gestion_relaciones.desmatricular_profesor_curso(conn)
            if respuesta == "3":
                gestion_relaciones.matricular_curso_alumno(conn)
            if respuesta == "4":
                gestion_relaciones.desmatricular_curso_alumno(conn)
            if respuesta == "5":
                gestion_curso.mostrar_todos(conn)
        else:
            print("\nIntroduzca una opcion valida\n")


def main_menu(conn):
    """
    Funcion que gestiona el menu principal, accede a los demas menus y termina la ejecucion del programa
    :param conn: Conexion con BBDD
    :return: None
    """
    salida = False
    while not salida:
        respuesta = input("--MAIN MENU--\nSeleccione una opcion:\n1. Alumnos\n2. Profesores\n3. Curso\n4. Matricular Alumno Curso/Asignar Profesor Curso\n------\n0. Cerrar programa\n")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                menu_alumno(conn)
            if respuesta == "2":
                menu_profesor(conn)
            if respuesta == "3":
                menu_curso(conn)
            if respuesta == "4":
                menu_relaciones(conn)
        else:
            print("\nIntroduzca una opcion valida\n")
