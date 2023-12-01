"""
this is gestion_BBDD
"""
import pymysql


def mysqlconnect():
    """
    Funcion que crea y devuelve la conexion a la base de datos.
    :return: un objeto con la conexion a la BD.
    """
    conn = pymysql.connect(
        host='localhost',
        user='root',
        )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print("Version: ", output)

    return conn


def create_tables(conn):
    """
    Funcion que crea las tablas de la bd
    :param conn:
    :return:
    """
    cur = conn.cursor()

    cur.execute("""CREATE DATABASE IF NOT EXISTS jorge_antonio;""")

    cur.execute("""USE IF EXISTS jorge_antonio;""")

    cur.execute("""SET foreign_key_checks = 1""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        num_exp INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(25) NOT NULL,
        apellido VARCHAR(25) NOT NULL,
        telefono CHAR(9) NOT NULL,
        direccion VARCHAR(50) NOT NULL,
        fech_nacimiento DATE NOT NULL       
    );""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS profesores (
        id_profesor INT AUTO_INCREMENT PRIMARY KEY,
        dni CHAR(9) UNIQUE NOT NULL,
        nombre VARCHAR(25) NOT NULL,
        direccion VARCHAR(50) NOT NULL,
        telefono CHAR(9) NOT NULL
    );""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        cod_curso INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(25) UNIQUE NOT NULL,
        descripcion VARCHAR(50) NOT NULL  
    );""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cursos_profesores (
        id_profesor INT NOT NULL,
        cod_curso INT NOT NULL,
        CONSTRAINT pk_curso_prof PRIMARY KEY (id_profesor, cod_curso),
        CONSTRAINT fk_cur_prof FOREIGN KEY (cod_curso) 
            REFERENCES cursos(cod_curso) 
            ON UPDATE CASCADE 
            ON DELETE CASCADE,
        CONSTRAINT fk_prof FOREIGN KEY (id_profesor) 
            REFERENCES profesores(id_profesor) 
            ON UPDATE CASCADE 
            ON DELETE CASCADE            
    );""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cursos_alumnos (
        num_exp INT NOT NULL,
        cod_curso INT NOT NULL,
        CONSTRAINT pk_curso_prof PRIMARY KEY (num_exp, cod_curso),
        CONSTRAINT fk_cur_alum FOREIGN KEY (cod_curso) 
            REFERENCES cursos(cod_curso) 
            ON UPDATE CASCADE 
            ON DELETE CASCADE,
        CONSTRAINT fk_alum FOREIGN KEY (num_exp) 
            REFERENCES alumnos(num_exp) 
            ON UPDATE CASCADE 
            ON DELETE CASCADE            
    );""")

    conn.commit()

    cur.close()


def insert(conn, tabla, datos):
    """
    Funcion que inserta datos en las tablas de la base de datos
    :param conn:
    :param tabla:
    :param datos:
    :return:
    """
    cur = conn.cursor()

    if tabla == "alumnos":
        cur.execute("INSERT INTO "+tabla+" (nombre, apellido, telefono, direccion, fech_nacimiento) "
            "VALUES ('" + datos["nombre"] + "','" + datos["apellido"] + "','" + datos["telefono"] + "','" + datos["direccion"] + "','" + datos["f_nac"] + "');")
    elif tabla == "profesores":
        cur.execute("INSERT INTO "+tabla+" (dni, nombre, direccion, telefono) "
            "VALUES ('" + datos["dni"] + "','" + datos["nombre"] + "','" + datos["direccion"] + "','" + datos["telefono"] + "');")
    elif tabla == "cursos":
        cur.execute("INSERT INTO "+tabla+" (nombre, descripcion) VALUES ('" + datos["nombre"] + "','" + datos["descripcion"] + "');")
    elif tabla == "cursos_profesores":
        cur.execute("INSERT INTO "+tabla+" (id_profesor, cod_curso) VALUES ('" + datos["id_profesor"] + "','" + datos["cod_curso"] + "');")
    elif tabla == "cursos_alumnos":
        cur.execute("INSERT INTO "+tabla+" (num_exp, cod_curso) VALUES ('" + datos["num_exp"] + "','" + datos["cod_curso"] + "');")

    conn.commit()

    cur.close()


def update(conn, tabla, datos, primary):
    """

    :param conn:
    :param tabla:
    :param datos:
    :param primary:
    :return:
    """
    print('b')


def delete(conn, tabla, primary):
    """

    :param conn:
    :param tabla:
    :param primary:
    :return:
    """
    print('b')
