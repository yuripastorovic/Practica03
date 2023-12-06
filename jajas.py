import pymysql
from datetime import datetime

import gestion_BBDD
import gestion_curso
import utiles_validaciones
import gestion_alumno

def add_alum_curso(conn, alumno, curso):
    cur = conn.cursor()  # Cursor
    cur.execute("INSERT INTO cursos_alumnos (num_exp, cod_curso) VALUES ('" + alumno+ "','" + curso +  "');")


def del_alum_curso(conn, datos):
    cur = conn.cursor()  # Cursor
    cur.execute("DELETE FROM cursos_alumnos WHERE num_exp = " + datos['num_exp'] + " AND cod_curso ="+ datos['cod_curso'] +";")


def existe_relacion(conn, tabla, primary):
    """
    Funcion de apoyos que busca en las tablas intermendias si existe relacion entre alumno-curso o profesor curso
    :param conn: conexion con BBDD
    :param tabla: tabla sobre la que miarar
    :param primary: diccionario de datos a comparar
    :return: True: existen coincidencias
    :return: False: no existen coincidencias
    """
    cur = conn.cursor()  # Generamos cursor
    if tabla == "cursos_alumnos":
        cur.execute("SELECT cursos_alumnos.* FROM cursos_alumnos WHERE num_exp = " + primary['num_exp'] + " AND cod_curso =" + primary['cod_curso'] +";")
    else:
        cur.execute(
            "SELECT cursos_profesores.* FROM cursos_profesores WHERE num_exp = " + primary['id_profesor'] + " AND cod_curso =" + primary['cod_curso'] + ";")
    out = cur.fetchall()
    if len(out)==1:
        return True
    else:
        return False
def selec_one_from_tabla(coon, tabla, primary):
    """
    Funcion que devuelve los campos de una row de una tabla que se desea buscar
    :param coon: la conexion a la bbdd
    :param tabla: la tabla que contiene la row
    :param primary: la primary key de la row que se desea mostrar
    :return: una tupla con los campos de la row
    """
    cur = coon.cursor()  # Generamos cursor

    if tabla == "alumnos":  # Elegimos la tabla en la que hacer un select
        cur.execute("SELECT " + tabla + ".* FROM " + tabla + " WHERE num_exp = " + str(primary) + ";")
    elif tabla == "profesores":
        cur.execute(
            "SELECT " + tabla + ".* FROM " + tabla + " WHERE dni = '" + primary + "';")
    elif tabla == "cursos":
        cur.execute("SELECT " + tabla + ".* FROM " + tabla + " WHERE nombre = '" + primary + "';")

    out = cur.fetchall()  # Fetcheamos el resultado del cursor

    return out  # Devolvemos la tupla


def matricular_curso_alumno(conn):
    salida = False
    while not salida:
        print("Relacionar alumnos y cursos.")
        alumno = gestion_alumno.busqueda_unica()
        if alumno is not None:
            curso= gestion_curso.busqueda_unica()
            if curso is not None:
                if utiles_validaciones.confirmacion("Desea matricuar al alumno "+alumno[1]+", al curso "+curso[1]+"?"):
                    datos ={"num_exp": alumno[0], "cod_curso": curso[0]}
                    gestion_BBDD.insert(conn, "cursos_alumnos",datos)
                else:
                    print("Matriculacion abortada")
        if not utiles_validaciones.confirmacion("Desea matricular otro alumno?"):
            print("Voviendo al menu anterior")
            salida = True

def desmatricular_curso_alumno(conn):
    salida = False
    while not salida:
        print("Relacionar alumnos y cursos.")
        alumno = gestion_alumno.busqueda_unica()
        if alumno is not None:
            curso = gestion_curso.busqueda_unica()
            if curso is not None:
                if utiles_validaciones.confirmacion("Desea desmatricuar al alumno " + alumno[1] + ", al curso " + curso[1] + "?"):
                    datos = {"num_exp": alumno[0], "cod_curso": curso[0]}
                    gestion_BBDD.delete(conn, "cursos_alumnos", datos)
                else:
                    print("Desmatriculacion abortada")
        if not utiles_validaciones.confirmacion("Desea dematricular otro alumno?"):
            print("Voviendo al menu anterior")
            salida = True