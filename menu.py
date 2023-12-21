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
    espai = "\n\t\t\t[--]\t" + '\033[92m'
    espai1 = '\033[0m' + "\t\t[--]\n\t\t\t[--]\t" + '\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai + " " * (15) + "--MENU ALUMNO--" + " " * (15) + espai1 + "Seleccione una opcion:" + " " * (
                23) + espai1 + "1. Alta" + " " * (37) + espai1 + "2. Baja" + " " * (37) + espai1 + "3. Buscar" + " " * (
                37) + espai1 + "4. Modificar" + " " * (35) + espai1 + "5. Mostrar Todos" + " " * (31) + espai1 + " " * (
                19) + "------" + " " * (19) + espai1 + "0. Volver a Main Menu" + " " * (23) + espai1 + "")
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
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")


def menu_profesor(conn):
    """
    Funcion que gestiona el menu profesor
    :param conn: Conexion con BBDD
    :return: None
    """
    espai = "\n\t\t\t[--]\t"+'\033[92m'
    espai1 = '\033[0m'+"\t\t[--]\n\t\t\t[--]\t"+'\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai + " " * (15) + "--MENU PROFESOR--" + " " * (15) + espai1 + "Seleccione una opcion:" + " " * (
                23) + espai1 + "1. Alta" + " " * (37) + espai1 + "2. Baja" + " " * (37) + espai1 + "3. Buscar" + " " * (
                35) + espai1 + "4. Modificar" + " " * (35) + espai1 + "5. Mostrar Todos" + " " * (31) + espai1 + " " * (
                19) + "------" + " " * (19) + espai1 + "0. Volver a Main Menu" + " " * (23) + espai1 + "")
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
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")


def menu_curso(conn):
    """
    Funcion que gestiona el menu curso
    :param conn: Conexion con BBDD
    :return: None
    """
    espai = "\n\t\t\t[--]\t"+'\033[92m'
    espai1 = '\033[0m'+"\t\t[--]\n\t\t\t[--]\t"+'\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai + " " * (15) + "--MENU CURSO--" + " " * (15) + espai1 + "Seleccione una opcion:" + " " * (
                25) + espai1 + "1. Alta" + " " * (39) + espai1 + "2. Baja" + " " * (39) + espai1 + "3. Buscar" + " " * (
                35) + espai1 + "4. Modificar" + " " * (33) + espai1 + "5. Mostrar Todos" + " " * (
                29) + espai1 + "------" + " " * (39) + espai1 + "0. Volver a Main Menu" + " " * (25) + espai1 + "")
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
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")


def menu_relaciones(conn):
    """
    Funcion que gestiona el menu relaciones
    :param conn: Conexion con BBDD
    :return: None
    """
    espai = "\n\t\t\t[--]\t"+'\033[92m'
    espai1 = '\033[0m'+"\t\t[--]\n\t\t\t[--]\t"+'\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai + " " * (15) + "--MENU RELACIONES--" + " " * (15) + espai1 + "Seleccione una opcion:" + " " * (
                27) + espai1 + "1. Asinar Profesor a un curso" + " " * (
                19) + espai1 + "2. Desasinar Profesor a un curso" + " " * (
                19) + espai1 + "3. Matricular Alumno a un curso" + " " * (
                19) + espai1 + "4. Desmatricular Alumno de un curso" + " " * (15) + espai1 + " " * (
                19) + "------" + " " * (23) + espai1 + "0. Volver a Main Menu" + " " * (27) + espai1 + "")
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
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")


def main_menu(conn):
    """
    Funcion que gestiona el menu principal, accede a los demas menus y termina la ejecucion del programa
    :param conn: Conexion con BBDD
    :return: None
    """
    espai = "\n\t\t[--]\t"+'\033[92m'
    espai1 = '\033[0m'+"\t[--]\n\t\t[--]\t"+'\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai + " " * (19) + "--MAIN MENU--" + " " * (19) + espai1 + "Seleccione una opcion:" + " " * (
                28) + espai1 + "1. Alumnos" + " " * (40) + espai1 + "2. Profesores" + " " * (
                36) + espai1 + "3. Curso" + " " * (
                40) + espai1 + "4. Matricular Alumno Curso/Asignar Profesor Curso" + espai1 + " " * (
                10) + "------" + " " * (34) + espai1 + "0. Cerrar programa" + " " * (32) + espai1 + "")
        respuesta = input()
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
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")
