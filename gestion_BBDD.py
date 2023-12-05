"""
this is gestion_BBDD
"""
import pymysql
from datetime import datetime
import utiles_validaciones

def mysqlconnect():
    """
    Funcion que crea y devuelve la conexion a la base de datos.
    :return: un objeto con la conexion a la BD.
    """
    datos=utiles_validaciones.lectura()

    conn = pymysql.connect(
        host=datos['localhost'],
        user=datos['user'],
        password=datos['password'],
        port=datos['port']
    )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print("Version: ", output)

    create_tables(conn)  # Crea las tablas si no existen

    return conn  # Devuelve la conexion con la BBDD


def create_tables(conn):
    """
    Funcion que crea las tablas de la bd
    :param conn: la conexion a la bbdd
    :return: None
    """
    cur = conn.cursor()

    cur.execute("""CREATE DATABASE IF NOT EXISTS jorge_antonio;""")  # Creamos la database si no existe

    cur.execute("""USE jorge_antonio;""")  # Usamos la database

    cur.execute("""SET foreign_key_checks = 1;""")  # Habilitamos las foreign keys

    cur.execute(""" 
    CREATE TABLE IF NOT EXISTS alumnos (
        num_exp INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(25) NOT NULL,
        apellido VARCHAR(25) NOT NULL,
        telefono CHAR(9) NOT NULL,
        direccion VARCHAR(50) NOT NULL,
        fech_nacimiento DATE NOT NULL       
    );""")  # Tabla alumnos

    cur.execute("""
    CREATE TABLE IF NOT EXISTS profesores (
        id_profesor INT AUTO_INCREMENT PRIMARY KEY,
        dni CHAR(9) UNIQUE NOT NULL,
        nombre VARCHAR(25) NOT NULL,
        direccion VARCHAR(50) NOT NULL,
        telefono CHAR(9) NOT NULL
    );""")  # Tabla profesores

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        cod_curso INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(25) UNIQUE NOT NULL,
        descripcion VARCHAR(50) NOT NULL  
    );""")  # Tabla cursos

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
    );""")  # Tabla que relaciona cursos y profesores

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
    );""")  # Tabla que relaciona cursos y alumnos

    conn.commit()  # commiteamos cambios

    cur.close()  # cerramos el cursos


def insert(conn, tabla, datos):
    """
    Funcion que inserta datos en las tablas de la base de datos
    :param conn: la conexion a la bbdd
    :param tabla: la tabla en la que se va a insertar
    :param datos: los datos de la row almacenados en un diccionario
    :return: None
    """
    cur = conn.cursor()  # Cursor

    if tabla == "alumnos":  # El insert de alumno sacando los datos de un diccionario
        cur.execute("INSERT INTO " + tabla + " (nombre, apellido, telefono, direccion, fech_nacimiento) "
            "VALUES ('" + datos["nombre"] + "','" + datos["apellido"] + "','" + datos["telefono"] + "','" + datos["direccion"] + "','" + datos["fech_nacimiento"] + "');")
    elif tabla == "profesores":  # El insert de profesores sacando los datos de un diccionario
        cur.execute("INSERT INTO " + tabla + " (dni, nombre, direccion, telefono) "
            "VALUES ('" + datos["dni"] + "','" + datos["nombre"] + "','" + datos["direccion"] + "','" + datos["telefono"] + "');")
    elif tabla == "cursos":  # El insert de cursos sacando los datos de un diccionario
        cur.execute("INSERT INTO " + tabla + " (nombre, descripcion) "
            "VALUES ('" + datos["nombre"] + "','" + datos["descripcion"] + "');")
    elif tabla == "cursos_profesores":  # El insert de crusos-profesores sacando los datos de un diccionario
        cur.execute(
            "INSERT INTO " + tabla + " (id_profesor, cod_curso) VALUES ('" + datos["id_profesor"] + "','" + datos["cod_curso"] + "');")
    elif tabla == "cursos_alumnos":  # El insert de cursos-alumno sacando los datos de un diccionario
        cur.execute("INSERT INTO " + tabla + " (num_exp, cod_curso) VALUES ('" + datos["num_exp"] + "','" + datos["cod_curso"] + "');")

    conn.commit()  # Commit

    cur.close()  # Colse cursor


# multiples cambios
def update(conn, tabla, datos, primary):
    """
    Metodo que se encarga de actualizar los valores de la tabla.
    :param conn: conexion con la BBDD
    :param tabla: tabla sobre la que se va a realizar la modificacion
    :param datos: diccionario de datos que contiene los datos actualizados
    :param primary: Primary key del registro a modificar
    :return: None
    """
    cur = conn.cursor()
    if tabla == 'alumnos':  # Seleccionamos la tabla en la que vamos a hacer el update
        #print(type(datos["fech_nacimiento"]))
        #fecha = datetime.date.strptime(str(datos["fech_nacimiento"]), "%Y-%m-%d").strftime("%Y-%m-%d")
        
        cur.execute("UPDATE alumnos SET nombre = '" + datos['nombre'] + "', apellido = '" + datos['apellido'] + "', telefono = '" +
            datos['telefono'] + "', direccion = '" + datos['direccion'] + "', fech_nacimiento = '" + str(datos["fech_nacimiento"]) + "' WHERE num_exp = " + str(primary) + ";")

    elif tabla == 'profesores':
        cur.execute("UPDATE profesores SET dni = '" + datos['dni'] + "', nombre = '" + datos['nombre'] + "', direccion = '" + datos['direccion'] + "', telefono = '" +
            datos['telefono'] + "' WHERE dni = '" + primary + "';")  # Realizamos el update en base a la primary

    elif tabla == 'cursos':
        cur.execute("UPDATE cursos SET nombre = '" + datos['nombre'] + "', descripcion = '" + datos['descripcion'] + "' WHERE nombre = '" + primary + "';")

    conn.commit()  # Commiteamos

    cur.close()  # cerramos cursor


def delete(conn, tabla, primary):
    """
    funcion que borra una row de la tabla.
    :param conn: la conexion a la bbdd
    :param tabla: la tabla en la que se borra
    :param primary: la primary key de la row que se va a borrar
    :return: None
    """
    cur = conn.cursor()  # Creamos cursor

    if tabla == 'alumnos':  # Selccionaos la tabla en la que vamos a hacer el delete
        cur.execute("DELETE FROM " + tabla + " WHERE num_exp = " + str(primary) + ";")  # Si la primary concuerda borramos la row
    elif tabla == 'profesores':
        cur.execute(
            "DELETE FROM " + tabla + " WHERE dni = '" + primary + "';")  # Si la primary concuerda borramos la row
    elif tabla == 'cursos':
        cur.execute("DELETE FROM " + tabla + " WHERE nombre = '" + primary + "';")  # Si la primary concuerda borramos la row

    conn.commit()  # Commit

    cur.close()  # Colse cursor


def selec_all_from_tabla(conn, tabla):
    """
    Funcion que muestra tod el contenido de una tabla
    :param conn: la conexion a la bbdd
    :param tabla: la tabla que se desea mostrar
    :return: una tupla con el contenido
    """
    cur = conn.cursor()  # Ceamos cursor

    cur.execute("SELECT " + tabla + ".* FROM " + tabla + ";")  # Seleccionamos tod el contenido de una tabla
    out = cur.fetchall()  # Lo fetchamos

    return out  # Lo devolvemos


def busqueda(coon, tabla, contexto, parametro):
    """
    Funcion que devuelve los campos de una row de una tabla que se desea buscar
    :param coon: la conexion a la bbdd
    :param tabla: la tabla que contiene la row
    :param primary: la primary key de la row que se desea mostrar
    :return: una tupla con los campos de la row
    """
    cur = coon.cursor()  # Generamos cursor

    if tabla == 'alumnos':  # Elegimos la tabla en la que hacer un select
        if contexto == 'doble':
            elementos = parametro.split('&&')
            nom = elementos[0]
            ape = elementos[1]
            cur.execute('SELECT ' + tabla + '.* FROM ' + tabla + ' WHERE nombre = \'' + nom + '\' AND apellido = \'' + ape + '\';')
        elif contexto == 'nombre':
            cur.execute('SELECT ' + tabla + '.* FROM ' + tabla + ' WHERE nombre = \'' + parametro + '\';')
        else:
            cur.execute('SELECT ' + tabla + '.* FROM ' + tabla + ' WHERE apellido = \'' + parametro + '\';')
    elif tabla == 'profesores':
        cur.execute('SELECT ' + tabla + '.* FROM ' + tabla + ' WHERE ' + contexto + ' = \'' + parametro + '\';')  # esto esta mal la primary no es el DNI
    elif tabla == 'cursos':
        cur.execute('SELECT ' + tabla + '.* FROM ' + tabla + ' WHERE nombre = \'' + parametro + '\';')

    out = cur.fetchall()  # Fetcheamos el resultado del cursor

    return out  # Devolvemos la tupla


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
