"""
this is gestion_curso
"""
import gestion_BBDD
import utiles_validaciones


def alta(conn):
    """
    Funcion que da de alta un curso en la bbdd.
    :param conn:
    :return:
    """
    print("Alta curso:")
    done = False
    while not done:  #Para dar de alta varios profesores en una ejecucion de la funcion
        nombre = None
        descripcion = None
        nombre = utiles_validaciones.check_campo("nombre", 25)
        if nombre is not None:
            descripcion = utiles_validaciones.check_campo("descripcion", 50)
        if descripcion is not None:

            datos = {"nombre": nombre, "descripcion": descripcion}  #Pasamos los datos a un diccionario

            gestion_BBDD.insert(conn, "cursos", datos)  #Realizamos el insert

            print("Alta realizada con existo")

        if not utiles_validaciones.confirmacion("Quieres tratar de dar de alta otro curso?"):  #Preguntamos si quiere dar otro profesor de alta
            done = True


def buscar(conn):
    """
    Funcion que busca un curso en la bbdd
    :param conn: conexion a la bbdd
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0:
        print("buscar cursos:")
        cursos = gestion_BBDD.selec_all_from_tabla(conn, "cursos")
        print("Nombre de los cursos: ", end="")
        for curso in cursos:
            print(curso[1], ", ", end="")
        print()
        done = False
        while not done:  #Para buscar mas de un profesor
            print("Introduzca el nombre del curso que desea buscar.")
            nombre = utiles_validaciones.check_campo("Nombre", 25)  #Pedimos dni valido
            if nombre is not None:
                curso = gestion_BBDD.selec_one_from_tabla(conn, "cursos", nombre)  #Encontramos al profesor
                if len(curso) > 0:  #Si lo encuentra lo muestra
                    print("Codigo del curso: ", curso[0][0])
                    print("Nombre: ", curso[0][1])
                    print("Descripcion:", curso[0][2])
                    print()

                else:
                    print("No se encontro ningun curso con ese nombre.")

            if not utiles_validaciones.confirmacion("Desea buscar otro curso"):  #Pedimos confirmacion para buscar mas de uno
                done = True

    else:
        print("No hay cursos en la base de datos.")


def mostrar_todos(conn):
    """
    Funcion que muestra por pantalla todos los cursos de la base de datos
    :param conn: la conexion a la bbdd
    :return: None
    """
    cursos = gestion_BBDD.selec_all_from_tabla(conn, "cursos")
    if len(cursos) > 0:
        print("Mostrar todos los cursos:")
        for curso in cursos:
            print("Codigo del curso: ", curso[0])
            print("Nombre: ", curso[1])
            print("Descripcion:", curso[2])
            print()

    else:
        print("No hay cursos en la base de datos.")
