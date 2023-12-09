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


