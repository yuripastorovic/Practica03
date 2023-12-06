import gestion_BBDD
import gestion_alumno
import gestion_curso
import gestion_profesor
import utiles_validaciones


def matricular_profesor_curso(conn):
    """
    Funcion que crea la relacion entre cursos y profesores.
    :param conn: la conexion a la bbdd
    :return: None
    """
    done = False
    while not done:
        print("Relacionar profesores y cursos.")
        print("Introduzca el dni del profesor que desea relacionar.")
        curso = None
        dni = utiles_validaciones.check_dni()  #Pedimos dni para mas adelante coger el profesor
        if dni is not None and not utiles_validaciones.unique_dni(conn, dni):  #Si el dni existe
            curso = gestion_curso.busqueda_unica(conn)  #Pillamos el curso por el nombre
        if curso is not None:

            profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Pillamos el profesor
            datos = {"id_profesor": profesor[0][0], "cod_curso": curso[0]}  #Montamos el diccionario de datos
            if gestion_BBDD.existe_relacion(conn, "cursos_profesores", datos):  #Si ya estan relacionados se notifica, pues no tiene sentidos volver a hacer el mismo insert
                print(profesor[0][2] + " ya imparte " + curso[1])
            else:  #Si no estan relacionados
                prof_ant = gestion_BBDD.tiene_profesor(conn, curso[0])  #Pillamos la posible relacion del curso
                if len(prof_ant) > 0:  #Si el curso ya tenia profesor
                    if utiles_validaciones.confirmacion(curso[1] + " ya tiene profesor, desea sustituirlo por " + profesor[0][2] + "?"):  #Se pregunta si quiere sustituirlo
                        para_borrar = {"id_profesor": prof_ant[0][4], "cod_curso": curso[0]}
                        gestion_BBDD.delete(conn, "cursos_profesores", para_borrar)  #Deleteamos la antigua row
                        gestion_BBDD.insert(conn, "cursos_profesores", datos)  #Creamos la nueva
                    else:
                        print("Relacion abortada")
                else:  #Si el curso no tiene relacion
                    if utiles_validaciones.confirmacion("Seguro que desea que " + profesor[0][2] + " imparta " + curso[1] + "?"):  #Preguntamos confirmacion
                        gestion_BBDD.insert(conn, "cursos_profesores", datos)  #Hacemos insert
                    else:
                        print("Relacion abortada")

        if not utiles_validaciones.confirmacion("Desea relacionar otro profesor con otro curso?"):  #Esto para relacionar mas de uno
            done = True


def desmatricular_profesor_curso(conn):
    """
    Funcion que desbindea un profesor y un curso
    :param conn: la conexion a la bbdd
    :return: None
    """
    done = False
    while not done:

        print("Desrelacionar profesores y cursos.")
        curso = None
        dni = utiles_validaciones.check_dni()  #Pedimos del dni del profeosr
        if dni is not None and not utiles_validaciones.unique_dni(conn, dni):
            curso = gestion_curso.busqueda_unica(conn)  #conseguimos el curso por nombre
        if curso is not None:

            profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Cogemso el profesor por el dni
            datos = {"id_profesor": profesor[0][0], "cod_curso": curso[0]}  #Montamos el diccionario
            if gestion_BBDD.existe_relacion(conn, "cursos_profesores", datos):  #Si hay relacion
                if utiles_validaciones.confirmacion("Seguro que desea que " + profesor[0][2] + " deje de ser el profesor de " + curso[1]):  #Pedimos confirmacion
                    gestion_BBDD.delete(conn, "cursos_profesores", datos)  #Deleteamos

                else:
                    print("Desrelacion abortada")
            else:
                print(profesor[0][2] + " no es el profesor de " + curso[1])  #si no hay relacion se notifica

        if not utiles_validaciones.confirmacion("Desea desrelacionar otro profesor con otro curso?"):  #Esto para desrealacionar mas de uno
            done = True
